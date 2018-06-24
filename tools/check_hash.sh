#!/bin/bash


cd ../tmp/
if [[ ! -d crystal-book ]];then
	git clone https://github.com/crystal-lang/crystal-book.git
fi

cd crystal-book
git pull
cd ..


../tools/check_hash.py ./crystal-book ../src/
