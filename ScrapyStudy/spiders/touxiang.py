# -*- coding: utf-8 -*-
import scrapy
from ScrapyStudy.items import ScrapystudyItem


class TouxiangSpider(scrapy.Spider):
    name = 'touxiang'
    allowed_domains = ['woyaogexing.com']
    start_urls = ['https://www.woyaogexing.com/touxiang/']
    # default_headers = {
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #     'Accept-Encoding': 'gzip, deflate, sdch, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    #     'Cache-Control': 'max-age=0',
    #     'Connection': 'keep-alive',
    #     'Host': 'www.douban.com',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    # }

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, headers=self.default_headers, callback=self.parse)

    def parse(self, response):
        # //img[@class='lazy']/@src
        imglinks = response.xpath("//img[@class='lazy']/@src").extract()
        item = ScrapystudyItem()
        for il in imglinks:
            item['imglink'] = "http:" + il
            yield item
        # print(response.body)
        next_page = response.xpath(u"//a[text()='下一页']/@href").extract()
        if len(next_page) > 0:
            url = "https://www.woyaogexing.com" + next_page[0]
            yield scrapy.Request(url, callback=self.parse)



