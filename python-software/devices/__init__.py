
from devices.manager import getDeviceManager
from devices.dps310  import DPS310Device

print("Initializing Devices")
getDeviceManager().registerDevice( DPS310Device )
