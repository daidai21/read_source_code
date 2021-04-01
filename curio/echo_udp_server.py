#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : echo_udp_server.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:07:48 2021
# #############################################################################

import curio
from curio import socket


async def udp_echo(addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(sock)
    sock.bind(addr)
    print(sock)
    while True:
        data, addr = await sock.recvfrom(10000)
        print('Received from', addr, data)
        await sock.sendto(data, addr)


if __name__ == '__main__':
    curio.run(udp_echo, ('', 25000))
    # >>> python3 echo_udp_server.py 
    # new terminal
    # >>> echo "hello" | nc -4u -w0 0.0.0.0 25000
