import urllib2

response = urllib2.urlopen('https://www.zhihu.com/people/wu9_29')
print response.read()
