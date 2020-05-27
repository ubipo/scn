# scn
Scaling networks scripts &amp; guides

To use IOU devices:
1. Search for & download {name of network hardware provider, rhymes with asco}IOU{name of program to generate keys, rhymes with yen}.py
2. Download https://gns3.com/marketplace/appliance/iou-l2 and https://www.gns3.com/marketplace/appliance/cisco-iou-l3 appliance
3. Search for & download L2 / L3 .bin files, most should work out-of-the-box with the appliance files (also see https://docs.gns3.com/appliances/cisco-iou-l2.html).


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
I haven't tested if importing this in another GNS3 instance actually works.
All IOU and TinyCore devices are run in the GNS3 VM in VMware workstation 11.
VyOS's are run in Qemu/KVM.
