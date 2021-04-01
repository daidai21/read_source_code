#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : tasks_communicate.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:34:47 2021
# #############################################################################

import curio


async def producer(queue):
    for n in range(10):
        await queue.put(n)
    await queue.join()
    print('Producer done')


async def consumer(queue):
    while True:
        item = await queue.get()
        print('Consumer got', item)
        await queue.task_done()


async def main():
    q = curio.Queue()
    prod_task = await curio.spawn(producer, q)
    cons_task = await curio.spawn(consumer, q)
    await prod_task.join()
    await cons_task.cancel()


if __name__ == '__main__':
    curio.run(main)
