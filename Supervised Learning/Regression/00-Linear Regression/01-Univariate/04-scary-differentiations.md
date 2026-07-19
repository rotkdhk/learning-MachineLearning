# Scary Differentiations
 
## What is Differentiation?
 
### Slope vs. Differentiation, what's the difference?
 
Earlier, when we derived $y = mx + c$, we calculated **slope** using two points:
 
$$m = \frac{y_2 - y_1}{x_2 - x_1}$$
 
That works perfectly for a **straight line** , the slope is the *same* everywhere, so any two points give the right answer.
 
But most real functions (like $f(x) = x^2$) are **curves**, not straight lines. A curve's steepness keeps changing , it's steep in some places, flatter in others. So "pick any two points" no longer gives one honest answer; the slope between two far-apart points on a curve is just an average, not the true steepness at either point.
 
**Differentiation solves this by asking for the slope at just one single point** , not between two points, but the *instantaneous* rate of change, right at that exact spot on the curve. That's why we made the second point "tiny" ($x = 3 \to 3.01$) instead of far away , as that gap shrinks toward zero, the "slope between two points" becomes the "slope at one point," which is the derivative.
 
So:
- **Slope** → rate of change **between 2 points** (only truly constant for a straight line)
- **Differentiation / derivative** → rate of change **at any one point**, instantaneously , works for curves too
The whole concept of **differentiation** is to find the **rate of change** at a moment.
 
What is meant by that? **Differentiation gives derivative** , and what the derivative tells us is: if we move $x$ by a tiny change, what will be the rate of change in the output?
 
### Working it out with a real example
 
Let's take the function:
 
$$f(x) = x^2$$
 
Start at $x = 3$:
 
$$f(3) = 3^2 = 9$$
 
Now nudge $x$ by a **tiny change** , say, $0.01$:
 
$$x = 3.01 \quad\Rightarrow\quad f(3.01) = 3.01^2 = 9.0601$$
 
So a tiny change in $x$ (by 0.01) caused a change in output. Let's measure exactly how much:
 
$$\text{change in output} = 9.0601 - 9 = 0.0601$$
$$\text{change in input} = 3.01 - 3 = 0.01$$
 
Now divide change in output by change in input:
 
$$\frac{0.0601}{0.01} = 6.01 \approx 6$$
 
### What does that "6" mean?
 
If we change $x$ by $0.01$, then the output will change by **approximately 6 times that change**:
 
$$0.01 \times 6 = 0.06$$
$$9 + 0.06 = 9.06 \quad \text{← very close to our actual } 9.0601 \; ✓$$
 
So **differentiation gives the derivative**, and here the derivative is $\approx 6$. What it tells us is: if we move $x$ by a tiny change, the rate of change in output will be about 6 times that change.
 
### Generalizing it
 
We just found that at $x = 3$, the rate of change of $f(x) = x^2$ is $2 \times 3 = 6$. Let's check this isn't a coincidence , the general pattern is:
 
$$\frac{d}{dx}(x^2) = 2x$$
 
At $x = 3$: $2(3) = 6$ ✓ , matches exactly what we calculated by hand above.
 
This confirms: **differentiation isn't a rule to memorize , it's literally "how much does output change, for a tiny change in input,"** and we just proved it numerically before trusting the shortcut formula.
 
---
 
## Rules of Differentiation
 
Now that we've derived the *idea* by hand, here are the shortcut rules , each one is just a faster way to get the same answer.
 
### 1. Constant Rule
 
$$\frac{d}{dx}(c) = 0$$
 
If $c$ is just a fixed number (like 5, or 100), it never changes , so no matter how much we change $x$, there's **no change** in output. Nothing will happen if we change $x$. Rate of change = 0.
 
### 2. Power Rule
 
$$\frac{d}{dx}(x^n) = n \cdot x^{n-1}$$
 
This is exactly what we derived above for $x^2$ ($n = 2$, so $2 \cdot x^1 = 2x$).
 
### 3. Constant Multiply Rule
 
$$\frac{d}{dx}\big(c \cdot f(x)\big) = c \cdot \frac{d}{dx}f(x)$$
 
If a function is multiplied by a fixed constant, the constant just carries through , you differentiate the function part and multiply the constant back in afterward.
 
### 4. Product Rule
 
$$\frac{d}{dx}\big(f(x) \cdot g(x)\big) = f(x)\cdot \frac{d}{dx}g(x) + g(x)\cdot \frac{d}{dx}f(x)$$
 
Used when **two changing functions** are multiplied together (not one function times a fixed constant). Each one gets differentiated in turn, while the *other* is temporarily held as-is, and the two results are added.
 
---
 
## Chain Rule (brief intro)
 
$$\frac{d}{dx}(y^2) = 2y \cdot \frac{dy}{dx}$$
 
Here, both $x$ and $y$ are changing , they're not independent. We're changing $x$, and we want to check: what effect does that have on the *other* function $y$?
 
So the derivative of $y^2$ isn't just $2y$ , we also multiply by $\frac{dy}{dx}$, because a change in $x$ affects $y$, and that change in $y$ then affects $y^2$. This chaining together of one effect causing another is exactly why it's called the **chain rule** , we'll use it directly when deriving the cost function's derivative.
 
---
 
## Partial Derivatives
 
Let's say:
 
$$f(x, y) = x^2 y$$
 
This function has **two variables** , $x$ and $y$. A **partial derivative** asks: if I change just *one* of them, and freeze the other, how does the output change?
 
### Differentiating with respect to x
 
$$\frac{\partial f}{\partial x} = \frac{\partial}{\partial x}(x^2 y)$$
 
Here, $y$ **plays constant** , it's not changing, so it just rides along:
 
$$= 2x \cdot y = 2xy$$
 
### Differentiating with respect to y
 
$$\frac{\partial f}{\partial y} = \frac{\partial}{\partial y}(x^2 y)$$
 
Now $x^2$ **plays constant** instead:
 
$$= x^2 \cdot \frac{dy}{dy} = x^2$$
 
### What this means, in general
 
When a function has **2 or more variables**, and you want the derivative as you change **one** variable while **freezing the others** , that's a **partial derivative**.
 
- Treat the other variables as constants
- Change in the one variable you're focused on
- See how the output changes
This is exactly the tool we need next: our cost function $J(w, b)$ has **two variables**, $w$ and $b$ , so to find how it changes with respect to each one separately, we take **partial derivatives**: $\frac{\partial J}{\partial w}$ and $\frac{\partial J}{\partial b}$.
