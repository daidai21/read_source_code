#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : fib.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 一  3/29 23:57:40 2021
# #############################################################################

import curio


async def countdown(n):
    while n > 0:
        print('T-minus', n)
        await curio.sleep(1)
        n -= 1


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# async def kid(x, y):
#     try:
#         print('Getting around to doing my homework')
#         async with curio.TaskGroup() as g:
#             tx = await g.spawn(curio.run_in_process, fib, x)
#             ty = await g.spawn(curio.run_in_process, fib, y)
#         return tx.result * ty.result
#     except curio.CancelledError:
#         print("Guess I'll fail!")
#         raise

async def kid(x, y):
    try:
        print('Getting around to doing my homework')
        fx = await curio.run_in_thread(fib, x)
        fy = await curio.run_in_thread(fib, y)
        return fx*fy
    except curio.CancelledError:
        print("No go diggy die!")
        raise

async def parent():
    async with curio.TaskGroup(wait=any) as g:
        await g.spawn(kid, 37, 42)
        await g.spawn(countdown, 10)

    if g.result is None:
        print("Why didn't you finish?")
    else:
        print("Result:", g.result)


if __name__ == '__main__':
    curio.run(parent, with_monitor=True)
    # > python3 fib.py
    # 新窗口
    # > python3 -m curio.monitor
    # > ps 寻找State为RUNNING的Task id
    # > w 5  # 上一步的taskId
