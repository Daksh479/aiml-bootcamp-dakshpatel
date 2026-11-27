# • Write three operations as plain Python loops: squaring every element, summing all elements, and computing a
#   dot product of two lists.
# • Rewrite each as a vectorised NumPy operation.
# • Time both versions with timeit. Use number=10 or more — a single run is noise, not a measurement.
# • Repeat at four sizes: 1,000 / 10,000 / 100,000 / 1,000,000 elements. Build a small results table.
# • Plot the speedup against array size with matplotlib.

import timeit
import numpy as np
import matplotlib.pyplot as plt

# --- Plain Python loop versions ---
def py_square(a):
    out = []
    for x in a:
        out.append(x * x)
    return out

def py_sum(a):
    total = 0
    for x in a:
        total += x
    return total

def py_dot(a, b):
    total = 0
    for x, y in zip(a, b):
        total += x * y
    return total

# --- Helper: average seconds per call ---
def avg_time(func):
    return timeit.timeit(func, number=10) / 10

# --- Benchmark ---
sizes = [1_000, 10_000, 100_000, 1_000_000]
speedups = {"Square": [], "Sum": [], "Dot": []}

print(f"{'Size':>9} {'Op':<7} {'Python(s)':>10} {'NumPy(s)':>10} {'Speedup':>8}")

for n in sizes:
    a, b = list(range(n)), list(range(n, 2 * n))   # Python lists
    A, B = np.array(a), np.array(b)                # same data as NumPy arrays

    tests = {
        "Square": (lambda: py_square(a), lambda: A * A),
        "Sum":    (lambda: py_sum(a),    lambda: A.sum()),
        "Dot":    (lambda: py_dot(a, b), lambda: A @ B),
    }

    for name, (py_f, np_f) in tests.items():
        t_py, t_np = avg_time(py_f), avg_time(np_f)
        speedups[name].append(t_py / t_np)
        print(f"{n:>9,} {name:<7} {t_py:>10.6f} {t_np:>10.6f} {t_py / t_np:>7.1f}x")

# --- Plot ---
for name, values in speedups.items():
    plt.plot(sizes, values, marker="o", label=name)

plt.xscale("log")
plt.yscale("log")
plt.xlabel("Array size")
plt.ylabel("Speedup (Python time / NumPy time)")
plt.title("Python loops vs NumPy")
plt.legend()
plt.grid(True)
plt.show()