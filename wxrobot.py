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

@bot.register(schoolmate, TEXT)
def girl(msg):
    if re.match(re.compile(r'^#[妹美女奶]'), msg.text):
        print(msg.text)
        path = MeiZiTu.random_pic_path()
        print(path)
        for x in path:
            schoolmate.send_image(x)
    else:
        return
bot.join()
