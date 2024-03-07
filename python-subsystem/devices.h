#include <python-subsystem/pipe.h>


struct AtmosphericData{
    double temperature;
    double presure;
    double altitude;
};

struct Dps310Device {
    public : 
    AtmosphericData query (TwoPipe* Pipe);
    
};
