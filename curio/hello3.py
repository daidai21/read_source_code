#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : hello3.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 一  3/29 23:53:13 2021
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
        await curio.sleep(4)  # 修改为6，结果不一样，kid和countdown执行结束的先后顺序对g.result有影响
        return x * y
    except curio.CancelledError:  # 取消任务的时候抛错
        print("No go diggy die!")
        raise


async def parent():
    async with curio.TaskGroup(wait=any) as g:
        await g.spawn(kid, 37, 42)
        await g.spawn(countdown, 5)

    if g.result is None:
        print("Why didn't you finish?")
    else:
        print("Result:", g.result)


if __name__ == '__main__':
    # 创建新窗口
    # >  python3 -m curio.monitor
    # >  ps # 可以看到线程状态
    # >  w 4 # 查看堆栈跟踪
    curio.run(parent, with_monitor=True)
