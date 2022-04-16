import time

start_1 = time.time()
a = 0
for i in range(1000000):
    a += i
end_1 = time.time()
print(f"time range in loop: {end_1- start_1}")

start_1 = time.time()
rng = range(1000000)
for i in rng:
    a += i
end_1 = time.time()
print(f"time range out of loop: {end_1- start_1}")