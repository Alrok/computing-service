from es.client import Client
from es.indices.index import Index


class Products(Index):

    @staticmethod
    def instance():
        return Products()

    def get_index_name(self):
        return 'products'

    def search(self, body=''):
        client = Client()
        return client.search(index=self.get_index_name(), body=body)
