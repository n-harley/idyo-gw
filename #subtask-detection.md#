---
layout: page
title: Sub-Task Detection
---

- The last element of the sequence representing the sub-task 'pickup key' represents a state in which the previous action is 'pickup', the agent's position is unchanged, and the key is no longer visible.
- The objective is to identify this boundary element between the sub-tasks using only the probabilities given by the model.

We assume that:
1. The information content of the boundary element will be low.
2. The information content of the element after the boundary element (i.e. the first element of the next sub-task) will be high. 
3. The entropy at the boundary element will be high. 
4. The entropy just before the boundary element will be low. 
5. The information gain (the KL divergence between the predictive distribution before and after the element is processed) will be ... 

information gain as the KL divergence between the predictive distribution before and after a note is processed

We consider the following detection methods:

- `min_ic`: minimum information content
- `min_h`: minimum entropy
- `max_ic_diff`: maximum increase in information content
- `max_ic_diff_minus1`: one position before the maximum increase in information content
- `max_h_diff`: maximum increase in entropy
- `max_h_diff_minus1`: one position before the maximum increase in entropy

- `max_ig_diff`: maximum information gain
- `max_ig_diff_minus1`: one position before the maximum increase in information gain
- `max_h_ic`: the maximum of entropy divided by information content
- `max_ig_ic`: the maximum of information gain divided by information content

