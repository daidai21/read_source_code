#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : hello.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 一  3/29 23:36:35 2021
# #############################################################################

import curio


async def countdown(n):
    while n > 0:
        print('T-minus', n)
        await curio.sleep(1)
        n -= 1


if __name__ == '__main__':
    curio.run(countdown, 10)
