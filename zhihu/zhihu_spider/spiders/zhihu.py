# -*- coding: utf-8 -*-
import scrapy
from zhihu_spider.items import ZhihuSpiderItem


class ZhihuSpider(scrapy.Spider):
    name = "zhihu_spider"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'https://www.zhihu.com/people/wu9_29'
    )

    def parse(self, response):
        for sel in response.xpath('//div[re:test(@class, "zh-profile-activity-page-list")]'):
            item = ZhihuSpiderItem()
            item['time'] = sel.xpath('span/text()').extract()
            item['desc'] = sel.xpath('div[re:test(@class, "zm-profile-section-main zm-profile-activity-main zm-profile-activity-page-item-main")]/a/text()').extract()
            item['link'] = sel.xpath('div[re:test(@class, "zm-profile-section-main zm-profile-activity-main zm-profile-activity-page-item-main")]/a/href').extract()
            yield item
