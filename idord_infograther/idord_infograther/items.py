# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IdordInfogratherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class prothomalolink(scrapy.Item):
    link = scrapy.Field()
    


class FiledownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field
    original_file_name = scrapy.Field()
