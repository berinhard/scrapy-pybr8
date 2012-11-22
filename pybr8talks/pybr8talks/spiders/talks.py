from scrapy import log
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from ..items import Pybr8TalksItem


class TalksSpider(BaseSpider):
    name = 'talks'
    allowed_domains = ['2012.pythonbrasil.org.br']
    start_urls = ['http://2012.pythonbrasil.org.br/schedule']

    def parse(self, response):
        talks_urls = self.get_talks_urls(response)
        for talk_url in talks_urls:
            yield Request(talk_url, callback=self.parse_talk)

    def get_talks_urls(self, response):
        hxs = HtmlXPathSelector(response)
        for path in hxs.select('//td/a/@href').extract():
            protocol = 'http://'
            domain = self.allowed_domains[0]
            yield protocol + domain + path

    def parse_talk(self, response):
        hxs = HtmlXPathSelector(response)

        item = Pybr8TalksItem()
        item['title'] = hxs.select('//div[@id="proposal"]/h1/text()').extract()[0]
        item['description'] = hxs.select('//div[@class="twocolumn"]/div[2]/text()[2]').extract()[0]
        item['author_name'] = hxs.select('//div[@class="twocolumn"]/div/div[2]/h3/text()').extract()[0]
        item['author_profile'] = hxs.select('//div[@class="twocolumn"]/div/div[2]/text()[3]').extract()[0]

        return item
