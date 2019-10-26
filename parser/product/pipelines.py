from scrapy.exceptions import DropItem
from es.indices.products import Products


class ProductValidationPipeline(object):
    required_fields = ['sku', 'name', 'offers', 'image', 'url']

    def process_item(self, item, spider):
        self.validate(item)

        return item

    def validate(self, item):
        for field in self.required_fields:
            if field not in item['data'].keys():
                raise DropItem("Not valid item: %s" % item)


class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['data']['sku'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['data']['sku'])
            return item


class ElasticSearchImportPipeline(object):
    def process_item(self, item, spider):
        Products.instance().save(item['data'])
        return item
