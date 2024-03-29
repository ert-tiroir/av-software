
from devices.abstract import AbstractDevice

from adafruit_dps310.basic import DPS310

class DPS310Device(AbstractDevice):
    def __init__(self, context):
        self.dps = DPS310(context.i2c)
    def is_query(self, query):
        return query == "0x76" or query == "0x77"
    def query(self, query):
        return f"{self.dps.temperature} {self.dps.pressure} {self.dps.altitude}"
        # T|P|H\n