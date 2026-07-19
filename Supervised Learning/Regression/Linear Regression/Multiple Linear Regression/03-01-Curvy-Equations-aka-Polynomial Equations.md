
# When a straight line isn't enough
 
## The setup
 
House size vs price. You plotted it. Roughly a line.
`y = w*x + b` fit fine. Gradient descent solved it. Done.
 
Now: engagement score vs tenure (your churn project).
You plot it, expecting the same thing.
 
It doesn't line up.
 
Drops fast early. Flattens out later. That's a curve, not a line.
 
## The failed attempt
 
You try the old model anyway: `y = w*x + b`.
 
It trains. It converges. It still misses.
Cuts straight through the middle of the curve.
No w, no b, can bend a straight line.
 
The model isn't broken. It just can't draw curves.
 
## The trick
 
Keep the same model. Change the input.
 
Instead of x, feed it x².
 
Example. True relationship: `y = 2x²`
 
| x | x² (fed to model) | y |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 4 | 8 |
| 3 | 9 | 18 |
| 4 | 16 | 32 |
| 5 | 25 | 50 |
| 6 | 36 | 72 |
 
Plot x vs y → curve.
Plot x² vs y → straight line.
 
Same data. Same 6 points. Only the x-axis changed.
 
The relationship was straight all along.
It only looked curved through raw x.
 
Model trains as: `y = w*(x²) + b`
Same gradient descent. Same update rule.
 
Write it back in terms of x:
 
`y = w*x² + b`
 
Looks curved from outside. Straight on the inside.
 
## Two names for this
 
**Polynomial equation** — the shape:
 
`y = b + w1*x + w2*x² + w3*x³ + ...`
 
- degree 1 → straight line
- degree 2 → one bend
- degree 3 → up to two bends
Still "linear" regression — linear in the *weights*.
Only the input got curved.
 
**Feature engineering** — the general habit.
Squaring x is one example.
Others: income / family_size, log of a skewed column,
hours_worked * hourly_rate.
 
Model stays dumb. Inputs get smarter.
 
## Feeding both x and x²
 
Why not just x²? Two reasons.
 
x² loses the sign — x=3 and x=-3 both give 9.
Feeding x too keeps that information.
 
Also, real curves are rarely *pure* x².
Usually a mix of straight-line part and curved part:
 
`y = b + w1*x + w2*x²`
 
Two features, two weights, plus bias.
Gradient descent finds all three — same rule as before,
just one more partial derivative, one more update.
 
**Numeric example**
 
Back to our data: true relationship is y = 2x², no straight part at all.
 
So gradient descent should converge to: b=0, w1=0, w2=2
 
| x | x² | w1*x (w1=0) | w2*x² (w2=2) | y = b + w1*x + w2*x² |
|---|---|---|---|---|
| 1 | 1 | 0 | 2  | 0 + 0 + 2 = 2   |
| 2 | 4 | 0 | 8  | 0 + 0 + 8 = 8   |
| 3 | 9 | 0 | 18 | 0 + 0 + 18 = 18 |
 
Matches the original table exactly.
w1 came out 0 because this data has zero straight-line component.
 
If the data *did* have a straight part mixed in, w1 would come out
non-zero too — that's the case where feeding both x and x² actually
earns its keep.
 
## Where it breaks
 
`y = x²` → one y per x. Fine.
 
`x² + y² = r²` (a circle) → two y's per x. Not a function.
 
Squaring x bends a line. It can't close a loop.
Circles need a different structure entirely.
 
## The trap: overfitting
 
More bend isn't free.
 
Degree 1 on curved data → underfits. Misses the pattern.
Degree 2, matching the real curve → good fit.
Degree 6 → overfits. Wiggles through every point exactly.
 
Training error hits zero. Looks amazing.
 
New data point comes in — way off.
 
Why: those extra wiggles weren't the real pattern.
They were the curve memorizing noise, not learning signal.
 
More features (more powers of x) isn't automatically better.
Match the degree to the actual shape in the data, not more.
