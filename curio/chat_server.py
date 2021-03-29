#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : chat_server.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 二  3/30 00:21:13 2021
# #############################################################################

from curio import run, spawn, TaskGroup, Queue, tcp_server

messages = Queue()
subscribers = set()


# 将所有消息分配给所有订阅者
async def dispatcher():
    while True:
        msg = await messages.get()
        for q in subscribers:
            await q.put(msg)


async def publish(msg):
    await messages.put(msg)


# Task that writes chat messages to clients
# 向客户端写入聊天消息的任务
async def outgoing(client_stream):
    # client_stream是 curio.io.SocketStream 类型

    queue = Queue()
    try:
        subscribers.add(queue)
        while True:  # 循环等待写出消息到client TODO
            name, msg = await queue.get()
            await client_stream.write(name + b': ' + msg)
    finally:
        subscribers.discard(queue)


# Task that reads chat messages and publishes them
# 读取聊天消息并发布它们的任务
async def incoming(client_stream, name):
    async for line in client_stream:
        await publish((name, line))


async def chat_handler(client, addr):
    print('Connection from', addr)
    # client 是 curio.io.Socket 类型
    # addr 是 tuple类型  (IPAddress, Port)
    async with client:
        client_stream = client.as_stream()
        await client_stream.write(b'Your name: ')
        name = (await client_stream.readline()).strip()
        await publish((name, b'joined\n'))

        async with TaskGroup(wait=any) as workers:
            await workers.spawn(outgoing, client_stream)
            await workers.spawn(incoming, client_stream, name)

        await publish((name, b'has gone away\n'))

    print('Connection closed')


async def chat_server(host, port):
    async with TaskGroup() as g:
        await g.spawn(dispatcher)
        await g.spawn(tcp_server, host, port, chat_handler)


if __name__ == '__main__':
    run(chat_server('', 25000))

    # > python3 chat_server.py
    # 新窗口1
    # > nc localhost 25000
    # 新窗口2
    # > nc localhost 25000
    # > hello  # 新窗口1执行，新窗口2将看到hello
