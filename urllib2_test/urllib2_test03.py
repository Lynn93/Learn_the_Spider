import urllib2

url = 'file:///Users/Tong/GitHub/Learn_the_Spider/urllib2_test/baidu.html'
req = urllib2.Request(url)
response = urllib2.urlopen(req)
print response.getcode()
