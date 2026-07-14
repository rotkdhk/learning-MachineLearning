# Gradient Descent

## What is a Gradient?

In general, **gradient** is basically the rate of change **with direction**, for a function of several variables — it's just the collection of **partial derivatives**.

## Going back to the Cost Function

$$J(w, b) = \frac{1}{2m}\sum_{i=1}^{m} \left(f_{w,b}(x_i) - y_i\right)^2 \qquad \text{where } f_{w,b}(x_i) = wx_i + b$$

Since we can't just randomly guess $w$ and $b$ and hope it works, let's generate them — start at $w = 0, b = 0$.

**What is the derivative here?** It means: for a **tiny change** in $w$ and $b$, how does it affect the cost function?

---

## Deriving $\frac{\partial J}{\partial w}$

$$\frac{\partial J}{\partial w} = \frac{\partial}{\partial w}\left[\frac{1}{2m}\sum_{i=1}^{m}\left(f(x_i) - y_i\right)^2\right]$$

The $\frac{1}{2m}$ is a constant multiplier, so it just carries through:

$$= \frac{1}{2m}\frac{\partial}{\partial w}\sum_{i=1}^{m}\left(f(x_i) - y_i\right)^2$$

Now apply the **chain rule** — remember, $\frac{d}{dx}(y^2) = 2y\cdot\frac{dy}{dx}$. Here, treat $\left(f(x_i)-y_i\right)$ as our "$y$":

$$= \frac{1}{2m}\sum_{i=1}^{m} 2\left(f(x_i)-y_i\right)\cdot \frac{\partial}{\partial w}\left[f(x_i)-y_i\right]$$

The 2 cancels with the $2m$ in the denominator:

$$= \frac{1}{m}\sum_{i=1}^{m}\left(f(x_i)-y_i\right)\cdot \frac{\partial}{\partial w}\left[wx_i + b - y_i\right]$$

Now differentiate the inner bracket **with respect to $w$** — remember, in partial derivatives, everything except $w$ is frozen (treated as constant):

$$\frac{\partial}{\partial w}\left[wx_i + b - y_i\right] = x_i \cdot \underbrace{\frac{\partial w}{\partial w}}_{=1} + \underbrace{\frac{\partial b}{\partial w}}_{=0} - \underbrace{\frac{\partial y_i}{\partial w}}_{=0} = x_i$$

($b$ is frozen/constant here, and $y_i$ is just data — neither depends on $w$, so both terms vanish.)

So we're left with:

$$\boxed{\frac{\partial J}{\partial w} = \frac{1}{m}\sum_{i=1}^{m}\left(f(x_i) - y_i\right)\cdot x_i}$$

---

## Deriving $\frac{\partial J}{\partial b}$

Same process, but now differentiating with respect to $b$ (freezing $w$ instead):

$$\frac{\partial J}{\partial b} = \frac{1}{2m}\sum_{i=1}^{m} 2\left(f(x_i)-y_i\right)\cdot \frac{\partial}{\partial b}\left[wx_i + b - y_i\right]$$

$$\frac{\partial}{\partial b}\left[wx_i + b - y_i\right] = \underbrace{\frac{\partial (wx_i)}{\partial b}}_{=0} + \underbrace{\frac{\partial b}{\partial b}}_{=1} - \underbrace{\frac{\partial y_i}{\partial b}}_{=0} = 1$$

(This time $w$ is frozen, so $wx_i$ doesn't depend on $b$ and vanishes.)

$$\boxed{\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}\left(f(x_i) - y_i\right)}$$

---

## What Does the Derivative Actually Tell Us?

Just like our earlier $x^2$ example — where a derivative of $6$ meant "a tiny change in $x$ causes about 6 times that change in output" — the same logic applies here.

If $\frac{\partial J}{\partial w} = +16$, it means: **if we change $w$ by a tiny amount $\Delta w$, the cost function $J$ will change by approximately $16 \times \Delta w$.**

### What does the sign (+ or −) mean?

Recall: $\frac{\partial J}{\partial b} = \frac{1}{m}\sum_{i=1}^{m}\left(f(x_i) - y_i\right)$ — this is just the **average error**, where error = predicted − actual.

