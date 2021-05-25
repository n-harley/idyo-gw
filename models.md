---
layout: page
title: Models
---

## idyom-action-action

This model was constructed using the following command:
```
(idyom:idyom 33 '(action) '(action))
```

The resulting model predicts the next `ACTION` from sequences of previous `ACTIONS`s. 

The mean information content of the model is 1.6158307.

## idyom-action-action-stmo1-ltmo1

This model was constructed using the following command:
```
(idyom:idyom 33 '(action) '(action) :stmo '(:order-bound 1) :ltmo '(:order-bound 1))
```

The resulting model predicts the next `ACTION` from the previous `ACTIONS`s. 

The mean information content of the model is 1.9552814.

## idyom-select-maxlinks2

This model was constructed by running the following command:

```
(idyom:idyom 33 '(action) :select :basis '(action orientation agentinfront agentbehind agentleft agentright agentx agenty agentquad keyquad doorquad agentinfrontleft agentinfrontright agentbehindleft agentbehindright canseedoor canseekey distance) :max-links 2)
```

The program considers viewpoints from the basis set as well as binary and ternary linked combination. It searches for the combination of these viewpoints which gives the most compact model. That is, is tries to minimise the mean information content by a simple hill-climbing algorithm.

The set of viewpoints selected by the program was as follows:

- `(ACTION AGENTINFRONT)`
- `(ACTION AGENTRIGHT)`
- `(ACTION AGENTLEFT)`
- `(ACTION AGENTINFRONTLEFT)`
- `(ACTION AGENTINFRONTRIGHT)` 
- `(ACTION CANSEEDOOR)`
- `(ACTION DISTANCE)`

The mean information content of the resulting model is 0.7807406.

## idyom-select-maxlinks2-plus

