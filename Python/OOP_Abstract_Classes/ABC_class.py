from abc import ABC, abstractmethod
from typing import Protocol


class APICaller(ABC):

    # this will force to create this method on child class
    @abstractmethod
    def connect_API(self):
        pass

    @abstractmethod
    def get_request(self):
        pass


class APICallerProtocol(Protocol):

    # this will force to create this method on child class
    def connect_API(self):
        ...

    def get_request(self):
        ...


class APIAmazon(APICaller):
    def connect_API(self):
        print("connected to API")

    def get_request(self):
        print('request done')


class APIAmazonProtocol(APICaller):
    pass


temp_test = APIAmazon()
temp_test.connect_API()
temp_test.get_request()
# temp_test = APIAmazonProtocol()

print(temp_test)
