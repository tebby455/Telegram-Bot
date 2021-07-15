from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
from bs4 import BeautifulSoup as soup
from random import randint
import requests
import psutil
import re
import os

TOKEN = '1844276050:AAENeCJku8ROK_yz-EDd1HqPeQe9N9J1S4I'

# ======================================== Process ======================================== #
def in4(update, context):
    chat_id = update.message.chat_id
    cpu_usage = psutil.cpu_percent(1)
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    ram_usage = round((used_memory/total_memory) * 100, 2)
    disk_used = psutil.disk_usage('/')
    msg = f"Your CPU: {cpu_usage}% \nYour RAM: {ram_usage}%\nYour Disk: {disk_used[3]}%"
    context.bot.send_message(chat_id=chat_id, text=msg)
# ======================================== Image, Gif ======================================== #
# ========= Huy Parsing ========= #
# IDK what to do in here, so I put independent
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

@run_async
def img(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

# =========== Global =========== #
def cat(update, context):
    chat_id = update.message.chat_id
    context.bot.send_animation(chat_id=chat_id, animation='https://cataas.com/cat')

def namngu(update, context):
    chat_id = update.message.chat_id
    list_img = ['https://scontent-xsp1-1.xx.fbcdn.net/v/t1.18169-9/19642274_770462263125727_2592695734119120343_n.jpg?_nc_cat=103&ccb=1-3&_nc_sid=174925&_nc_ohc=ng94ayoHR_8AX9uUB0v&_nc_ht=scontent-xsp1-1.xx&oh=5ca34b1b1fd0bad2463d939f31293266&oe=60F433A0',
                'https://scontent-xsp1-3.xx.fbcdn.net/v/t1.6435-9/43016054_1040098609495423_8260332874650091520_n.jpg?_nc_cat=107&ccb=1-3&_nc_sid=174925&_nc_ohc=V6iNtkG0c90AX9osKh3&_nc_ht=scontent-xsp1-3.xx&oh=21ca4e948ceac79732b4b620ddbf9367&oe=60F4F6FE',
                'https://scontent-xsp1-2.xx.fbcdn.net/v/t1.6435-9/72456365_1333998910105390_1675020825780027392_n.jpg?_nc_cat=106&ccb=1-3&_nc_sid=730e14&_nc_ohc=OlXo9F9y9TIAX8_nrau&tn=4dtmWZBiw0LmDSH2&_nc_ht=scontent-xsp1-2.xx&oh=d29dbb49355cd45f1fb9332e8d19d4e9&oe=60F57B4C',
                'https://scontent-xsp1-2.xx.fbcdn.net/v/t1.6435-9/168839743_3108952812723625_4535858662046465976_n.jpg?_nc_cat=104&ccb=1-3&_nc_sid=0debeb&_nc_ohc=7BrdDHtivK4AX_A3MDg&_nc_ht=scontent-xsp1-2.xx&oh=3c461c4eebebc7118444cd15b480c01b&oe=60F42960'] # Đây là tứng (Night Barron)
    context.bot.send_photo(chat_id=chat_id, photo=list_img[randint(0, len(list_img)-1)])

def girl(update, context):
    URL = ['https://www.pinterest.com/lockuteni/list-g%C3%A1i-%C4%91%E1%BA%B9p/',
           'https://weheartit.com/aluuna/collections/100812115-girls-random-pictures-profilpictures?page=4&before=286671742']
    link_img = []
    html = requests.get(URL[randint(0, len(URL)-1)]).text
    # print(html)
    soup_parser = soup(html, 'html.parser')
    list_img = soup_parser.findAll('img')
    for img in list_img:
        img = img.get('src')
        if 'whicdn' in img and 'jpg' in img and 'superthumb' in img:
            link_img.append(img)
        elif 'pinimg' in img:
            link_img.append(img)
    send_img_link = link_img[randint(0, len(link_img)-1)]
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=send_img_link)
# ======================================== Main ======================================== #
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('img', img))
    dp.add_handler(CommandHandler('in4', in4))
    dp.add_handler(CommandHandler('cat', cat))
    dp.add_handler(CommandHandler('girl', girl))
    dp.add_handler(CommandHandler('namngu', namngu))
    updater.start_polling()
    updater.idle()

#pip install python-telegram-bot --upgrade

if __name__ == '__main__':
    main()
