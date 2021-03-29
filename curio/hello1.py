#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : hello1.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 一  3/29 23:37:51 2021
# #############################################################################

import curio


async def countdown(n):
    while n > 0:
        print('T-minus', n)
        await curio.sleep(1)
        n -= 1


async def kid(x, y):
    print('Getting around to doing my homework')
    await curio.sleep(15)
    return x * y


async def parent():
    kid_task = await curio.spawn(kid, 37, 42)  # spawn: 生产
    count_task = await curio.spawn(countdown, 10)  # curio.spawn() 启动并发任务

    await count_task.join()  # .join() 等待任务结束

    print("Are you done yet?")
    result = await kid_task.join()

    print("Result:", result)


if __name__ == '__main__':
    # curio.run(parent)

    # 创建新窗口
    # >  python3 -m curio.monitor
    # >  ps # 可以看到线程状态
    # >  w 4 # 查看堆栈跟踪
    curio.run(parent, with_monitor=True)
