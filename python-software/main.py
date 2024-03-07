
from devices import getDeviceManager

manager = getDeviceManager()

def main ():
    while True:
        line = input()

        value = manager.query(line)
        if value == None: 
            print()
            break

        print(value)

main()
