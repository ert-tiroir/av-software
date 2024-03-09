
from devices.abstract import AbstractDevice

import adafruit_mpu6050

class GY521Device(AbstractDevice):
    def __init__(self, context):
        self.dps = adafruit_mpu6050.MPU6050(context.i2c)
    def is_query(self, query):
        return query == "0x68"
    def query(self, query):
        return f"Received MPU6050"
        # T|P|H\n
