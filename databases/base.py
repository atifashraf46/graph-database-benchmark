from abc import ABC, abstractmethod


class BaseDatabase(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute(self, query, parameters=None):
        pass

    @abstractmethod
    def execute_write(self, query, parameters=None):
        pass