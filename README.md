# scn
Scaling networks scripts &amp; guides

## Scripts

### 2-router-vrrp.py

Also see: https://docs.vyos.io/en/latest/high-availability.html

Configure two routers to act as one ipv4 vrrp router. Sets config over telnet.
Client is not automatically configured, just set the ip to \*.\*.\*.4 and default gateway to \*.\*.\*.1 (ip of virtual router).

## Config

### vyos-roas.txt

Config for ipv6 vyos router-on-a-stick between VLANS 10 and 20.

## Project

### scn.gns3

GNS3 project used for all scripts / configs.
