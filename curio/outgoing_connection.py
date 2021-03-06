#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : outgoing_connection.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:17:20 2021
# #############################################################################

import curio


async def main():
    sock = await curio.open_connection('www.python.org', 80)
    async with sock:
        await sock.sendall(b'GET / HTTP/1.0\r\nHost: www.python.org\r\n\r\n')
        chunks = []
        while True:
            chunk = await sock.recv(10000)
            if not chunk:
                break
            chunks.append(chunk)

    response = b''.join(chunks)
    print(response.decode('latin-1'))


if __name__ == '__main__':
    curio.run(main)
    # >>> python3 outgoing_connection.py
