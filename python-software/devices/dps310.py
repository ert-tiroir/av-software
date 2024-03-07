
from devices.abstract import AbstractDevice

from adafruit_dps310.basic import DPS310

class DPS310Device(AbstractDevice):
    def __init__(self, context, key = 0x76):
        self.dps = DPS310(context.i2c, key)
    def is_query(self, query):
        return query[0] == 0x76 or query[0] == 0x77
    def query(self, query):
        return f"{self.dps.temperature}|{self.dps.pressure}|{self.dps.altitude}"
    