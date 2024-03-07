
from devices.abstract import AbstractDevice

class DPS310(AbstractDevice):
    def is_query(self, query):
        return query[0] == 0x76 or query[0] == 0x77
    def query(self, query):
        return "21.79 1014 200m"