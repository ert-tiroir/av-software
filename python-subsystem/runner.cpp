
#include <python-subsystem/runner.h>
#include <python-subsystem/subprocess.h>

TwoPipe* startPythonSoftware () {
    return subprocess("python3", "python3", "python-software/main.py");
}
