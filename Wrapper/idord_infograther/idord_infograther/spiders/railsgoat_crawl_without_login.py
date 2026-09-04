import scrapy

from ..items import HLinkItem


class CrawlRailsGoat(scrapy.Spider):

    name = "railsgoatNotLogin"

    def _get_url(self):
        try:
            with open("link_to_crawl.txt", "r") as handle:
                return handle.readline().strip()
        except OSError:
            return None

    def __init__(self, config_file=None, *args, **kwargs):
        super(CrawlRailsGoat, self).__init__(*args, **kwargs)
        self.start_urls = [f"https://{self._get_url()}"]

    def start_requests(self):
        for url in self.start_urls:
            print(f"____________________{url}____________________________________")
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = HLinkItem()
        form_links = response.css("form::attr(action)")
        post_forms = response.css("form")

        for form in post_forms:
            method = form.css("::attr(method)").extract()
            if method and method[0] == "post":
                item["link"] = form.css("::attr(action)").extract()
                yield item

        for form in form_links:
            link = form.extract()
            if not isinstance(link, list):
                link = [link]
            item["link"] = link
            yield item

        links = response.css("a::attr(href)").extract()
        print(f"_____________________________{links}___________________________________")
        for link in links:
            item["base_link"] = self.start_urls[0]
            item["link"] = link
            item["tag"] = "before_login"
            yield item
