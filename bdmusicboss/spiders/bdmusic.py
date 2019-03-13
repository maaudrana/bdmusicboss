# -*- coding: utf-8 -*-
import scrapy


class BdmusicSpider(scrapy.Spider):
    name = 'bdmusic'
    allowed_domains = ['bdmusicboss.mobi']
    start_urls = ['http://bdmusicboss.mobi/page/%s' % page for page in range(1,30)]
    #going to the pagination
    def parse(self, response):
        post = response.xpath('//*[@class="post-box-title"]/a/@href').extract()
        for i in post:
            yield scrapy.Request(i,callback=self.parse1)
     #collecting information
    def parse1(self,response):
        videoLink = response.xpath('//*[@class="su-button su-button-style-stroked"]/@href').extract_first()
        videoname = response.xpath('//*[@itemprop="name"]/text()').extract_first()
        yield{'Name':videoname,
        "video":videoLink}
