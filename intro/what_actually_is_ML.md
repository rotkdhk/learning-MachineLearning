> In general, **Machine Learning** is when a computer learns patterns from data to make predictions and improves its accuracy over time — without being given fixed rules.

## So, what is "learning" here?

We humans have a brain to understand things. But a computer only understands 0s and 1s, so how does it "learn"? That's where mathematics comes in. Concepts like algebra, derivatives, and Euclidean distance are what make learning actually work. We'll understand how, as we go further.

lets understand how ML works in general with 2 examples.

### Example 1: Email Spam Filter

In GMAIL or any other mailing services we can see the spam filtering how it work? any fixed rules?. No, its all about data we have.
- Let's say we have 1000 mails and we manually labelled if its spam or not by comparing various factors (aka features in ML) like unknowns sender, grammar mistakes, urgency, etc...
- For each feature we gave some number 0,1,2,3... and the mention final outcome as **spam** or **not spam**.

Now with this data let's understand how computer can define if its spam or not
| Email# | 'Urgent' word | unknown sender | label |
|-------|-------|-------|-------|
| e1   | 5     | 1    | SPAM    |
| e2   | 0    | 0    | NOT SPAM    |

Now we have new email
| Email# | 'Urgent' word  | unknown sender |
|-------|-------|-------|
| ne1   | 4     | 1     |



