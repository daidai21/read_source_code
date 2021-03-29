#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : hello2.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 一  3/29 23:46:33 2021
# #############################################################################

import curio


async def countdown(n):
    while n > 0:
        print('T-minus', n)
        await curio.sleep(1)
        n -= 1


async def kid(x, y):
    try:
        print('Getting around to doing my homework')
        await curio.sleep(1000)
        return x * y
    except curio.CancelledError:  # 取消任务的时候抛错
        print("No go diggy die!")
        raise


async def parent():
    kid_task = await curio.spawn(kid, 37, 42)  # spawn: 生产
    count_task = await curio.spawn(countdown, 10)  # curio.spawn() 启动并发任务

    await count_task.join()  # .join() 等待任务结束

    print("Are you done yet?")
    try:
        result = await curio.timeout_after(5, kid_task.join)  # 5s后就timeout
        print("Result:", result)
    except curio.TaskTimeout as e:  # 捕捉timeout，取消任务
        print("We've got to go!")
        await kid_task.cancel()


if __name__ == '__main__':
    # 创建新窗口
    # >  python3 -m curio.monitor
    # >  ps # 可以看到线程状态
    # >  w 4 # 查看堆栈跟踪
    curio.run(parent, with_monitor=True)
