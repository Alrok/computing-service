from elasticsearch import Elasticsearch


class Client:
    es = None

    def __init__(self):
        self.es = Elasticsearch(['elasticsearch'], scheme="http", port=9200)

    def search(self, index, body):
        result = self.es.search(index=index, body=body)

        items = list()
        for hit in result['hits']['hits']:
            product = hit["_source"]
            product['id'] = hit["_id"]
            items.append(product)

        return items
