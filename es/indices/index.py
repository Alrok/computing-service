from abc import ABC, abstractmethod

from es.client import Client


class Index(ABC):
    client = None

    def __init__(self):
        self.client = Client()

    @abstractmethod
    def get_index_name(self):
        pass

    def search(self, body=''):
        return self.client.search(index=self.get_index_name(), body=body)

    def save(self, doc):
        return self.client.es.index(index=self.get_index_name(), doc_type='_doc', body=doc)

