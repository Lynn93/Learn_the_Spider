import scrapy
import urllib2

from bs4 import BeautifulSoup
from PengPaiNews.items import PengpainewsItem

class DmozSpider(scrapy.Spider):
    name = "PengPai"
    allowed_domains = ["thepaper.cn"]
    start_urls = [
        "http://www.thepaper.cn"
    ]

    def parse(self, response):
        news_li = response.xpath('//div[class="news_li"]')
        for sel in news_li:
            item = PengpainewsItem()
            item['title'] = sel.xpath('h2/a/text()').extract()
            item['link'] = sel.xpath('h2/a/@href').extract()
            item['desc'] = sel.xpath('p/text()').extract()
            yield item