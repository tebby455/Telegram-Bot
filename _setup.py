#! /usr/bin/python3
import time
import os
app = ['python-telegram-bot', 'bs4', 'requests', 'psutil', 'PyCryptodome']
print('[+] Setting up...')
time.sleep(0.5)
for name in app:
    os.system(f'pip install {name}')
