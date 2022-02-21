from scrapy_proxy_pool.policy import BanDetectionPolicy

class BanDetectionPolicyNotText(BanDetectionPolicy):

    def response_is_ban(self, request, response):
        # if self.BANNED_PATTERN.search(response.text): <-this line caused error
        #    return True

        if response.status not in self.NOT_BAN_STATUSES:
            return True
        if response.status == 200 and not len(response.body):
            return True