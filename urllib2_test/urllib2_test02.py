import urllib2

req = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(req)
print response
#f = open('baidu.html', 'w+')
#f.write(response.read())
#f.close()
