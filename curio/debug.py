#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : debug.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 17:03:54 2021
# #############################################################################

# #############################################################################
# __init__.py
# #############################################################################
import curio

print(curio.__all__)
print(*curio.__all__)
# #############################################################################
# __main__.py
# #############################################################################
from curio.__main__ import CurioIOInteractiveConsole
print(CurioIOInteractiveConsole(None))

# TODO

# #############################################################################
