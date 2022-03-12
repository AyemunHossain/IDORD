import scrapy
from ..items import *
from scrapy.http import FormRequest

class SingupRailsGoat(scrapy.Spider):

    name = "signupRailsgoat"

    def __init__(self, start_url= None,config_file = None, *args, **kwargs):                    
        super(SingupRailsGoat, self).__init__(*args, **kwargs)   
        self.start_url = start_url+"/signup"

    
    def start_requests(self):
        
        yield scrapy.Request(url=self.start_url, callback=self.parse)
        

    def parse(self, response, **kwargs):
        form = response.css('form')
        
        if (form !="" or form !=None):
            typ = form.css('form::attr(method)').extract()
            for i in range(len(typ)):
                
                if (str(typ[i]).lower()=="post"):
                    form = response.css('form')
                    items = FormDetailsItem()


                    items['page_link'] =  self.start_url
                    items['link'] = form.css('form::attr(action)').extract()[0]

                    auth =  ['signup','signin','login','create','crate-account']

                    for q in auth:
                        
                        if(q in items['link']):
                            items['is_auth_related'] =True
                            break

                        if(q in self.start_url):
                            items['is_auth_related'] =True
                            break

                        elif (q in str(form)):
                            items['is_auth_related'] =True
                            break

                    items['type'] = 'post'
                    yield items