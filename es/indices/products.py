from es.indices.index import Index


class Products(Index):

    @staticmethod
    def instance():
        return Products()

    def get_index_name(self):
        return 'products'

