#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : producer.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:51:10 2021
# #############################################################################

from curio import Channel, run


async def producer(ch):
    c = await ch.accept(authkey=b'peekaboo')
    for i in range(10):
        await c.send(i)  # Send some data
    await c.send(None)


if __name__ == '__main__':
    ch = Channel(('localhost', 30000))
    run(producer, ch)
    # >>> python3 producer.py
