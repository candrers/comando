#!/usr/bin/python3
# -*- coding: utf-8 -*-


import subprocess

subprocess.run(["cd", "/home/carlos/comando/controle/chat/"])

processo = subprocess.Popen('python3 client.py', shell=True)
