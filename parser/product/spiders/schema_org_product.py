import scrapy
from scrapy import Selector
from parser.product.items import ProductItem
import json


class SchemaOrgProductSpider(scrapy.Spider):
    name = 'schema_org_product'
    allowed_domains = []
    start_urls = []

    def __init__(self, allowed_domains, start_urls):
        self.allowed_domains = allowed_domains
        self.start_urls = start_urls

    def parse(self, response):
        scripts = Selector(response).xpath('//script[@type="application/ld+json"]/text()')
        for script in scripts:

            data = json.loads(script.extract())

            if self._is_product(data):
                item = ProductItem()
                item['data'] = data
                yield item

    def _is_product(self, data):
        return data['@context'] == 'http://schema.org/' and data['@type'] == 'Product'
