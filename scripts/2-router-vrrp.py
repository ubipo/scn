from telnetlib import Telnet
import getpass
from ipaddress import IPv4Address, IPv4Network
import itertools


def execute(tn: Telnet, commands: str, prompt: str):
    for command in commands:
        tn.write(command.encode('ascii') + b"\n")
        tn.read_until(prompt.encode('ascii'))

def execute_config(tn: Telnet, commands: str):
    execute(tn, commands, '# ')

def login(tn: Telnet, username: str, password: str):
    tn.write(b'\n')
    tn.read_until(b"login: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

def enter_config(tn: Telnet):
    execute_config(tn, ['configure'])

def set_dhcp(tn: Telnet, interface: str):
    execute_config(tn, [
        f'set interfaces ethernet {interface} address dhcp'
    ])

def set_static(tn: Telnet, interface: str, ip: IPv4Address, prefix_len: int):
    execute_config(tn, [
        f'set interfaces ethernet {interface} address {ip}/{prefix_len}'
    ])

def set_vrrp(tn: Telnet, interface: str, ip: IPv4Address, prefix_len: int, group_name: str, vrid: int):
    execute_config(tn, [
        f'set high-availability vrrp group {group_name} vrid {vrid}',
        f'set high-availability vrrp group {group_name} interface {interface}',
        f'set high-availability vrrp group {group_name} virtual-address {ip}/{prefix_len}'
    ])

def commit(tn: Telnet):
    execute_config(tn, ['commit'])


def start():
    print('Make sure you are logged out and are starting with a clean config')
    network = IPv4Network(input('Network: '))
    group_name = input('VRRP group name: ')
    vrid = input('Virtual router ID: ')
    router_1_telnet_port = input('Router 1 telnet port: ')
    router_2_telnet_port = input('Router 2 telnet port: ')
    client_telnet_port = input('Client telnet port: ')
    print('Assuming same credentials for all three vyos machines...')
    username = input("Username: ")
    password = getpass.getpass()

    hosts = list(itertools.islice(network.hosts(), 4))
    virtual_router_ip = hosts[0]
    router_1_ip = hosts[1]
    router_2_ip = hosts[2]
    client_ip = hosts[3]

    with Telnet('localhost', router_1_telnet_port) as tn:
        login(tn, username, password)
        enter_config(tn)
        set_dhcp(tn, 'eth0')
        set_static(tn, 'eth1', router_1_ip, network.prefixlen)
        set_vrrp(tn, 'eth1', virtual_router_ip, network.prefixlen, group_name, vrid)
        commit(tn)
        print('Router 1 done!')

    with Telnet('localhost', router_2_telnet_port) as tn:
        login(tn, username, password)
        enter_config(tn)
        set_dhcp(tn, 'eth0')
        set_static(tn, 'eth1', router_2_ip, network.prefixlen)
        set_vrrp(tn, 'eth1', virtual_router_ip, network.prefixlen, group_name, vrid)
        commit(tn)
        print('Router 2 done!')


if __name__ == "__main__":
    start()
