# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanMovieItem(scrapy.Item):
    # 排名
    id = scrapy.Field()
    # 电影名称
    name = scrapy.Field()

    pass
    
