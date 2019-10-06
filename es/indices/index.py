from abc import ABC, abstractmethod

from es.client import Client


class Index(ABC):
    @abstractmethod
    def get_index_name(self):
        pass

    def search(self, body=''):
        client = Client()
        return client.search(index=self.get_index_name(), body=body)
