
# Multivariate Linear Regression — Notes
 
## 1. From One Feature to Many
 
So far the model only used **one** input feature:
 
```
f(w,b)(x) = wx + b
```
 
But real data (like house prices) has multiple features: size, bedrooms, floors, age of home.
 
| x₁ (size ft²) | x₂ (bedrooms) | x₃ (floors) | x₄ (age, years) | price ($1000s) |
|---|---|---|---|---|
| 2104 | 5 | 1 | 45 | 460 |
 
**Notation:**
- `xⱼ` = the j-th feature (a column)
- `n` = number of features
- `x⁽ⁱ⁾` = all features of the i-th training example (a row vector)
- `xⱼ⁽ⁱ⁾` = value of feature j in the i-th training example
For the example row `[2104, 5, 1, 45]`:
- every extra sq. ft. → price ↑ by 0.1
- every extra bedroom → price ↑ by 4
- every extra floor → price ↑ by 10
- every extra year of age → price ↓ by 2
- plus a base value of 80
So the model becomes:
 
```
f(w,b)(x) = w₁x₁ + w₂x₂ + w₃x₃ + ... + wₙxₙ + b
```
 
This is **multiple linear regression**.
 
---
 
## 2. Vectors
 
A **vector** is just a list of numbers. Nothing more.
 
```
w = [w₁, w₂, w₃, ..., wₙ]   ← parameters (weights)
x = [x₁, x₂, x₃, ..., xₙ]   ← features (input)
```
 
`b` stays a single number (not part of the vector).
 
---
 
## 3. Dot Product
 
**Dot product** = multiply matching positions, then add everything up.
 
Example:
```
a = (2, 3)
b = (4, 6)
 
a · b = (2×4) + (3×6) = 8 + 18 = 26
```
 
Instead of writing out `w₁x₁ + w₂x₂ + ... + wₙxₙ` term by term, this is *exactly* what a dot product computes — we're just representing the same sum compactly.
 
So the multivariate model can be written as:
 
```
f(w,b)(x) = w · x + b
```
 
This is the whole concept behind multiple linear regression — one dot product replaces the entire sum.
 
**Why dot product instead of a for loop, if it's the same math?**
- Same concept, but **not** because of fewer lines of code — because of *execution*.
- A for loop calculates `w[j] * x[j]` one at a time, step by step (sequentially).
- NumPy's dot product runs on **parallel hardware** — even if n = 100, all multiplications happen at the same time, not one after another.
---
 
## 4. Vectorization
 
**Without vectorization (no NumPy):**
 
```python
f = w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + b
 
# or with a loop:
f = 0
for j in range(n):
    f = f + w[j] * x[j]
f = f + b
```
 
**With vectorization (NumPy):**
 
```python
f = np.dot(w, x) + b
```
 
Same math, but NumPy's `dot` runs the multiplications in parallel on hardware — much faster than a Python for loop, especially as `n` grows.
 
---
 
## 5. Gradient Descent — One Feature vs. Multiple Features
 
**One feature:**
```
repeat until convergence:
    w = w - α (dw/dJ)
    b = b - α (db/dJ)
 
dw/dJ = (1/m) Σᵢ (f(w,b)(xⁱ) - yⁱ) xⁱ
db/dJ = (1/m) Σᵢ (f(w,b)(xⁱ) - yⁱ)
```
 
**Multiple features (n ≥ 2):**
```
repeat until convergence:
    wⱼ = wⱼ - α (dJ/dwⱼ)     for j = 1 ... n
    b  = b  - α (dJ/db)
 
dJ/dwⱼ = (1/m) Σᵢ (f(w,b)(x⁽ⁱ⁾) - y⁽ⁱ⁾) xⱼ⁽ⁱ⁾
dJ/db  = (1/m) Σᵢ (f(w,b)(x⁽ⁱ⁾) - y⁽ⁱ⁾)
```
 
**Without vectorization:**
```python
for i in range(16):
    w[j] = w[j] - 0.1 * d[j]   # for all features
```
 
**With vectorization (NumPy):**
```python
w = w - 0.1 * d
```
This one line does the derivative-of-each-feature update, multiplies each by α, and assigns the whole result back to the vector `w` — all in parallel.
 
---
 
## 6. Single Feature vs. Multi-Feature Derivative — the Key Difference
 
**Single feature:**
```
dJ/dw = (1/m) Σᵢ (f(xᵢ) - yᵢ) · xᵢ
```
Here we multiply the error by a **single feature value**.
 
**Multiple features:**
```
dJ/dwⱼ = (1/m) Σᵢ (f(x⁽ⁱ⁾) - y⁽ⁱ⁾) · xⱼ⁽ⁱ⁾
```
Now, for **each sample**, the error must be multiplied against **every feature of that sample** — not just one number. That's why the update needs a nested loop (samples × features) instead of a single loop.
 
`x.shape` gives `(m, n)`:
- `m` = number of samples (rows)
- `n` = number of features (columns)
---
 
## 7. Gradient Function (final, corrected)
 
```python
def gradient(x, y, w, b):
    m, n = x.shape
    dw = np.zeros((n,))
    db = 0.
 
    for i in range(m):
        error = np.dot(w, x[i]) + b - y[i]
        dw = dw + (error * x[i])
        db = db + error
 
    return dw/m, db/m
```
 
### Walking through it
 
1. **`m, n = x.shape`** — `m` samples, `n` features. `dw` needs one slot per feature, so it's initialized as a zero vector of length `n`. `db` is a single number, starts at 0.
2. **`for i in range(m):`** — loop over every training example (row), one at a time.
3. **`error = np.dot(w, x[i]) + b - y[i]`**
   - `np.dot(w, x[i])` computes the dot product of the weight vector with the i-th sample's features — this is `w₁x₁ + w₂x₂ + ... + wₙxₙ` in one shot.
   - Add `b`, subtract the true label `y[i]` → this gives the **prediction error** for sample i: how far off the model's guess was.
4. **`dw = dw + (error * x[i])`**
   - `error` is a single number; `x[i]` is a vector of `n` feature values for that sample.
   - `error * x[i]` multiplies that one error by **every feature** of the sample simultaneously (NumPy broadcasts the scalar across the vector) — giving a length-`n` vector.
   - This is added into the running total `dw`, accumulating the gradient contribution feature-by-feature across all samples.
5. **`db = db + error`** — same idea, but since bias has no associated feature, we just accumulate the raw error.
6. **`return dw/m, db/m`** — after summing over all `m` samples, divide by `m` to get the average — this matches the `(1/m) Σ` in the formula.
### Why no inner `for j in range(n)` loop is needed
Your earlier version had an explicit inner loop over features (`for j in range(n): dw[j] = dw[j] + error*x[i][j]`). The corrected version replaces that entire inner loop with one line — `dw = dw + (error * x[i])` — because NumPy vector addition/multiplication already applies the operation to every feature position at once. This is the same vectorization idea from Section 4: same math, computed in parallel instead of sequentially.
 
---
