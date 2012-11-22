from scrapy.spider import BaseSpider

class TalksSpider(BaseSpider):
    name = 'talks'
    allowed_domains = ['2012.pythonbrasil.org.br']
    start_urls = ['http://2012.pythonbrasil.org.br/schedule']

    def parse(self, response):
        pass