- **If this average comes out positive (+ve):** it means, on average, $f(x_i) > y_i$ — our **predictions are higher than the actual data**. In other words, the current line (with this $w, b$) sits **above** the actual datapoints on average.
 - **If this average comes out negative (−ve):** it means, on average, $f(x_i) < y_i$ — our **predictions are lower than the actual data**. The current line sits **below** the actual datapoints on average.
 
  - So the derivative isn't just an abstract number — its **sign tells us whether our current line is overshooting or undershooting the data**, and its **magnitude** tells us how much a tiny nudge in $w$ (or $b$) will shift the cost — exactly the same way $6$ told us how much a tiny nudge in $x$ shifted $x^2$.
 
  - That's exactly why the update rule subtracts the derivative — if the line is sitting above the data (+ve derivative), subtracting a positive number pulls the line **down**; if the line is sitting below the data (−ve derivative), subtracting a negative number pushes the line **up**. Either way, we move toward the data.
 
  - ---

  ## The Update Rule

  $$w := w - \alpha\frac{\partial J}{\partial w}$$

  $$b := b - \alpha\frac{\partial J}{\partial b}$$

  But there's a catch: $\frac{\partial J}{\partial w}$ or $\frac{\partial J}{\partial b}$ **can be huge!** If we subtract the raw derivative directly, we could overshoot wildly. That's why we introduce:

  $$\alpha \rightarrow \textbf{learning rate}$$

  $\alpha$ controls **how big a step** we actually take, based on the derivative — it scales the derivative down (or up) to a sensible step size.

  ### Worked example

  Say the derivative comes out to $+16$, and we set $\alpha = 0.001$:

  $$\alpha \cdot \frac{\partial J}{\partial w} = 0.001 \times 16 = 0.016$$

  If $w = 4$ currently:

  $$w := 4 - 0.016 = 3.984$$

  So even though the raw derivative was a big number (16), the learning rate shrinks the actual step down to something small and safe (0.016).

  ---

  ## Repeat Until Convergence

  $$w := w - \alpha\frac{\partial J}{\partial w} \qquad b := b - \alpha\frac{\partial J}{\partial b}$$

  We repeat this update **until convergence** — when things become similar step after step. For example:

  $$w = 2 \to w = 3 \to w = 3.001 \to w = 4 \to w = 4 \to w = 4 \;(\text{similar} \Rightarrow \text{converged})$$

## Why We're Trying to Reach the Bottom

Let's use our familiar dataset again: $x=[1,2,3]$, $y=[2,4,6]$, fixing $b=0$. Here's $J(w)$ and its derivative $\frac{\partial J}{\partial w}$ side by side:

| $w$ | $J(w)$ | $\frac{\partial J}{\partial w}$ |
|-----|--------|-----------------------------------|
| 0.0 | 9.33 | −9.33 |
| 1.0 | 2.33 | −4.67 |
| 1.5 | 0.58 | −2.33 |
| **2.0** | **0.00** | **0.00** |
| 2.5 | 0.58 | +2.33 |
| 3.0 | 2.33 | +4.67 |
| 4.0 | 9.33 | +9.33 |

Look at the derivative column: it shrinks steadily as $w$ approaches $2$, hits **exactly zero** at $w=2$, then grows again on the other side. That zero is the "bottom" — the one point on the whole curve where the slope goes flat, and it lines up exactly with $J(w)=0$, the smallest error possible.

### Watching gradient descent actually walk there

Start at $w=0$, with learning rate $\alpha=0.1$, and just apply $w := w - \alpha\frac{\partial J}{\partial w}$ repeatedly:

| Step | $w$ (before) | $\frac{\partial J}{\partial w}$ | Step taken | $w$ (after) | $J(w)$ |
|------|---------------|-----------------------------------|------------|--------------|--------|
| 0 | 0.0000 | −9.33 | +0.933 | 0.9333 | 2.65 |
| 1 | 0.9333 | −4.98 | +0.498 | 1.4311 | 0.76 |
| 2 | 1.4311 | −2.65 | +0.266 | 1.6966 | 0.21 |
| 3 | 1.6966 | −1.42 | +0.142 | 1.8382 | 0.061 |
| 4 | 1.8382 | −0.76 | +0.076 | 1.9137 | 0.017 |
| 5 | 1.9137 | −0.40 | +0.040 | 1.9540 | 0.0049 |

**Watch the "step taken" column**: 0.933 → 0.498 → 0.266 → 0.142 → 0.076 → 0.040. Each step is roughly **half** the previous one — nobody told it to slow down; it's a direct consequence of the derivative itself shrinking as $w$ nears $2$. And look at $J(w)$: 2.65 → 0.76 → 0.21 → 0.061 → 0.017 → 0.0049 — the error keeps dropping, faster at first, then more gently, exactly matching how the bowl flattens near the bottom.

If we kept going, $w$ would keep creeping closer to $2.000$ and $J(w)$ closer to $0$, but the *steps themselves* would keep shrinking — that's what "convergence" actually looks like in practice, not a sudden stop, but the updates fading out as we near the flat floor of the bowl.

---
  
