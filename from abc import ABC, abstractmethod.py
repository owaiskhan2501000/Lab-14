from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

class FileStorage(ABC):
    @abstractmethod
    def save(self, data):
        pass

class DataManager(DatabaseConnection, FileStorage):
    def process_data(self, data):
        self.connect()
        self.save(data)
