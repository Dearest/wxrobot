#! /usr/bin/env python3
#-*- coding:utf-8 -*-
import re
from cook_book import  *
from parse_html_to_img import *
from wxpy import *
from meizitu import *
# 初始化机器人，扫码登陆
bot = Bot(console_qr=1)
schoolmate = bot.groups().search('君子藏器于身待时而动')[0]
boss = bot.friends().search('Dearest')[0]

@bot.register( [schoolmate, boss], TEXT)
def cook_book(msg):
    if re.match(re.compile(r'^#[晚餐|晚饭|菜谱]'), msg.text):
        print(msg.text)
        ParseHtmlToImg.parse(CookBook.random_path()[0])
        msg.reply_image('cook_book.jpg')
    elif re.match(re.compile(r'^#[妹子|美女]'), msg.text):
        print(msg.text)
        path = MeiZiTu.random_pic_path()
        print(path)
        for x in path:
            schoolmate.send_image(x)
    elif re.match(re.compile(r'^#[张杰|杰少]'), msg.text):
        return '傻逼'
    elif re.match(re.compile(r'^#[曾]'), msg.text):
        return '国服第一李索斯'
    elif re.match(re.compile(r'^#[罡]'), msg.text):
        return '国服第一辅助'
    else:
        return
bot.join()