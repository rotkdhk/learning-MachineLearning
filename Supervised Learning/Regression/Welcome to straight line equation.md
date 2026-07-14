
## The Caveman Story
 
Imagine a caveman walking into a cave. Right at the entrance, the cave is wide. But as he walks further and further inside, the cave **narrows**, the walls close in a little more with every meter he walks.
 
He's curious: *"If I walk 100 meters into the cave, how narrow will it be there?"*
 
He doesn't want to walk all 100 meters just to check. So he measures the cave's width at a few points he's **already walked**, and looks for the *pattern*.
 
### The data points
 
| Meters walked in (x) | Cave width (y, in cm) |
|------------------------|--------------------------|
| 10                     | 95                       |
| 20                     | 90                       |
| 30                     | 85                       |
| 40                     | 80                       |
 
### Plotting it (the graph)
 
Plot meters walked (x) on the bottom, and cave width (y) on the side. These 4 points fall in a perfectly **straight line**, sloping downward — the further he walks in, the narrower it gets:
 
```
width
100 |
 95 |  •
 90 |     •
 85 |        •
 80 |           •
 75 |
    +---+---+---+---+---- meters walked in
    0   10  20  30  40
```
 
A straight line always follows this formula:
 
```
y = m*x + c
```
 
- `y` = what we want to predict (cave width)
- `x` = what we already know (meters walked in)
- `m` = **slope** — how steep the line is (how fast the width shrinks),rate of change b/w 2 points -> Change in output/Change in Input
- `c` = **intercept** — where the line starts, at x = 0 (right at the entrance)
### Finding the slope (m)
 
Slope = **how much y changes, for every 1 unit x changes**.
 
Pick any two points, say (10, 95) and (20, 90):
 
```
m = (y2 − y1) / (x2 − x1)
  = (90 − 95) / (20 − 10)
  = (−5) / (10)
  = −0.5
```
 
So for every 1 meter he walks in, the cave width shrinks by **0.5 cm**. Negative slope = line goes downward.
 
Check with another pair, (30, 85) and (40, 80), to confirm it's really a straight line:
 
```
m = (80 − 85) / (40 − 30)
  = (−5) / (10)
  = −0.5
```
 
Same slope both times ✓ confirms it's a straight line.
 
### Finding the intercept (c)
 
`c` is the cave width right at the entrance, when he's walked `x = 0` meters in.
 
We know at x = 10, y = 95. Plug into `y = m*x + c` and solve for `c`:
 
```
95 = (−0.5)(10) + c
95 = −5 + c
c  = 95 + 5
c  = 100
```
 
So the cave entrance is **100 cm** wide.
 
### The full equation
 
```
y = −0.5x + 100
```
 
### Predicting at 100 meters walked in
 
Now the caveman's real question, cave width at x = 100:
 
```
y = (−0.5)(100) + 100
  = −50 + 100
  = 50
```
 
**Prediction: 100 meters into the cave, it will be 50 cm wide.**
 
He never had to walk that far to know it — the straight-line pattern from just 4 measurements told him.

---

> Going forward will use this equation as **y = wx+b**
