#!/usr/bin/env python
import socket

server_socket = ('127.0.0.1', 9000)
max_sz = 1024
def send(request):
    msg_buffer = str.encode(request)
    # Create a UDP Client
    udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Senda a datagram to a UDP server
    udp_client.sendto(msg_buffer, server_socket)
    # Get the Server's response:
    response = udp_client.recvfrom(max_sz)
    print(f'Response: [{response}]')
    udp_client.close()

send('Client Hello')
