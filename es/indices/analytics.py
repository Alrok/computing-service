import json

from es.client import Client
from es.indices.index import Index


class Analytics(Index):

    @staticmethod
    def instance():
        return Analytics()

    @staticmethod
    def get_mapping():
        return json.dumps({
            'mappings': {
                '_doc': {
                    'properties': {
                        'event': {
                            'properties': {
                                'name': {'type': 'keyword'}
                            }
                        }
                    }
                }
            }
        })

    def get_index_name(self):
        return 'analytics'
