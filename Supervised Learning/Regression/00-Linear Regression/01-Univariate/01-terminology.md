## Linear Regression
 
**Linear Regression** = drawing a straight line that is as close as possible to all the data points, using **least squares** across all datapoints.
 
### Example dataset: House prices
 
| House (sqft) | Price ($1000s) |
|--------------|-----------------|
| 2104         | 400             |
| 1416         | 232             |
| ...          | ...             |
| 3210         | 870             |
 
### Terminology
 
- **Training set**: the data used to train the model.
### Notation
 
- $x$ → **input variable** / **feature**
- $y$ → **output** / **target variable**
- $(x, y)$ → a **single training example** (one row of data)
- $(x^{(i)}, y^{(i)})$ → the **i-th training example** — i.e., a specific row in the dataset
### The flow: how a model works
 
```
training set (features + target)
        ↓
  learning algorithm
        ↓
  x  →  [ f ]  →  ŷ  (y-hat)
      function     prediction
```
 
- **Input** → **feature**
- $f$ → the **function** / **model**
- $\hat{y}$ (y-hat) → the **prediction**, the model's guess for $y$, given $x$
Note the difference: $y$ is the **actual** answer in our training data, while $\hat{y}$ is what the **model predicts**. They may not be the same and that gap is exactly what we'll measure next with the cost function.
 