Idyom was run on the gridwold data using the following command:

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)))
```

The model predicts the next `ACTION` from the following set of viewpoints:

- `(ACTION AGENTINFRONT)`
- `(ACTION AGENTRIGHT)`
- `(ACTION AGENTLEFT)`
- `(ACTION AGENTINFRONTLEFT)`
- `(ACTION AGENTINFRONTRIGHT)` 
- `(ACTION CANSEEDOOR)`
- `(ACTION CANSEEKEY)`
- `(ACTION DISTANCE)`

These are the viewpoints selected in [idyom-select-maxlinks2](./idyom-select-maxlinks2.ipynb) the first-person viewpoint `CANSEEKEY`. 

The mean information content of the resulting model is 0.7917453.

## idyom-select-maxlinks3

This model was constructed by running the following command:

```
(idyom:idyom 33 '(action) :select :basis '(action orientation agentinfront agentbehind agentleft agentright agentx agenty agentquad keyquad doorquad agentinfrontleft agentinfrontright agentbehindleft agentbehindright canseedoor canseekey distance) :max-links 3)
```

The program considers viewpoints from the basis set as well as binary and ternary linked combination. It searches for the combination of these viewpoints which gives the most compact model. That is, is tries to minimise the mean information content by a simple hill-climbing algorithm.

The set of viewpoints selected by the program was as follows:

- `(ACTION CANSEEDOOR)`
- `(ACTION CANSEEDOOR CANSEEKEY)`
- `(ACTION AGENTLEFT CANSEEKEY)`
- `(ACTION AGENTLEFT CANSEEDOOR)`
- `(ACTION AGENTRIGHT CANSEEKEY)`
- `(ACTION AGENTRIGHT CANSEEDOOR)`
- `(ACTION AGENTINFRONT CANSEEKEY)`
- `(ACTION AGENTINFRONT CANSEEDOOR)`
- `(ACTION AGENTINFRONT AGENTLEFT)`
- `(ACTION AGENTINFRONT AGENTRIGHT)`
- `(ACTION AGENTINFRONTRIGHT DISTANCE)`
- `(ACTION AGENTINFRONTRIGHT CANSEEDOOR)`
- `(ACTION AGENTINFRONTLEFT CANSEEKEY)`
- `(ACTION AGENTQUAD KEYQUAD)`

The mean information content of the resulting model is 0.6769469.

## idyom-select-maxlinks3-plus

This model was constructed using the following command:

```
(idyom:idyom 33 '(action) ((action canseedoor)(action canseedoor canseekey)(action agentleft canseekey)(action agentleft canseedoor)(action agentright canseekey)(action agentright canseedoor)(action agentinfront canseekey)(action agentinfront canseedoor)(action agentinfront agentleft)(action agentinfront agentright)(action agentinfrontright distance)(action agentinfrontright canseedoor)(action agentinfrontleft distance)(action agentinfrontleft canseedoor)(action agentinfrontleft canseekey)(action agentinfrontright canseekey)(action agentquad keyquad)))
```

This model predicts the next `ACTION` from the following set of viewpoints:

- `(ACTION CANSEEDOOR)`
- `(ACTION CANSEEDOOR CANSEEKEY)`
- `(ACTION AGENTLEFT CANSEEKEY)`
- `(ACTION AGENTLEFT CANSEEDOOR)`
- `(ACTION AGENTRIGHT CANSEEKEY)`
- `(ACTION AGENTRIGHT CANSEEDOOR)`
- `(ACTION AGENTINFRONT CANSEEKEY)`
- `(ACTION AGENTINFRONT CANSEEDOOR)`
- `(ACTION AGENTINFRONT AGENTLEFT)`
- `(ACTION AGENTINFRONT AGENTRIGHT)`
- `(ACTION AGENTINFRONTRIGHT DISTANCE)`
- `(ACTION AGENTINFRONTRIGHT CANSEEDOOR)`
- `(ACTION AGENTINFRONTLEFT DISTANCE)`
- `(ACTION AGENTINFRONTLEFT CANSEEDOOR)`
- `(ACTION AGENTINFRONTLEFT CANSEEKEY)`
- `(ACTION AGENTINFRONTRIGHT CANSEEKEY)`
- `(ACTION AGENTQUAD KEYQUAD)`

These are the viewpoints selected by [idyom-select-maxlinks3](./idyom-select-maxlinks3.ipynb) plus the symmetric counterparts which were not included. 

The average IC was 0.67931646

## idyom-select-maxlinks3-minus

This model constructed by running the following command:

```
(idyom:idyom 33 '(action) '((action canseedoor)(action canseedoor canseekey)(action agentleft canseekey)(action agentleft canseedoor)(action agentright canseekey)(action agentright canseedoor)(action agentinfront canseekey)(action agentinfront canseedoor)(action agentinfront agentleft)(action agentinfront agentright)(action agentquad keyquad)))
```

The model predicts the next `ACTION` from the following set of viewpoints:

- `(ACTION CANSEEDOOR)`
- `(ACTION CANSEEDOOR CANSEEKEY)`
- `(ACTION AGENTLEFT CANSEEKEY)`
- `(ACTION AGENTLEFT CANSEEDOOR)`
- `(ACTION AGENTRIGHT CANSEEKEY)`
- `(ACTION AGENTRIGHT CANSEEDOOR)`
- `(ACTION AGENTINFRONT CANSEEKEY)`
- `(ACTION AGENTINFRONT CANSEEDOOR)`
- `(ACTION AGENTINFRONT AGENTLEFT)`
- `(ACTION AGENTINFRONT AGENTRIGHT)`
- `(ACTION AGENTQUAD KEYQUAD)`

These are the viewpoints selected in [idyom-select-maxlinks3](./idyom-select-maxlinks3.ipynb) minus the ones whose symmetric counterparts were not included.

The average IC was 0.68368334

## idyom-action-action-stmo1

```
(idyom:idyom 33 '(action) '(action) :stmo '(:order-bound 1))
```
Mean IC: 1.6254971

## idyom-select-maxlinks2-plus-stmo1

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :stmo '(:order-bound 1))
```

Mean IC: 0.7924194

## idyom-select-maxlinks2-plus-stmo1-ltmo1

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :output-path "/Users/nick/Dropbox" :detail 3 :separator "," :stmo '(:order-bound 1) :ltmo '(:order-bound 1))
```

Mean IC: 1.0009514
