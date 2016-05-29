# -*- coding: utf-8 -*-

# author: macwu
# created_data: 2015_5_29
import os
import re
import string
import urllib
import urllib2

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
        while True:
            url = "http://dl.acm.org/results.cfm?query=Cyber%20Physical%20Systems&start="+start+"&filtered=&within=owners.owner%3DHOSTED&dte=&bfr=&srt=_score"
            # 自动翻页
            start_int = string.atoi(start, 10)+10
            start = start_int.__str__()
            print start

            # 预写入头数据，并在头数据中放入cookie
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
            cookie = '_ga=GA1.2.2019075266.1456282750; CFID=388281440; CFTOKEN=76463149; AK=expires=1464518800~access=/10.1145/1650000/1644122/*~md5=0d05082baa1257c5a85c479ed5a17c86'
            headers = { 'User-Agent': user_agent, 'Cookie': cookie, 'Connection': 'keep-alive'}

            # 这里不需要声明为POST方法，在Request中已经用选择定义了，如果有data就是POST方法，没有data就是GET方法
            req = urllib2.Request(url = url, headers=headers)
            resp = urllib2.urlopen(req)

            # 使用正则表达式的预处理，将utf-8转为unicode
            resp_unicode = resp.read().decode('utf-8')

            # 匹配网页里的pdf下载地址，得到所有符合这个形式的列表.*?<div.*?class="author".*?>.*?>(.*?)</a>.*?class="publicationDate".*?>(.*?)</span>
            # 标题，作者，日期，下载地址
            paper_download_list = re.findall('<div.*?class="title".*?>.*?>(.*?)</a>.*?<a.*?name.*?FullText.*?href=(.*?) target=', resp_unicode, re.S)


            # 流的打开
            if paper_download:
                f_download = open(paper_download, 'a+')
            else:
                f_download = open(paper_download, 'w+')

            if paper_details:
                f_detail = open(paper_details, 'a+')
            else:
                f_detail = open(paper_details, 'w+')

            for paper in paper_download_list:
                print paper
                # 论文标题
                paper_title = paper[0].encode('utf-8')
                # 论文作者
                # paper_author = paper[1].encode('utf-8')
                # 论文发表日期
                # paper_publishDate = paper[2].encode('utf-8')
                # 论文地址
                paper_download_path = "http://dl.acm.org/" + paper[1].encode('utf-8').replace('"', '')
                # paper_absolute_name = paper_local_path + paper_title
                try:
                    f_download.write(paper_title + "\n" +paper_download_path + "\n\n")
                    f_download.flush()

                    # f_detail.write("title: " + paper_title + "\n\tauthor:" + paper_author + "\n\tpublishDate:" + paper_publishDate)
                    # f_detail.flush()
                    # urllib.urlretrieve(paper_download_path, paper_absolute_name)
                except Exception, e:
                    continue
            f_download.close()
            # f_detail.close()

    def start(self):
        self.search();

PaperScrap_demo_instance = PaperScrap_demo()
PaperScrap_demo_instance.start()