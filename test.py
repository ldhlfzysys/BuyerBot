#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *
import re

def handle_msg_text(uid,text):
    if (text == "1"):
        return "台灯：123\n数据线：234"
    elif (text == "2"):
        return "你正在进行的商品有："
    elif (text == "3"):
        return "等待回复截图的商品有："
    elif (text == "4"):
        return "审核通过的商品有："
    elif (text == u"人工"):
        return "请稍等，客服马上与你联系"
    elif (re.match(r'\d+',text)):
        return "纯数字，数据库查询对应商品"
    else:
        return ("使用方式：\n"
        "回复 介绍 查看规则\n"
        "回复 1 获得最新商品列表和商品编号\n"
        "回复 [商品编号] 抢下商品\n"
        "回复 2 查看我正在进行的商品\n"
        "回复 3 查看等待我回复截图的商品\n"
        "回复 4 查看审核通过\n"
        "回复 人工 获取人工帮助\n")
        
def handle_msg_image(uid):
    return "您的截图收到啦，等待审核后立马返现。"

def dispatch_msg(uid,content):
    msgtype = content['type']
    if msgtype == 0:
        return handle_msg_text(uid,content['data'])
    if msgtype == 3:
        return handle_msg_image(uid)
    return None



class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        return_msg = dispatch_msg(msg['user']['id'],msg['content'])
        print ">>>>>>>>回复"
        print return_msg
        if return_msg != None:
            self.send_msg_by_uid(return_msg, msg['user']['id'])
        



'''
    def schedule(self):
        self.send_msg(u'张三', u'测试')
        time.sleep(1)
'''


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
