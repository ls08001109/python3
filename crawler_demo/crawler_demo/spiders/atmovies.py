# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from crawler_demo.items import CrawlerDemoItem


class ＡtmoviesSpider(scrapy.Spider):
    name = 'atmovies'
    allowed_domains = ['atmovies.com.tw']
    start_urls = ['http://www.atmovies.com.tw']

    def __init__(self, moviesName=None, *args, **moviesNameargs):
        super(ＡtmoviesSpider, self).__init__(*args, **moviesNameargs)
        self.moviesName = moviesName

    def parse(self, response):
        yield FormRequest(
            url="http://search.atmovies.com.tw/search/",
            method="post",
            formdata={
                "fr": "search-page",
                "enc": "UTF-8",
                "type": "all",
                "search_term": self.moviesName,
                "x": "0",
                "y": ""
            },
            callback=self.parse_search_block
            )

    def parse_search_block(self, response):

        search_url = response.xpath('//*[@id="main"]/div[2]/div/section/div/div/div[1]/div/blockquote/header[1]/a/@href').extract()[0]
        search_name = response.xpath('//*[@id="main"]/div[2]/div/section/div/div/div[1]/div/blockquote/header[1]/a/text()').extract()[0]

        yield FormRequest(
            url="http://www.atmovies.com.tw/movie" + search_url.replace("/F", ""),
            method="post",
            formdata={
                "name": search_url,
                "link": search_name
            },
            callback=self.parse_url
            )


    def parse_url(self, response):
        data = CrawlerDemoItem()
        data["moviesName"] = str.strip(response.xpath('//*[@id="main"]/div/div[1]/div/div[2]/text()').extract()[1])
        data["playdate"] = response.xpath('//*[@id="filmTagBlock"]/span[2]/ul/li/text()').extract()[0]
        data["years"] = response.xpath('//*[@id="filmCastDataBlock"]/ul[2]/li[3]/b/text()').extract()[0] + \
                             response.xpath('//*[@id="filmCastDataBlock"]/ul[2]/li[3]/text()').extract()[0]
        data["director"] = response.xpath('//*[@id="filmCastDataBlock"]/ul[1]/li[1]//*/text()').extract()[0] + \
                               str.strip(response.xpath('//*[@id="filmCastDataBlock"]/ul[1]/li[1]//*/text()').extract()[1])
        print("="*100)
        print(data)
        yield data

