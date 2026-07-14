> In general, **Machine Learning** is when a computer learns patterns from data to make predictions and improves its accuracy over time — without being given fixed rules.

## So, what is "learning" here?

We humans have a brain to understand things. But a computer only understands 0s and 1s, so how does it "learn"? That's where mathematics comes in. Concepts like algebra, derivatives, and Euclidean distance are what make learning actually work. We'll understand how, as we go further.

lets understand how ML works in general with 2 examples.

### Example 1: Email Spam Filter

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
