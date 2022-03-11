import scrapy
from ..items import LinkItem
from scrapy.http import FormRequest

class SingupRailsGoat(scrapy.Spider):

    name = "signupRailsgoat"

    def __init__(self, config_file = None, *args, **kwargs):                    
        super(SingupRailsGoat, self).__init__(*args, **kwargs)   
        self.start_urls = ["http://0.0.0.0:3000/signup/"]

    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response, **kwargs):
        token = response.css('form input').extract_first()
        print(f"------------{token}---------")
        # return FormRequest.from_response(response,formdata={
        #     'csrf_token':token,
        #     'username':'afasdfsdfddfdsaf',
        #     'password':'asfdffsfsdfsdf',},callback=self.start_crawling_after_login)

    # def start_crawling_after_login(self,response):
    #     items = QuotetItem()
    #     all_div = response.css('div.quote')

    #     for div in all_div:
    #         title = div.css('span.text::text').extract()
    #         author = div.css('.author::text').extract()
    #         tag = div.css('.tag::text').extract()

    #         items['title'] = title
    #         items['author'] = author
    #         items['tag'] = tag
    #         yield items