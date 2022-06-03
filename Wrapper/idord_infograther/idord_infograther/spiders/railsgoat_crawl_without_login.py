import scrapy
from ..items import *

class CrawlRailsGoat(scrapy.Spider):

    name = "railsgoatNotLogin"

    
    def _get_url(self):
        file= open("link_to_crawl.txt","r")
        try:
            return file.readline()
        except:
            return None

    def __init__(self, config_file = None, *args, **kwargs):                    
        super(CrawlRailsGoat, self).__init__(*args, **kwargs)  
        self.start_urls = [f"https://{self._get_url()}"]

    def start_requests(self):
        for url in self.start_urls:
            print(f"____________________{url}____________________________________")
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


        links = response.css('a::attr(href)').extract()
        print(f"_____________________________{links}___________________________________")
        for link in links:
            item['base_link'] = self.start_urls[0]
            item['link'] = link
            item['tag'] = 'before_login'
            yield item
        
