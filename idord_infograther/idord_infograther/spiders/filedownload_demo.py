
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FiledownloadItem


class NirsoftSpider(CrawlSpider):
    name = 'nirsoft'
    allowed_domains = ['www.nirsoft.net']
    start_urls = ['http://www.nirsoft.net/']
    
    #select specific pipline for a spider
    custom_settings = {'ITEM_PIPELINES': {'idord_infograther.pipelines.FiledownloadPipeline': 300}}
    
    rules = (
        Rule(LinkExtractor(allow=r'utils/'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        file_url = response.css('.downloadline::attr(href)').get()
        file_url = response.urljoin(file_url)
        file_extension = file_url.split('.')[-1]
        if file_extension not in ('zip', 'exe', 'msi'):
            return
        item = FiledownloadItem()
        item['file_urls'] = [file_url]
        item['original_file_name'] = file_url.split('/')[-1]
        yield item