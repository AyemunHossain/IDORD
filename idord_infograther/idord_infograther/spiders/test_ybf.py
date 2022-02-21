
import scrapy



#test spider is working fine or not 
class testybf(scrapy.Spider):

    name = "testybf"

    start_urls = ["http://www.ybfbd.info/"]

    def parse(self, response, **kwargs):
        
        all_link = response.css('a::attr(href)')
        
        for link in all_link:
            print("-----------------------------------------------------------------")
            print(link)
            print("-----------------------------------------------------------------")
