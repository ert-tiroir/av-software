
#include <python-subsystem/runner.h>
#include <python-subsystem/devices.h>
#include <string>
#include <iostream>

#include <chrono>
#include <thread>

using namespace std::this_thread; 
using namespace std::chrono;

int main () {
    TwoPipe* python = startPythonSoftware();
    python->useBlocking(false);

    std::cout << "Starting AV-Nordli Software\n";
    
    AtmosphericData data;
    
    Dps310Device device; 
       
    
    while (true) {
        data = device.query(python); 
        
        std::cout << "==============\n";
        std::cout << "Temperature : " << data.temperature << " °C\n";
        std::cout << "Pressure    : " << data.pressure << " hPa\n";
        std::cout << "Altitude    : " << data.altitude << " m\n";

        sleep_for( seconds(1) );
    }

    python->closeWriter();
}
