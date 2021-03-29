#!/usr/bin/env bash


# #############################################################################
# File Name   : test.sh
# Author      : DaiDai
# Mail        : daidai4269@aliyun.com
# Created Time: 一  3/29 23:19:08 2021
# #############################################################################


git clone https://github.com/dabeaz/curio
pip3 install curio
cd curio

python3 examples/echoserv.py

# open http://127.0.0.1:25000
nc localhost 25000
