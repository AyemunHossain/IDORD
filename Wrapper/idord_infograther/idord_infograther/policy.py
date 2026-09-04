from scrapy_proxy_pool.policy import BanDetectionPolicy


class BanDetectionPolicyNotText(BanDetectionPolicy):

    def response_is_ban(self, request, response):
        # The default policy inspects ``response.text``; some responses have
        # no decodable text body, so we only look at status and body length.
        if response.status not in self.NOT_BAN_STATUSES:
            return True
        if response.status == 200 and not len(response.body):
            return True
        return False
