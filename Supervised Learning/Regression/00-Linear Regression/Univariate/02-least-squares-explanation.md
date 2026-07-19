### What is "Least Squares"?
 
**Least squares** is the method of finding the best-fit line by making the **sum of squared errors** as small as possible.
 
Recall, for any line, each datapoint has an error:
 
$$\text{error} = y^{(i)} - f(x^{(i)})$$
 
Some errors are positive (point above the line), some are negative (point below the line). If we just added them as-is, they'd cancel out — a line could look "perfect on average" while actually missing every point badly.
 
**Least squares fixes this by squaring each error before summing:**
 
$$\text{sum of squared errors} = \sum_{i=1}^{m} \left(y^{(i)} - f(x^{(i)})\right)^2$$
 
Squaring does two things:
- Makes every error **positive**, so they can't cancel each other out
- **Punishes big misses harder** than small ones (an error of 10 becomes 100, but an error of 20 becomes 400 — four times worse, not just double)
The **"least"** in least squares means: out of every possible straight line we could draw, we want the **one specific line** whose sum of squared errors is the **smallest possible**.
 
This is exactly what the **cost function $J(w,b)$** measures — it's the least-squares sum, just averaged over all $m$ points instead of left as a raw total. So when we say "find $w, b$ that minimizes $J(w,b)$," we're really saying: **find the least-squares line**.
