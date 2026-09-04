# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from core.models import LinkItem
from core.models import FormDetailsItem as FormDetailsModel


class HLinkItem(DjangoItem):
    django_model = LinkItem


class FormDetailsItem(DjangoItem):
    django_model = FormDetailsModel


class FiledownloadItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    original_file_name = scrapy.Field()
