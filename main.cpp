
#include <python-subsystem/runner.h>
#include <string>
#include <iostream>

int main () {
    TwoPipe* python = startPythonSoftware();
    python->useBlocking(false);

    while (true) {
        std::string data = python->readAll();

        if (data.size() != 0) std::cout << data;
    
        if (data.size() != 0 && data[data.size() - 1] == 0) break ;
    }

    python->closeWriter();
}
