import ctypes
#import glob
import os
import time

print("Starting test")

#low_latency_file = glob.glob("low_latency.so")[0]
low_latency_file = os.path.abspath("low_latency.so")
low_latency = ctypes.CDLL(low_latency_file)

# Configure ctypes with info on the return and argument types of function
low_latency.run_me.restype = ctypes.c_int
low_latency.run_me.argtypes = [ctypes.c_char_p]

# Run once, just in case first-time-load impacts significantly as I don't care about that stat
low_latency.run_me("start".encode("utf-8"))

start = time.perf_counter()
text = "something".encode("utf-8")
for i in range(10000):
    low_latency.run_me(text)
end = time.perf_counter()
count = low_latency.run_me("".encode("utf-8"))
print("Execution = {} runs took {}s".format(count, (end - start)))

print("Ending test")
