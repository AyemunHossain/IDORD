import scrapy
from ..items import prothomalolink

class CrawlProthomAlo(scrapy.Spider):

    name = "prothomalo"

    def __init__(self, config_file = None, *args, **kwargs):                    
        super(CrawlProthomAlo, self).__init__(*args, **kwargs)   
        self.start_urls = [self.read_file()]

   
    def read_file(self):
        return "http://www.prothomalo.com/"
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response, **kwargs):
        item = prothomalolink()
        all_div = response.css('div')
        
        
        for div in all_div:
            link = div.css('a::attr(href)').extract()
            item['link'] = link
            yield item