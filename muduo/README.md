

### 模块

**日志**

FileUtil

LogFile
AsyncLogging

LogStream
Logging

双缓冲器日志

**定时器**

TimeQueue，Timer,TimerId

### 线程模型


Muduo 的线程模型符合我主张的 one loop per thread + thread pool 模型。每个线程最多有一个 EventLoop。每个 TcpConnection 必须归某个 EventLoop 管理，所有的 IO 会转移到这个线程，换句话说一个 file descriptor 只能由一个线程读写。TcpConnection 所在的线程由其所属的 EventLoop 决定，这样我们可以很方便地把不同的 TCP 连接放到不同的线程去，也可以把一些 TCP 连接放到一个线程里。TcpConnection 和 EventLoop 是线程安全的，可以跨线程调用。TcpServer 直接支持多线程，它有两种模式：

1. 单线程，accept 与 TcpConnection 用同一个线程做 IO。

2. 多线程，accept 与 EventLoop 在同一个线程，另外创建一个 EventLoopThreadPool，新到的连接会按 round-robin 方式分配到线程池中。

### 编译

```sh
➜  git clone https://github.com/chenshuo/muduo
➜  git checkout cpp11
➜  ./build.sh
➜  cd ../../
➜  cd build/release-cpp11 
➜  ls -1
bin  # 可执行文件，包括example
CMakeCache.txt
CMakeFiles
cmake_install.cmake
compile_commands.json
contrib
CTestTestfile.cmake
examples
lib
Makefile
muduo
```


### 链接

* [发布一个基于 Reactor 模式的 C++ 网络库](https://www.cnblogs.com/Solstice/archive/2010/08/29/muduo_net_lib.html)
* [Muduo 源码分析](https://youjiali1995.github.io/network/muduo/)
* [muduo源码剖析 |cyhone](https://zhuanlan.zhihu.com/p/85101271)
* [MyMuduo | 从0到1实现muduo网络库](https://github.com/ouyangmingyu/MyMuduo)
* [muduo 源码剖析](https://www.cyhone.com/articles/analysis-of-muduo/)
* [muduo 代码注释](https://github.com/chenyahui/AnnotatedCode/tree/master/muduo)



===



### QA

* 介绍一下这个项目(几乎是必问的)
* 定时器是怎么实现的？还有什么实现方式？
* 实现一个无锁队列(用原子操作)
* eventfd是什么？有什么好处？
* 双缓冲区异步日志是什么？为什么要这样做？对这个日志系统有没有进行压力测试？
* 什么是优雅关闭连接？(就是read()到0，要透明的传递这个行为而不是直接暴力close())
* epoll的边沿触发和水平触发有什么区别？(epoll的源码并不长，从源码的角度回答比较好)
* epoll为什么高效，相比select和poll
* HTTP报文都有哪些字段？
* 假如服务器要升级，又不想让用户感觉到服务器升级了，该怎么做？(其实就是不间断的提供服务，参考nginx的平滑升级)
* 有没有实现内存池？
* 一个请求到来具体的处理过程是怎样的？
* 线程的唤醒还有哪些方式？
* 怎么检查内存泄漏的？
* 用到了哪些智能指针和RAII机制，几种锁的区别是什么
* 任务队列是怎么实现的，除了加锁还有什么方式？
* 如何解决死锁？
* 怎么进行压测的？
* 为什么要用非阻塞io？
* 为什么要做这个项目？
* Reactor模式是什么？
* 多级缓存日志，宕机日志丢失怎么办？
不会丢失coredump会存储的
