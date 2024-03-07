
import board

class DeviceContext:
    def __init__(self):
        self.i2c = board.I2C()
