
from devices.manager import getDeviceManager
from devices.dps310  import DPS310Device
from devices.gy521   import GY521Device

getDeviceManager().registerDevice( DPS310Device )
getDeviceManager().registerDevice( GY521Device )
