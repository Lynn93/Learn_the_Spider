# -*- coding: utf-8 -*-

# author: macwu
# created_data: 2015_5_29
import os
import re
import string
import urllib
import urllib2
from bs4 import BeautifulSoup

import sys


class PaperScrap_demo:
    def search(self):
        # 下载存放路径：
        if(os.path.exists('download') == False):
            os.mkdir('download')
        os.chdir('download')
        paper_local_path = os.getcwd()+"//"
        # 初始页数
        start = "0"

        # 论文pdf以及详情的存放的路径
        paper_download = paper_local_path + "paper_download_sites.txt"
        paper_details = paper_local_path + "paper_details.txt"
        # 将搜索的数据encode成为url的数据
        # data = {'search': 'Cyber+Physical+Systems'}
        # data_urlencode = urllib.urlencode(data)
        # while True:
        url = "http://dl.acm.org/results.cfm?query=Cyber%20Physical%20Systems&"+start+"&filtered=&within=owners.owner%3DHOSTED&dte=&bfr=&srt=_score"
        # 自动翻页
        start_int = string.atoi(start, 10)+10
        start = start_int.__str__()

        # 预写入头数据，并在头数据中放入cookie
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        cookie = '_ga=GA1.2.2019075266.1456282750; CFID=388281440; CFTOKEN=76463149; AK=expires=1464518800~access=/10.1145/1650000/1644122/*~md5=0d05082baa1257c5a85c479ed5a17c86'
        headers = { 'User-Agent': user_agent, 'Cookie': cookie, 'Connection': 'keep-alive'}

        # 这里不需要声明为POST方法，在Request中已经用选择定义了，如果有data就是POST方法，没有data就是GET方法
        req = urllib2.Request(url = url, headers=headers)
        resp = urllib2.urlopen(req)

        paper_page = resp.read()
        file = "dl_ieee.html"
        f = open(file)
        f.write(paper_page)
        f.flush()
        f.close()

        soup = BeautifulSoup(paper_page, 'html.parser')
        details = soup.find_all('div', attrs={"class":"details"})
        for d in details:
            print d


    def start(self):
        self.search();

PaperScrap_demo_instance = PaperScrap_demo()
PaperScrap_demo_instance.start()