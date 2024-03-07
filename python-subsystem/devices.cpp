#include <python-subsystem/devices.h>
#include <string.h>
#include <sstream>
#include <string>

AtmosphericData Dps310Device :: query (TwoPipe* pipe){
    {
        char buffer[5]; 
        memcpy(buffer, "0x76\n", 5); 
        pipe->write(buffer,5);
    }

   std::string buffer = "";
   while (buffer.size() == 0) buffer = pipe->readAll();
   while (buffer[buffer.size() - 1] != '\n')
        buffer += pipe->readAll();

   std::stringstream stream(buffer); 
   AtmosphericData data;
   stream>>data.temperature; 
   stream>>data.pressure; 
   stream>>data.altitude; 

    return data;
}


