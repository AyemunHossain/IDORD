import scrapy
from ..items import *

class CrawlRailsGoat(scrapy.Spider):

    name = "railsgoatNotLogin"

    def __init__(self, config_file = None, *args, **kwargs):                    
        super(CrawlRailsGoat, self).__init__(*args, **kwargs)   
        self.start_urls = ["http://0.0.0.0:3000/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response, **kwargs):
        item = HLinkItem()
        all_div = response.css('div')
        
        from_links = response.css('form::attr(action)')
        post_from = response.css('form')

        for form in post_from:
            method = form.css('::attr(method)').extract()
            
            if(method[0]=="post"):
                link = form.css('::attr(action)').extract()
                item['link'] = link
                yield item

        for form in from_links:
            link = form.extract()
            if (type(link)!=type(list())):
                item['link'] = [link]
            yield item

        for div in all_div:
            link = div.css('a::attr(href)').extract()
            item['link'] = link
            
            yield item