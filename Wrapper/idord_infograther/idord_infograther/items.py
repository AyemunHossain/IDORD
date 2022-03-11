# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from core.models import LinkItem

class HLinkItem(DjangoItem):
    django_model = LinkItem


class FiledownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field
    original_file_name = scrapy.Field()
