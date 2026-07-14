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
