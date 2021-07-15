from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import subprocess
import requests
import psutil 
import re
import os


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

@run_async
def img(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)
    # cpu_usage = psutil.cpu_percent(1)
    # total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    # ram_usage = round((used_memory/total_memory) * 100, 2)
    # disk_used = psutil.disk_usage('/')
    # msg = f"Your CPU: {cpu_usage}% \nYour RAM: {ram_usage}%\nYour Disk: {disk_used[3]}%"
    #context.bot.send_message(chat_id=chat_id, text=msg)

def in4(update, context):
    chat_id = update.message.chat_id
    cpu_usage = psutil.cpu_percent(1)
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    ram_usage = round((used_memory/total_memory) * 100, 2)
    disk_used = psutil.disk_usage('/')
    msg = f"Your CPU: {cpu_usage}% \nYour RAM: {ram_usage}%\nYour Disk: {disk_used[3]}%"
    context.bot.send_message(chat_id=chat_id, text=msg)

def main():
    updater = Updater('1844276050:AAENeCJku8ROK_yz-EDd1HqPeQe9N9J1S4I', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('img',img))
    dp.add_handler(CommandHandler('in4',in4))
    updater.start_polling()
    updater.idle()

    # cmd = 'vnstat -i "enp3s0" -tr 3 | grep rx'
    # #os.system(cmd)
    # x = os.popen(cmd).read()
    # result = re.search(r'([0-9.]{1,} kbit/s).+?([0-9]{1,} packets/s)', x, re.S)
    # print (x)
    # print(result.group(0))
    # print(result.group(1))
    # print(result.group(2))
    # ifconfig = subprocess.check_output(['ifconfig'])

#   Output: enp3s0: inet: 192.168.1.105 mask: 255.255.255.0 inet6: fe80::2fb4:cdf7:55d9:c781

#thêm command (function): tạo 1 def cmd(update, context) rồi add thêm dp.add_handler(CommandHandler('cmd',def_cmd)) trong main
#pip install python-telegram-bot --upgrade

if __name__ == '__main__':
    main()