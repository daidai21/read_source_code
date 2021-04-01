#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# #############################################################################
# File Name   : catch_signals.py
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 四  4/ 1 16:46:26 2021
# #############################################################################

import curio
from curio import UniversalEvent
import signal

# Set up signal handling
sigint_evt = UniversalEvent()


def handle_sigint(signo, frame):
    sigint_evt.set()


signal.signal(signal.SIGINT, handle_sigint)


# Wait for a single in Curio code
async def main():
    print("Waiting for a signal")
    await sigint_evt.wait()
    print("Got it!")


if __name__ == '__main__':
    curio.run(main)
