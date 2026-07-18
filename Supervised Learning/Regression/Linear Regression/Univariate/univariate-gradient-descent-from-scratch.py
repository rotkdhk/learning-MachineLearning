import numpy as np
import matplotlib.pyplot as plt

def compute_gradient(w,b):
    dw = 1/m*sum((w*x[i]+b-y[i])*x[i] for i in range(m))
    db = 1/m*sum((w*x[i]+b-y[i]) for i in range(m))
    return dw, db

x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([3.1, 4.9, 7.2, 8.8, 11.1])

m = len(x)
alpha = 0.001
iterations = 10000
w, b = 0, 0
for i in range(iterations):
    dw, db = compute_gradient(w, b)
    p_w, p_b = w, b #previous
    w = w - alpha*dw
    b = b - alpha*db
    if abs(w - p_w) <= 1e-7 and abs(b - p_b) <= 1e-7:
        print(f"Converged at iteration {i}")
        break

print(w, b)
