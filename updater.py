#! /usr/bin/env python3
import sys
import os

bot_script = 'telegram-bot.py'
os.system(f'curl https://raw.githubusercontent.com/tebby455/Telegram-Bot/main/{bot_script} > {bot_script}')
sys.exit(os.system(f'python3 {bot_script}'))