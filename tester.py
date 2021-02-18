import low_latency
import time

print("Starting test")

# Run once, just in case first-time-load impacts significantly as I don't care about that stat
low_latency.run_me("start")

start = time.perf_counter()
for i in range(10000):
    low_latency.run_me("something")
end = time.perf_counter()
count = low_latency.run_me("")
print("Execution = {} runs took {}s".format(count, (end - start)))

print("Ending test")
