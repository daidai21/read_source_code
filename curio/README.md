# [curio](https://github.com/dabeaz/curio)

commit-id `78bca8a`

### Doc

##### A Tutorial Introduction

* 任务和并发： hello.py hello1.py hello2.py
* 任务组： hello3.py
* 耗时操作： fib.py
* 回声服务器： echo_server.py
* 任务间通讯： inter_task_comm.py
* 聊天服务器： chat_server.py

##### How to

* TCP server: echo_server.py echo_stream_server.py
* UDP Server: echo_udp_server.py
* outgoing connection: outgoing_connection.py ssl_outgoing_connection.py
* [ ] SSL-enabled server: ssl_enabled_server.py
* tasks communicate: tasks_communicate.py
* a task and a thread communicate: a_task_and_a_thread_communicate.py
* catch signals: catch_signals.py
* two different Python interpreters send messages to each other: producer.py consumer.py

### Project

##### Catalog tree

```sh
>>> tree curio/curio 
curio/curio
├── __init__.py     # 定义对外的接口
├── __main__.py     # 提供的调试工具 `python3 -m curio` 进入
├── channel.py      #
├── debug.py        # 任务debug工具
├── errors.py       # 定义错误类型
├── file.py         # 
├── io.py           # 
├── kernel.py       # 
├── meta.py         # 
├── monitor.py      # 
├── network.py      # 
├── queue.py        # 
├── sched.py        # 
├── socket.py       # 
├── ssl.py          # 内置SSL模块的包装器
├── subprocess.py   # 
├── sync.py         # 
├── task.py         # 
├── thread.py       # 
├── time.py         # 
├── timequeue.py    # 
├── traps.py        # 
└── workers.py      # 

0 directories, 23 files


>>> find curio | grep ".py$" | xargs wc -l
     384 curio/queue.py
     347 curio/sync.py
     195 curio/time.py
     697 curio/task.py
     264 curio/thread.py
     316 curio/monitor.py
     856 curio/kernel.py
     171 curio/subprocess.py
     281 curio/channel.py
     637 curio/io.py
      28 curio/__init__.py
     110 curio/timequeue.py
     133 curio/traps.py
     190 curio/file.py
     110 curio/debug.py
     125 curio/sched.py
     170 curio/network.py
      90 curio/errors.py
     482 curio/workers.py
      77 curio/ssl.py
     101 curio/socket.py
     119 curio/__main__.py
     236 curio/meta.py
    6119 total
```

### 解析

* `__init__.py`
* [ ] `__main__.py`
* [ ] `channel.py`
* [ ] `debug.py`
* [ ] `errors.py`
* [ ] `file.py`
* [ ] `io.py`
* [ ] `kernel.py`
* [ ] `meta.py`
* [ ] `monitor.py`
* [ ] `network.py`
* [ ] `queue.py`
* [ ] `sched.py`
* [ ] `socket.py`
* [ ] `ssl.py`
* [ ] `subprocess.py`
* [ ] `sync.py`
* [ ] `task.py`
* [ ] `thread.py`
* [ ] `time.py`
* [ ] `timequeue.py`
* [ ] `traps.py`
* [ ] `workers.py`

### link

* https://curio.readthedocs.io/en/latest/
