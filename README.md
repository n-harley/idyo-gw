# IDyOG: The Information Dynamics of Gridworld

#### Statistical modelling of agent behaviour in minimalistic gridworld environments.  

<https://n-harley.github.io/idyog>

[TEST](test.md)

## Overview

This repository contains preliminary experiements investigating the use of statistical models to detect sub-task boundaries in data describing the behaviour of agents in minimalistic gridword environments.

## Introduction

- Partial observability, dynamic environments, hidden rewards and explainability are problems for RL models. 
- Supervised learning incorporating relevant knowledge can mitigate these problems.
- The goal of this work is to learn the relevant knowledge in an unsupervised manner.
- We focus on minimalistic gridworld environments (<https://github.com/maximecb/gym-minigrid>).
- We use an unsupervised learning algorithm called IDyOM (<http://mtpearce.github.io/idyom/>).
- The algorithm constructs statistical models of patterns in agent behaviour data.
- We use these models to find the boundaries between sub-tasks.

## Scenario

We consider a highly simplified scenario in which a gridworld agent must open a door by first picking up a key. The task here is 'open door'. The (implicit) sub-tasks are 'pickup key' and 'unlock door'. Our aim is to identify the boundary between the subtasks. 

## Data Set

The [data set](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/dataset.ipynb) (dataset.pkl) contains 1000 example missions recording the agent behaviour required to successfully 'open door'. Each example mission begins with a random configuration of agent, key and door. dataset.ipynb explores the content of the dataset. 

## Representation

We represent each example mission as a sequence of objects. Each object represents the state of the gridworld at that point in the mission, as well as the action performed immediately prior to entering that state. We represent gridworld states as a collection of feature values. These features capture abstract information about the grid from both bird's-eye and first-person perspectives. These features are described [here](https://github.com/n-harley/idyog/blob/main/representation.pdf).

## Statistical Modelling

The features are used to construct statistical models of the object sequences. These models are constructed using IDyOM (<http://mtpearce.github.io/idyom/>). (IDyOM is primarily intended for modelling musical sequences. However, the basic principle are more generally applicable.) We use a vairety of models constructed by running IDyOM with different parameters. The following notebooks describe each of the models and explore the results. 

- [idyom-action-action](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-action-action.ipynb)
- [idyom-select-maxlinks2](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks2.ipynb)
- [idyom-select-maxlinks2-plus](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks2-plus.ipynb)
- [idyom-select-maxlinks3](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks3.ipynb)
- [idyom-select-maxlinks3-plus](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks3-plus.ipynb)
- [idyom-select-maxlinks3-minus](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks3-minus.ipynb)
- TODO: models with a limit on the order

## Sub-Task Boundary Detection

Using the models we can compute the information content of each object in a sequence (the degree to which it was unexpected), as well as the entropy at each point in the mission (the uncertainty of what comes next). We use information content and entropy to estimate the location of the boundary between the subtasks 'pickup key' and 'open door'. We consider 10 estimators:

- `min_ic`: minimum information content
- `min_h`: minimum entropy
- `max_h_diff`: maximum increase in entropy
- `max_h_diff_minus1`: one position before the maximum increase in entropy
- `max_ic_diff`: maximum increase in information content
- `max_ic_diff_minus1`: one position before the maximum increase in information content
- `max_ig_diff`: maximum information gain
- `max_ig_diff_minus1`: one position before the maximum increase in information gain
- `max_h_ic`: the maximum of entropy divided by information content
- `max_ig_ic`: the maximum of information gain divided by information content

## Results 

We calculate the numbers of correctly identified subtask boundaries for each model and each estimator. The results tabel is available [here](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/subtask-detection.ipynb).

~75% of the subtask boundaries were correctly identified by using the model [idyom-select-maxlinks2-plus](https://nbviewer.jupyter.org/github/n-harley/idyog/blob/main/idyom-select-maxlinks2-plus.ipynb) and the estimator `max_ig_ic`.

## Further Work

