# -*- coding: utf-8 -*-

# author: macwu
# created_data: 2015_5_29


import urllib
import urllib2

class PaperScrap_demo:
    def search(self):
        # 将搜索的数据encode成为url的数据
        data = {'search': 'Cyber+Physical+Systems'}
        data_urlencode = urllib.urlencode(data)
        url = "http://jacm.acm.org/search-acm.cfm"

        # 预写入头数据，并在头数据中放入cookie
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        cookie = '_ga=GA1.2.2019075266.1456282750; CFID=388281440; CFTOKEN=76463149; AK=expires%3D1464499444%7Eaccess%3D%2F10%2E1145%2F1800000%2F1795205%2F%2A%7Emd5%3D113fa03f910924d93635e84a77b3c713'
        headers = { 'User-Agent': user_agent, 'Cookie': cookie, 'Connection': 'keep-alive'}

        # 这里不需要声明为POST方法，在Request中已经用选择定义了，如果有data就是POST方法，没有data就是GET方法
        req = urllib2.Request(url = url, headers=headers, data = data_urlencode)
        resp = urllib2.urlopen(req)
        file = "jacm.html"
        f = open(file, 'w+')
        f.write(resp.read())

    def start(self):
        self.search();

PaperScrap_demo_instance = PaperScrap_demo()
PaperScrap_demo_instance.start()