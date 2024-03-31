#!/usr/bin/env python
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()  # создаем объект запроса
    arp_request.pdst = ip  # подставляется IP-адрес из параметров
    print(arp_request.summary())  # общая информация о ARP-запросе
    scapy.ls(scapy.ARP())


scan('192.168.1.254')
