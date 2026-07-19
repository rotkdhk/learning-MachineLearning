# Feature Scaling, Standard Deviation & Z-score
 
## 1. What is Feature Scaling?
 
**Feature scaling / data normalization / standardization** — convert a large dataset into small numbers.
 
The goal: figure out **where each value sits between the high and low** of that feature.

### Why we need it (for multiple linear regression)
 
Features often live on very different scales (e.g. size in thousands of sq ft vs. bedrooms as single digits). When features aren't scaled, gradient descent's updates get skewed — the large-scale feature dominates the gradient step, and the cost function's contours become long, narrow ellipses instead of circles. This makes gradient descent zig-zag and converge slowly (or not at all), instead of taking a direct path to the minimum. Scaling puts all features on comparable ranges so gradient descent converges faster and more smoothly.
 
---
 
## 2. Min-Max Scaling
 
```
scaled value = (value - min) / (max - min)
```
 
**Example — Salary feature:**
 
| min | max | max - min |
|---|---|---|
| 20 | 90 | 70 |
 
| Salary | Calculation | Result |
|---|---|---|
| 20k | (20-20)/70 | 0 |
| 22k | (22-20)/70 | 0.029 |
| 24k | (24-20)/70 | 0.057 |
| 26k | (26-20)/70 | 0.086 |
| 70k | (70-20)/70 | 0.714 |
| 90k | (90-20)/70 | 1.00 |
 
All values land between 0 and 1.
 
**Weakness — outliers.** In this example the 90k salary is an outlier. Because Min-Max scaling anchors everything to the min and max, one extreme outlier compresses every other (normal) value into a tiny sliver of the 0–1 range — it completely distorts everyone else's scale.
 
---
 
## 3. Standard Deviation (SD)
 
**What it measures:** how many steps (typically) a value is away from the average (mean).
 
**Why it's needed:** two datasets can have the *same mean* but be spread very differently — the mean alone doesn't tell you how tightly the values cluster around it.
 
**Example:**
```
A = (4, 5, 6)   → mean = 5
B = (1, 5, 9)   → mean = 5
```
Both have the same mean, but A's values are close together and B's are spread far apart. SD is what tells them apart.
 
### Calculating SD for A = (4, 5, 6)
 
| Value | Mean | Distance | Error² (Distance²) |
|---|---|---|---|
| 4 | 5 | -1 | 1 |
| 5 | 5 | 0 | 0 |
| 6 | 5 | +1 | 1 |
 
**Formula:**
```
SD = √( Σᵢ (vᵢ - mean)² / N )
```
 
```
SD = √(2/3) = √0.66 = 0.816
```
 
**Variance** is basically SD squared:
```
Variance = (SD)² = 0.666
```
 
### Same calculation for B = (1, 5, 9)
```
distances: -4, 0, +4
squared:    16, 0, 16   → sum = 32
SD = √(32/3) = √10.66 ≈ 3.27
```
 
### What these numbers are telling us
 
```
mean = 5, SD = 0.816   →   value 4 is ≈ ±0.816 away from the mean (not exact, approximate)
```
 
So for **A**, a typical value sits about 0.816 away from 5.
For **B**, a typical value sits about 3.27 away from 5 — much more spread out, even though both means are 5.
 
---
 
## 4. Z-score
 
**What it measures:** how many SD-steps a value is from the mean (a standardized "distance").
 
```
z-score = (value - mean) / SD
```
 
This is the basis of **standardization** — instead of scaling by min/max (which outliers can distort), each value is rescaled relative to the *typical spread* (SD) of the whole dataset, making it far less sensitive to outliers than Min-Max scaling.
 
---
