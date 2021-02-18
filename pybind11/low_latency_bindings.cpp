#include <pybind11/pybind11.h>
#include "low_latency.h"

PYBIND11_MODULE(low_latency, m) {
    m.doc() = "low_latency test code for pybind11";

    m.def("run_me", &run_me, "Test function for calling from python");
}

