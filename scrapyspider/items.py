# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#class ScrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 #   pass

class DoubanItem(scrapy.Item):
    ranking = scrapy.Field()
    movie_name=scrapy.Field()
    score=scrapy.Field()
    score_num=scrapy.Field()
