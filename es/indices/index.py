from abc import ABC, abstractmethod


class Index(ABC):
    @abstractmethod
    def get_index_name(self):
        pass
