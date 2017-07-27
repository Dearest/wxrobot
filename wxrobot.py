# 导入模块
from wxpy import *
from cook_book import *
import re
from cook_book import  *
from parse_html_to_img import *
# 初始化机器人，扫码登陆
bot = Bot()
schoolmate = bot.groups().search('君子藏器于身待时而动')[0]
boss = bot.friends().search('Dearest')[0]

@bot.register( boss, TEXT)
def cook_book(msg):
    patten  = re.compile(r'^#[晚餐|晚饭|菜谱]')
    if  patten.match(msg.text):
        print(msg.text)
        path = CookBook.random_path()[0]
        ParseHtmlToImg.parse(path)
        msg.reply_image('cook_book.jpg')
    else:
        return
@bot.register( schoolmate, TEXT)
def group_cook_book(msg):
    patten  = re.compile(r'^#[晚餐|晚饭|菜谱]')
    if  patten.match(msg.text):
        path = CookBook.random_path()[0]
        ParseHtmlToImg.parse(path)
        msg.reply_image('cook_book.jpg')
    else:
        return

embed()