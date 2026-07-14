> In general, **Machine Learning** is when a computer learns patterns from data to make predictions and improves its accuracy over time — without being given fixed rules.

## So, what is "learning" here?

We humans have a brain to understand things. But a computer only understands 0s and 1s, so how does it "learn"? That's where mathematics comes in. Concepts like algebra, derivatives, and Euclidean distance are what make learning actually work. We'll understand how, as we go further.

lets understand how ML works in general with 2 examples.

## Example 1: Email Spam Filter

In Gmail, or any other mail service, we can see spam filtering at work. How does it work? Are there any fixed rules? No — it's all about the data we have.

- Let's say we have 1000 emails and we manually label each one as spam or not, by comparing various factors (called **features** in ML) like unknown sender, grammar mistakes, urgency, and so on.
- For each feature we assign a number (0, 1, 2, 3...) and note the final outcome as **spam** or **not spam**.

Now, with this data, let's understand how the computer can decide whether an email is spam or not.

| Email # | 'Urgent' word | Unknown sender | Label |
|---------|---------------|----------------|-------|
| e1      | 5             | 1              | SPAM |
| e2      | 0             | 0              | NOT SPAM |

Now a new email arrives:

| Email # | 'Urgent' word | Unknown sender |
|---------|---------------|----------------|
| ne1     | 4             | 1              |

### How does the computer decide? → Distance
 
The computer measures how **close** the new email is to each known email. Closer = more similar.
 
To measure closeness between two points, we use the **distance formula** (Euclidean distance):
 
`distance = √( (x2 − x1)² + (y2 − y1)² )`
 
Here:
- x = 'Urgent' word count
- y = Unknown sender
Our new email **ne1** = (4, 1). Let's find its distance to each known email.
 
**Distance from ne1 (4, 1) to e1 (5, 1):**
 
```
d = √( (5 − 4)² + (1 − 1)² )
  = √( (1)²   + (0)²   )
  = √( 1 + 0 )
  = √1
  = 1
```
 
**Distance from ne1 (4, 1) to e2 (0, 0):**
 
```
d = √( (0 − 4)² + (0 − 1)² )
  = √( (−4)²   + (−1)²   )
  = √( 16 + 1 )
  = √17
  ≈ 4.12
```
 
**Result:**
 
| Compared to | Distance |
|-------------|----------|
| e1 (SPAM)     | 1.00 |
| e2 (NOT SPAM) | 4.12 |
 
ne1 is much closer to **e1** (distance 1) than to e2 (distance 4.12).
Since e1 is SPAM, the computer predicts **ne1 = SPAM**.

## Example 2: Grouping People (no labels!)
 
Now let's say we have data like this, just some people with their height and weight. But notice one thing: there's **no label** like we had in the spam filter (no spam / not spam). Just raw data.
 
| Person | Height (cm) | Weight (kg) |
|--------|-------------|-------------|
| A      | 150         | 50          |
| B      | 152         | 52          |
| C      | 180         | 90          |
| D      | 182         | 88          |
 
So the question is, without any label telling the answer, how can the computer group these people?
 
And guess what, the trick is the same **distance** math we used before. The computer just checks who is close to whom. Close people = same group.
 
`distance = √( (h2 − h1)² + (w2 − w1)² )`
 
**A (150, 50) to B (152, 52):**
 
```
d = √( (152−150)² + (52−50)² )
  = √( 2² + 2² )
  = √( 4 + 4 )
  = √8
  ≈ 2.83   → very close
```
 
**A (150, 50) to C (180, 90):**
 
```
d = √( (180−150)² + (90−50)² )
  = √( 30² + 40² )
  = √( 900 + 1600 )
  = √2500
  = 50      → very far
```
 
**C (180, 90) to D (182, 88):**
 
```
d = √( (182−180)² + (88−90)² )
  = √( 2² + (−2)² )
  = √8
  ≈ 2.83   → very close
```
 
Now just look at the numbers:
- A ↔ B ≈ 2.83 (tiny)
- C ↔ D ≈ 2.83 (tiny)
- A ↔ C = 50 (huge)
So the computer doesn't need any label. The numbers itself tell us there are 2 natural groups:
 
| Group | People | Roughly |
|-------|--------|---------|
| Group 1 | A, B | shorter & lighter |
| Group 2 | C, D | taller & heavier |
 
That's the whole idea, **small distance = same group, big distance = different group**. The computer finds the groups just from the math, nobody told it the answer.

---

**Example 1:** Where we already have a dataset with the outcome (label), and we use it to predict for new data — this is called **Supervised Learning**.

**Example 2:** Where we don't have any labels, and instead the computer groups similar things on its own — this is called **Unsupervised Learning**.

