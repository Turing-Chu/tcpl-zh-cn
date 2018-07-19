#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
Author: Turing<qishiwenjun@163.com>
Date: 2018-06-23 16:59
Desc: rust学的不咋样 还是用python吧

"""

import os.path
import subprocess
import logging
import sys
import git

# Logger init ############################################################
# create logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
# logger_handler = logging.FileHandler(r'./app.log', 'w')
logger_handler = logging.StreamHandler(stream=sys.stdout)
logger_handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(lineno)d] %(message)s', ' %Y-%m-%d %H:%M:%S')
logger_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(logger_handler)


def get_original_hash(path=""):

    result = {}
    if not os.path.exists(path):
        logger.error('no such file or directory: {}'.format(path))
        sys.exit(1)
    old_path = os.path.abspath(os.curdir)
    os.chdir(path)

    # TODO check if the path is a git repository or not
    g = git.Git()
    for f in g.ls_files().split():
        if not f.endswith(".md"):
            continue
        p = subprocess.Popen("git log -1 {}".format(f), encoding='utf8', shell=True, stdout=subprocess.PIPE)
        stdout = p.stdout.readlines()
        if 0 == len(stdout):
            continue
        result[f] = {
            'file': f,
            'commit_hash': stdout[0].replace('commit', '').strip(),
            'author': stdout[1].replace('Author:', '').strip(),
            'date': stdout[2].replace('Date:', '').strip(),
            'message': stdout[4].strip(),
        }
    os.chdir(old_path)
    return result


def get_tpl_hash(path=""):
    result = {}
    print(os.path.abspath(os.curdir))
    if not os.path.exists(path):
        logger.error('no such file or directory: {}'.format(path))
        sys.exit(1)

    old_path = os.path.abspath(os.curdir)
    os.chdir(path)

    # TODO check if the path is a git repository or not
    g = git.Git()
    for f in g.ls_files().split():
        if not f.endswith(".md"):
            continue

        p = subprocess.Popen("cat %s | grep -oE 'commit [0-9a-z]{40}'" % f,
                             encoding='utf8', shell=True, stdout=subprocess.PIPE)
        stdout = p.stdout.readlines()
        if 0 == len(stdout):
            continue
        result[f] = {
            'file': f,
            'commit_hash': stdout[0].replace('commit', '').strip(),
        }
    os.chdir(old_path)

    return result


if __name__ == '__main__':

    if sys.argv.__len__() < 3:
        logger.error('missing parameters')
        sys.exit(2)
    original_hash = get_original_hash(sys.argv[1])
    tpl_hash = get_tpl_hash(sys.argv[2])

    all_equal = True
    ignore_file = ['SUMMARY.md', "README.md"]
    for f in original_hash.keys():
        if f in ignore_file:
            continue
        if f not in tpl_hash.keys():
            logger.warning('no such file in tpl: {}, or no commit hash in this file'.format(f))
            continue
        if original_hash[f]['commit_hash'] != tpl_hash[f]['commit_hash']:
            logger.warning("{}: {} - {}".format(f, original_hash[f]['commit_hash'], tpl_hash[f]['commit_hash']))
    print("total: {}".format(len(original_hash.keys())))
