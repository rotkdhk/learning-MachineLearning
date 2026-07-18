## Cost Function
 
**The question:** for a given $w$ and $b$, what is the average error across **all** datapoints?
 
That's exactly what the cost function measures.
 
<img width="1050" height="750" alt="image" src="https://github.com/user-attachments/assets/fcccfe09-cd73-440d-812d-c231ed7bb3dd" />
 
*(Red line = high cost, far from most points. Green line = low cost, near most points — as we saw earlier when comparing the two candidate lines.)*
 
### The formula
 
$$J(w, b) = \frac{1}{2m}\sum_{i=1}^{m} \left(f_{w,b}(x^{(i)}) - y^{(i)}\right)^2$$
 
Breaking each piece down:
 
- $m$ → **number of training inputs** (rows in the dataset)
- $f_{w,b}(x^{(i)})$ → the **model function's prediction** for the i-th input — this is our $\hat{y}$
- $y^{(i)}$ → the **actual data output** for the i-th input
- $f_{w,b}(x^{(i)}) - y^{(i)}$ → the **error** for that one point (predicted − actual)
- squaring it → makes every error positive, and punishes big misses harder (as we saw in the earlier error section)
- $\sum$ (sigma) → sum this squared error across **all** $m$ points
- dividing by $2m$ → takes the **average** (the extra factor of 2 is just there to make the derivative cleaner later — it doesn't change *which* $w, b$ minimizes $J$)
### What we're really asking
 
For **all** $x$, calculate what error is produced. We need the $w, b$ that generates the **least value of $J(w,b)$** — the smallest possible average error.
 
### Why can't we just guess w and b?
 
Because we can't manually guess $w$ and $b$ randomly and hope it works. So instead:
 
1. Start with some values — say $w = 0, b = 0$
2. Ask: **what is the derivative** at this point?
3. Use that derivative to know *which direction* to adjust $w$ and $b$
4. Repeat until we reach the **least value of $J(w,b)$**
This is exactly where **differentiation** comes back in — the derivative of the cost function tells us which way to move $w$ and $b$ to make the error smaller. That's what we derive next.
