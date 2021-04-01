#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : a_task_and_a_thread_communicate.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:36:37 2021
# #############################################################################

import threading
import curio


# A thread - standard python
def producer(queue):
    for n in range(10):
        queue.put(n)
    queue.join()
    print('Producer done')


# A task - Curio
async def consumer(queue):
    while True:
        item = await queue.get()
        print('Consumer got', item)
        await queue.task_done()


async def main():
    q = curio.UniversalQueue()
    prod_task = threading.Thread(target=producer, args=(q, ))
    prod_task.start()
    cons_task = await curio.spawn(consumer, q)
    await curio.run_in_thread(prod_task.join)
    await cons_task.cancel()


if __name__ == '__main__':
    curio.run(main)
