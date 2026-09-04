import scrapy

from ..items import FormDetailsItem


class SingupRailsGoat(scrapy.Spider):

    name = "signupRailsgoat"

    def __init__(self, start_url=None, config_file=None, *args, **kwargs):
        super(SingupRailsGoat, self).__init__(*args, **kwargs)
        self.start_url = start_url + "/signup"

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response, **kwargs):
        form = response.css("form")
        if not form:
            return

        methods = form.css("form::attr(method)").extract()
        auth_keywords = ["signup", "signin", "login", "create", "crate-account"]

        for method in methods:
            if str(method).lower() != "post":
                continue

            items = FormDetailsItem()
            items["page_link"] = self.start_url
            items["link"] = form.css("form::attr(action)").extract()[0]
            items["type"] = "post"
            items["is_auth_related"] = any(
                keyword in items["link"]
                or keyword in self.start_url
                or keyword in str(form)
                for keyword in auth_keywords
            )
            yield items
