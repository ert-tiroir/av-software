#include <python-subsystem/pipe.h>


struct AtmosphericData{
    double temperature;
    double pressure;
    double altitude;
};

struct Dps310Device {
    public : 
    AtmosphericData query (TwoPipe* Pipe);
    
};
