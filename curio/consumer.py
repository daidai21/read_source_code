#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : consumer.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:51:19 2021
# #############################################################################

from curio import Channel, run


async def consumer(ch):
    c = await ch.connect(authkey=b'peekaboo')
    while True:
        msg = await c.recv()
        if msg is None:
            break
        print('Got:', msg)


if __name__ == '__main__':
    ch = Channel(('localhost', 30000))
    run(consumer, ch)
    # >>> python3 consumer.py
