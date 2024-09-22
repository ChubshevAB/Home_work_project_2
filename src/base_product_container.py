from abc import ABC, abstractmethod


class BaseProductContainer(ABC):

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def products_info(self):
        pass
