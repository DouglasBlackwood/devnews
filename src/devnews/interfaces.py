from abc import ABC, abstractmethod


class NewsRepository(ABC):
    @abstractmethod
    def get_all(self):
        pass
