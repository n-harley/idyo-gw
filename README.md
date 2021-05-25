
# IDyOG: The Information Dynamics of Gridworld

#### Statistical modelling of agent behavior in minimalistic gridworld environments.  

<https://n-harley.github.io/idyog>

## Introduction

- Partial observability, dynamic environments, hidden rewards and explainability are problems for RL models. 
- Supervised learning incorporating relevant knowledge about sub-tasks can mitigate these problems.
- The goal of this work is to learn the relevant knowledge in an unsupervised manner.
- We focus on minimalistic gridworld environments (<https://github.com/maximecb/gym-minigrid>).
- We use an unsupervised learning algorithm called IDyOM (<http://mtpearce.github.io/idyom/>).
- The algorithm constructs statistical models of patterns in agent behavior data.
- We use these models to find the boundaries between sub-tasks.

## Scenario

We consider a highly simplified scenario in which a gridworld agent must open a door by first picking up a key. The task here is 'open door'. The (implicit) sub-tasks are 'pickup key' and 'unlock door'. Our aim is to identify the boundary between these sub-tasks.

## Data Set

The [data set](dataset.pkl) contains 1000 example missions recording the agent behavior undertaken to successfully 'open door'. Each example mission begins with a random configuration of agent, key and door. [This](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/dataset-explorer.ipynb) notebook explores the data set. 

## Representation

We represent each example mission as a sequence of objects. Each object represents the state of the gridworld at that point in the mission, as well as the action performed immediately prior to entering that state. Objects consist of a collection of feature values. These features capture abstract information about the grid from both bird's-eye and first-person perspectives. Details of the representation are described [here](./representation.md).

## Statistical Modelling

The features are used to construct statistical models of the object sequences. These models are constructed using IDyOM (<http://mtpearce.github.io/idyom/>). IDyOM is a multiple viewpoint system for capturing statistical patterns in multi-dimensional data. (It was originally applied to musical. However, the basic principle are applicable to any sequence.) We use a variety of models constructed by running IDyOM with different parameters. The models are described [here](./models.md). [This](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/model-explorer.ipynb) notebook explores the models.

## Sub-Task Boundary Detection

The models give the information content of each object in a sequence (the degree to which it was unexpected), as well as the entropy at each point in the mission (the uncertainty of what comes next). Information content and entropy are used to define a variety of boundary strength profiles. By looking for peaks in these profiles, we can estimate the location of the sub-task boundary between 'pickup key' and 'open door'. We explore a variety of different boundary strength profiles and peak picking estimators, described [here](./subtask-detection.md)

## Results 

We calculate the numbers of correctly identified subtask boundaries for each model and each estimator. The results table is available [here](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/subtask-detection.ipynb).

~75% of the subtask boundaries were correctly identified by using the model [idyom-select-maxlinks2-plus](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks2-plus.ipynb) and the estimator `max_ig_ic`.

## Further Work

