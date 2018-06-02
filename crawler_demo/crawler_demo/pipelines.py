#coding=utf-8

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import sys

class CrawlerDemoPipeline(object):
    def open_spider(self, spider):
        rows = [
            "moviesName",
            "playdate",
            "years",
            "director"
        ]
        with open("/tmp/data.csv", "w", encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerows([rows])

    def process_item(self, item, spider):
        rows = [
           item['moviesName'],
           item['playdate'],
           item['years'],
           item['director'],
        ]

        print(sys.stdout.encoding)

        with open("/tmp/data.csv", "a", encoding='utf-8') as f:
            w = csv.writer(f)
            w.writerows([rows])

        return item


