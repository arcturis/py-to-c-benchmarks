CC=gcc
CFLAGS=-fpic
LD=ld

all: library

low_latency.o: low_latency.c
	$(CC) $(CFLAGS) -o low_latency.o -c low_latency.c

library: low_latency.o
	$(LD) -shared low_latency.o -o low_latency.so
	rm -f low_latency.o

clean:
	rm -f low_latency.so
	rm -f low_latency.o
