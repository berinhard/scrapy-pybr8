from scrapy import log
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector


class TalksSpider(BaseSpider):
    name = 'talks'
    allowed_domains = ['2012.pythonbrasil.org.br']
    start_urls = ['http://2012.pythonbrasil.org.br/schedule']

    def parse(self, response):
        talks_urls = self.get_talks_urls(response)
        for talk_url in talks_urls:
            self.log('Retrieved URL: %s' % talk_url, level=log.DEBUG)
        return None

    def get_talks_urls(self, response):
        hxs = HtmlXPathSelector(response)
        for path in hxs.select('//td/a/@href').extract():
            protocol = 'http://'
            domain = self.allowed_domains[0]
            yield protocol + domain + path
