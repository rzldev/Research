# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

## Scraped data -> Item containers -> json/csv files
## Scraped data -> Item containers -> Pipelines -> SQL/Mongo Database

## To activate pipelines uncoment the ITEM_PIPELINES code in setting.py (line 67, 68, 69)

class ScrapykompasPipeline(object):
    def process_item(self, item, spider):
        print("pipeline : " + item['title'][0] + ' ' + item['tag'][0] + ' ' + item['link'][0])
        return item
