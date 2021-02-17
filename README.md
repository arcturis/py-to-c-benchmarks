# Test for python to C interface using SWIG

This is a speed test for interfacing with C shared object files from a python script.

## Building manually
(This is a useful starter: http://www.swig.org/tutorial.html)
- Install SWIG
- Install `python3-dev` for the `Python.h` file in `/usr/local/include/python3`
- Generate the python and C interface files with `swig -python low_latency.i`
- Compile the library and interface code in a position-independent way, using the Python.h file: `gcc -fpic -c low_latency.c low_latency_wrap.c -I/usr/local/include/python3.8`
- Use the linker to squash these object files into a shared object library: `ld -shared low_latency.o low_latency_wrap.o -o _low_latency.so`
- You should now be able to `import low_latency` in python, and run the tester script.

## Building with CMake
- Install SWIG
- Install `python3-dev` for the `Python.h` file in `/usr/local/include/python3`
- `mkdir build ; cd build`
- `cmake ..`
- `make`
- You can now export the `low_latency.py` and `_low_latency.so` to run the tester script.
