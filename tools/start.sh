#!/bin/bash
# Author: Turing Zhu
# Date: 2018-06-20 15:22:00
# Desc: start mdbook with port 3002 backend

cd ../

ps -ef|grep -vE "grep -E mdbook serve -p 3002 -w 3003" | grep -E "mdbook serve -p 3002 -w 3003" >/dev/null
[[ $? -eq 0 ]] && exit 0
mdbook serve -p 3002 -w 3003 >log/serve.log 2>log/serve.err &
