# -*- coding: utf-8 -*-
#================================================
#糗事百科爬虫
#本程序用于获取糗事百科的每日笑话
#版本：v0.3
#本程序是v0.2的升级版，
#v0.2:主要升级的功能是自动跳转下一页，并自动将笑话下载
#v0.3:主要升级的功能是下载笑话自动保存到/download/year-month-date/文件夹
#================================================

import urllib2
import string
import re
import time
import os

class qiubai_spider:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    def getPage(self, page):
        url = 'http://www.qiushibaike.com/hot/page/' + str(page)

        #htmlheader写入，模拟浏览器登录
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)

        #调用read()方法，将流写入mypage，使用decode()方法，将‘utf－8’编码的页面文件转为’unicode‘
        mypage = response.read()
        unicodepage = mypage.decode('utf-8')

        #使用正则表达式匹配笑话所在的标签。并去掉其他文本
        temp_items = re.findall('<div.*?class="content">(.*?)<!--\d*?-->', unicodepage, re.S)
        items = []
        count = 0

        #将count引入，记录笑话数量。并将<br/>换行标签去除，并且将笑话编号与笑话文本组成list。存入items
        for item in temp_items:
            count += 1
            itemcount = '笑话' + str(count) + '：'
            items.append([itemcount, item.replace("<br/>", "")])
        return items

    def downloadJoke(self):
        while(self.page < 51):
            try:
                jokes = self.getPage(self.page)
            except Exception as e:
                print (e)
            else:
                if(os.path.exists('download') == False):
                    os.mkdir('download')
                os.chdir('download')
                if(os.path.exists(time.strftime("%Y-%m-%d")) == False):
                    os.mkdir(time.strftime("%Y-%m-%d"))
                os.chdir(time.strftime("%Y-%m-%d"))

                file = '笑话' + str(self.page) + ".txt"
                f = open(file, 'w+')
                for item in jokes:
                    f.write(item[0])
                    f.write(item[1].encode('utf-8'))
                f.close()
                os.chdir('..')
                os.chdir('..')
                self.page += 1

    def start(self):
        self.downloadJoke()
        # jokes = self.getPage(page)
        #
        # #建文件
        # file = "笑话" + str(page) + ".txt"
        # f = open(file, 'w+')
        #
        # #写入笑话编号和笑话文本
        # for item in jokes:
        #     f.write(item[0])
        #     f.write(item[1].encode('utf-8'))
        #
        # f.close()


qiubai_instance = qiubai_spider()
qiubai_instance.start()
