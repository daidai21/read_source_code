#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : echo_server.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 二  3/30 00:07:26 2021
# #############################################################################

from curio import run, tcp_server


# async def echo_client(client, addr):
#     print('Connection from', addr)
#     while True:
#         data = await client.recv(1000)
#         if not data:
#             break
#         await client.sendall(data)
#     print('Connection closed')


async def echo_client(client, addr):
    print("Connection from", addr)
    async with client.as_stream() as s:
        async for line in s:
            await s.write(line)
    print('Connection closed')


if __name__ == '__main__':
    run(tcp_server, '', 25000, echo_client)
    # > python3 echo_server.py
    # 新窗口
    # > nc localhost 25000
    # > hello
