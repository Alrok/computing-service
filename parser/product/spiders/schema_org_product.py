import scrapy
from scrapy import Selector
from parser.product.items import ProductItem
import json


class SchemaOrgProductSpider(scrapy.Spider):
    name = 'schema_org_product'
    allowed_domains = []
    start_urls = []
    follow_links = False

    def __init__(self, allowed_domains, start_urls, follow_links=False):
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls
        self.follow_links = follow_links

    def parse(self, response):

        self.logger.info('Parse function called on %s', response.url)

        scripts = Selector(response).xpath('//script[@type="application/ld+json"]/text()')

        for script in scripts:
            data = json.loads(script.extract())

            if self.__is_product(data):
                item = ProductItem()
                item['data'] = data
                yield item

        if self.follow_links:
            for next_page in response.css('a'):
                yield response.follow(next_page, self.parse)

    def __is_product(self, data):
        return data['@context'] == 'http://schema.org' and data['@type'] == 'Product'
