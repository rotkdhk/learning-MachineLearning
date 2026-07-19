import numpy as np
import matplotlib.pyplot as plt

# -----------------------
# Sample Data
# -----------------------
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)   # True equation: y = 2x

# -----------------------
# Cost Function
# -----------------------
def compute_cost(w):
    predictions = w * x
    return np.mean((predictions - y) ** 2)

# -----------------------
# Generate Random w values
# -----------------------
np.random.seed(42)

w_values = np.random.uniform(-2, 5, 100)
cost_values = []

for w in w_values:
    cost = compute_cost(w)
    cost_values.append(cost)

# -----------------------
# Plot
# -----------------------
plt.figure(figsize=(8,5))

plt.scatter(w_values, cost_values)

plt.xlabel("w")
plt.ylabel("Cost")
plt.title("Random w values vs Cost")
plt.grid(True)

plt.show()
