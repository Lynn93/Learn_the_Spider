# -*- coding: utf-8 -*-
import urllib2
import string

########################################################################
#分析百度贴吧帖子的url，发现http://tieba.baidu.com/p/4191938120?pn=1
#pn后面的数字代表页面数，前面的url不变
########################################################################

#函数baidu_teiba（）输入starturl为起始页面，输入begin，为第一页，输入end为终止页
#将每个页面保存为html文件
def baidu_tieba(starturl, begin, end):
    for i in range(begin, end+1):
        pagename = string.zfill(i, 5) + '.html'
        print "正在将第" + str(i) + "页面" + "保存为：" + pagename
        f = open(pagename, 'w+')
        f.write(urllib2.urlopen(starturl + pagename).read())
        f.close()

starturl = str(raw_input(u'please input pageurl\n'))
begin = int(raw_input(u"please input beginnum\n"))
end = int(raw_input(u"please input endnum\n"))

print baidu_tieba(starturl, begin, end)
