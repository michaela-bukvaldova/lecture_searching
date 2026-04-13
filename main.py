import time
from generators import ordered_sequence
from searching import linear_search, binary_search

ns = []
times_linear = []
times_binary = []
for n in ns:
    seq = ordered_sequence(n)

    # ns = list(range(1, 1000, 100))


    start = time.perf_counter()
    res1 = linear_search(seq, 5)
    time_ = time.perf_counter() - start
    times_linear.append(time_)
    end = time.perf_counter()

    start = time.perf_counter()
    res2 = binary_search(seq,5)
    time_ = time.perf_counter()
    times_binary.append(time_)

import matplotlib.pyplot as plt

sizes = [100, 500, 1000, 5000, 10000]
times = [0.00001, 0.00003, 0.00006, 0.00031, 0.00067]

plt.plot(sizes, times)

plt.xlabel("Velikost vstupu")
plt.ylabel("Čas [s]")
plt.title("Ukázkový graf měření")
plt.show()

