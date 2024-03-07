
from devices.context import DeviceContext

__DEVICE_MANAGER__ = None

class DeviceManager:
    def __init__(self):
        if hasattr(self, "context"): return

        self.context = DeviceContext()

        self.devices = []
    def __new__(clz, *args, **kwargs):
        global __DEVICE_MANAGER__

        if __DEVICE_MANAGER__ != None:
            return __DEVICE_MANAGER__

        __DEVICE_MANAGER__ = super(DeviceManager, clz).__new__(clz, *args, **kwargs)
        return __DEVICE_MANAGER__
    
    def registerDevice (self, clazz):
        self.devices.append(clazz(self.context))
    def query (self, query):
        for device in self.devices:
            if device.is_query(query):
                return device.query(query)
        return None

def getDeviceManager ():
    return DeviceManager()
