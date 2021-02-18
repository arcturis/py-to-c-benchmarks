CC=g++
CFLAGS=-shared -fPIC -std=c++11 -O0 
PYBIND11_INCLUDES=$(shell python3 -m pybind11.pybind11 --includes)

all: library

pybind11:
	git clone https://github.com/pybind/pybind11.git

library: pybind11
	$(CC) $(CFLAGS) $(PYBIND11_INCLUDES) low_latency.c low_latency_bindings.cpp -o low_latency.so

clean:
	rm -f low_latency.so
