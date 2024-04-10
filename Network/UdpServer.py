#!/usr/bin/env python
import socket

server_address = '127.0.0.1'
port_server = 9000
max_sz = 1024

# Server: Create a datagram socket
udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to socket
udp_server.bind((server_address, port_server))
print('UDP Started.')
# Intercept incoming datagramms
count = 0
while (True):
    print('\tUDP Server Listening...')
    request_set = udp_server.recvfrom(max_sz)
    count += 1
    print(f'\t{count}.) {request_set}')
    udp_server.sendto(str.encode('ACK - Server'), request_set[1])
