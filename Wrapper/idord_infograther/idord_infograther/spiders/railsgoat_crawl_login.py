import scrapy
from ..items import *
from scrapy.http import FormRequest
import os

class CrawlRailsGoat(scrapy.Spider):
    
    name = "railsgoatLogin"

    def _get_url(self):
        file= open("link_to_crawl.txt","r")
        try:
            return file.readline()
        except:
            return None
        
    def __init__(self, config_file = None, *args, **kwargs):                    
        super(CrawlRailsGoat, self).__init__(*args, **kwargs)   
        self.start_urls = [f"http://{self._get_url()}"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    
    def parse(self, response, **kwargs):
        inputs = response.css('form input')
        for inp in inputs:
            try:
                input_name = inp.css('input::attr(name)').extract()[0]
            except:
                input_name = inp.css('input::attr(name)').extract()

            if('token' in input_name or 'csrf' in input_name):
                token = inp.css("input::attr(value)").extract()
                if (token  and type(token)!=str):
                    
                    return FormRequest(url=f"{self.start_urls[0]}/sessions/",formdata={
                        input_name:token[0],
                        'email':'a@a.com',
                        'password':'ashikashik',},callback=self.start_crawling_after_login)

    def start_crawling_after_login(self,response):
        
        print("_----------------------------------------------______")
        item = HLinkItem()
        links_after_login = response.css('a::attr(href)').extract()
        for link in links_after_login:
            item['base_link'] = self.start_urls[0]
            item['link'] = link
            item['tag'] = 'after_login'
            yield item