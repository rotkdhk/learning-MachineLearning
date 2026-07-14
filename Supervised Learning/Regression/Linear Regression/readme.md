As learnt in the previous section, we can make predictions using a straight line equation y = wx + b. But in the real world, data is messy, there's no proper straight line connecting the data points exactly.
 
Let's say we have datapoints as follows:
 
<img width="563" height="432" alt="image" src="https://github.com/user-attachments/assets/02241b9d-bc19-44a9-bf5c-73b5b7af0870" />

If we connect these datapoints directly, the result is not a straight line, there's no proper way of telling what's happening here to predict a new outcome:
 
<img width="563" height="432" alt="image" src="https://github.com/user-attachments/assets/a1f880ef-e1af-40f7-8309-22a88081e311" />

That's where **error** comes in. We need a straight line that stays as close as possible to all the data points, even if it can't touch every single one exactly. The red line below is far from most datapoints, while the green line stays near most of them:
 
<img width="562" height="432" alt="image" src="https://github.com/user-attachments/assets/0b040e17-e56f-4044-bd14-4ddeb8bbde7b" />

### What is Error?
 
**Error** is the gap between what actually happened and what our line predicted:
 
```
error = actual value − predicted value
```
 
Each blue dot below is a real datapoint. Each green X is where the line predicts that point should be. The red dashed line is the error at that point:
 
<img width="1050" height="750" alt="image" src="https://github.com/user-attachments/assets/fcccfe09-cd73-440d-812d-c231ed7bb3dd" />

Notice the errors aren't all the same sign, if the actual point is **above** the line, the error is **positive**; if it's **below**, the error is **negative**.

*In machine learning, perfection isn't the goal, minimizing the error is.*
 
---
 
> Going forward, let's understand how we can find that best-fit line.
