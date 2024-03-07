
from devices.manager import getDeviceManager

from devices.dps310 import DPS310Device

getDeviceManager().registerDevice( DPS310Device )
