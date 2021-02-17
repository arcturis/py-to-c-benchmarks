# Test for python to C interface using ctypes

This is a speed test for interfacing with C shared object files from a python script using ctypes.

## Building manually
- `gcc -fpic -o low_latency.o -c low_latency.c`
- `ld -shared low_latency.o -o low_latency.so`
- `python3 tester.py`

## Building with Make
- `make`
- `python3 tester.py`
