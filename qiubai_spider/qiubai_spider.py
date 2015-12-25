# -*- coding: utf-8 -*-
#================================================
#
#本程序用于获取糗事百科的每日笑话
#v0.1
#
#================================================

import urllib2
import string
import re

class qiubai_spider:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def getPage(self, page):
        url = 'http://www.qiushibaike.com/hot/page/' + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)
        mypage = response.read()
        unicodepage = mypage.decode('utf-8')

        temp_items = re.findall('<div.*?class="content">(.*?)<!--\d*?-->', unicodepage, re.S)
        items = []
        count = 0
        for item in temp_items:
            count += 1
            itempage = '笑话' + str(count) + '：'
            items.append([itempage, item.replace("<br\>", "")])
        return items

    def start(self, page):
        jokes = self.getPage(page)
        file = "笑话.txt"
        f = open(file, 'w+')

        for item in jokes:
            f.write(item[0])
            f.write(item[1].encode('utf-8'))

        f.close()

qiubai_instance = qiubai_spider()
qiubai_instance.start(1)
