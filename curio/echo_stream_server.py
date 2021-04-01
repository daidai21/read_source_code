#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : echo_stream_server.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:05:42 2021
# #############################################################################

from curio import run
from curio import spawn
from curio import tcp_server


async def echo_client(client, addr):
    print('Connection from', addr)
    s = client.as_stream()
    while True:
        data = await s.read(100000)
        if not data:
            break
        await s.write(data)
    print('Connection closed')


if __name__ == '__main__':
    run(tcp_server, '', 25000, echo_client)
    # >>> python3 echo_stream_server.py 
    # new terminal
    # > nc localhost 25000
    # > hello
