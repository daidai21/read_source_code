* 内部数据结构
    * `sds.h`  string类型
    * `adlist.h`  双向队列
* 内存映射数据结构
* 数据类型
* 功能的实现
* 内部运作机制

===

**Source Code Catalog**

```md
src
├── Makefile
├── Makefile.dep
├── adlist.c
├── adlist.h        双向队列
├── ae.c
├── ae.h
├── ae_epoll.c
├── ae_evport.c
├── ae_kqueue.c
├── ae_select.c
├── anet.c
├── anet.h
├── aof.c
├── asciilogo.h
├── bio.c
├── bio.h
├── bitops.c
├── blocked.c
├── cluster.c
├── cluster.h
├── config.c
├── config.h
├── crc16.c
├── crc64.c
├── crc64.h
├── db.c
├── debug.c
├── dict.c
├── dict.h
├── endianconv.c
├── endianconv.h
├── fmacros.h
├── help.h
├── hyperloglog.c
├── intset.c
├── intset.h
├── lzf.h
├── lzfP.h
├── lzf_c.c
├── lzf_d.c
├── memtest.c
├── mkreleasehdr.sh
├── multi.c
├── networking.c
├── notify.c
├── object.c
├── pqsort.c
├── pqsort.h
├── pubsub.c
├── rand.c
├── rand.h
├── rdb.c
├── rdb.h
├── redis-benchmark.c
├── redis-check-aof.c
├── redis-check-dump.c
├── redis-cli.c
├── redis-trib.rb
├── redis.c
├── redis.h
├── redisassert.h
├── release.c
├── replication.c
├── rio.c
├── rio.h
├── scripting.c
├── sds.c
├── sds.h       string类型
├── sentinel.c
├── setproctitle.c
├── sha1.c
├── sha1.h
├── slowlog.c
├── slowlog.h
├── solarisfixes.h
├── sort.c
├── syncio.c
├── t_hash.c
├── t_list.c
├── t_set.c
├── t_string.c
├── t_zset.c
├── testhelp.h
├── util.c
├── util.h
├── valgrind.sup
├── version.h
├── ziplist.c
├── ziplist.h
├── zipmap.c
├── zipmap.h
├── zmalloc.c
└── zmalloc.h
```

===

**Links**

* [Redis 设计与实现（第一版）](https://redisbook.readthedocs.io/en/latest/index.html)
* [如何高效深入的阅读Redis的源码？](https://www.zhihu.com/question/28677076)
* [redis源码解析](https://redissrc.readthedocs.io/en/latest/)
* [huangz1990/redis-3.0-annotated](https://github.com/huangz1990/redis-3.0-annotated)
