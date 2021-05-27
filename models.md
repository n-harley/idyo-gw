---
layout: page
title: Models
---

Each model gives the distribution of next ACTIONs by combining the distributions resulting from multiple other variable-order models for different combinations of features. The expression run to construct each model is given below. Details of the parameters to IDYoM can be found [here](https://github.com/mtpearce/idyom/wiki/IDyOM-Parameters). `select-maxlinksN` means the system automatically selected the best combination of features by a hill climbing algorithm to minimise mean information content. 

## idyom-action-action

```
(idyom:idyom 33 '(action) '(action))
```
Mean IC: 1.6158307.

## idyom-action-action-stmo1-ltmo1

This model was constructed using the following command:
```
(idyom:idyom 33 '(action) '(action) :stmo '(:order-bound 1) :ltmo '(:order-bound 1))
```
The order of the model is limited to 1, i.e. bigrams. 
Mean IC: 1.9552814.

## idyom-select-maxlinks2

```
(idyom:idyom 33 '(action) :select :basis '(action orientation agentinfront agentbehind agentleft agentright agentx agenty agentquad keyquad doorquad agentinfrontleft agentinfrontright agentbehindleft agentbehindright canseedoor canseekey distance) :max-links 2)
```
The system automatically selects the best set of features including binary combinations. The set of features selected by the program was as follows:

- `(ACTION AGENTINFRONT)`
- `(ACTION AGENTRIGHT)`
- `(ACTION AGENTLEFT)`
- `(ACTION AGENTINFRONTLEFT)`
- `(ACTION AGENTINFRONTRIGHT)` 
- `(ACTION CANSEEDOOR)`
- `(ACTION DISTANCE)`

Mean IC: 0.7807406.

## idyom-select-maxlinks2-plus

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)))
```
This model uses same features as [idyom-select-maxlinks2](#idyom-select-maxlinks2) but with the addition of `(ACTION CANSEEKEY)`. 

Mean IC: 0.7917453.

## idyom-select-maxlinks3

```
(idyom:idyom 33 '(action) :select :basis '(action orientation agentinfront agentbehind agentleft agentright agentx agenty agentquad keyquad doorquad agentinfrontleft agentinfrontright agentbehindleft agentbehindright canseedoor canseekey distance) :max-links 3)
```
The system automatically selects the best set of features including binary and ternary combinations. The set of features selected by the program was as follows:
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

Mean IC: 0.6769469.

## idyom-select-maxlinks3-plus

```
(idyom:idyom 33 '(action) ((action canseedoor)(action canseedoor canseekey)(action agentleft canseekey)(action agentleft canseedoor)(action agentright canseekey)(action agentright canseedoor)(action agentinfront canseekey)(action agentinfront canseedoor)(action agentinfront agentleft)(action agentinfront agentright)(action agentinfrontright distance)(action agentinfrontright canseedoor)(action agentinfrontleft distance)(action agentinfrontleft canseedoor)(action agentinfrontleft canseekey)(action agentinfrontright canseekey)(action agentquad keyquad)))
```
This model uses same features as [idyom-select-maxlinks3](#idyom-select-maxlinks3) but with the addition of all feature combinations which are the symmetrical counterparts of those selected e.g. `(ACTION AGENTINFRONTRIGHT CANSEEKEY)`.

Mean IC: 0.67931646

## idyom-select-maxlinks3-minus
```
(idyom:idyom 33 '(action) '((action canseedoor)(action canseedoor canseekey)(action agentleft canseekey)(action agentleft canseedoor)(action agentright canseekey)(action agentright canseedoor)(action agentinfront canseekey)(action agentinfront canseedoor)(action agentinfront agentleft)(action agentinfront agentright)(action agentquad keyquad)))
```
This model uses same features as [idyom-select-maxlinks3](#idyom-select-maxlinks3) but without all the feature combinations whose symmetrical counterparts are absent e.g. `(ACTION AGENTINFRONTLEFT CANSEEKEY)`.

Mean IC: 0.68368334

## idyom-action-action-stmo1
```
(idyom:idyom 33 '(action) '(action) :stmo '(:order-bound 1))
```
The bound of the short term model is restricted to 1. 

Mean IC: 1.6254971

## idyom-select-maxlinks2-plus-stmo1

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :stmo '(:order-bound 1))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but restricts the order of the short term model to 1. 

Mean IC: 0.7924194

## idyom-select-maxlinks2-plus-stmo1-ltmo1

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :stmo '(:order-bound 1) :ltmo '(:order-bound 1))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but restricts the order of both the short term and long term models to 1. 

Mean IC: 1.0009514

## idyom-select-maxlinks2-plus-ltm
```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm)
```
Mean IC: 0.7965729

## idyom-select-maxlinks2-plus-ltm-ltmo1

```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm :ltmo '(:order-bound 1))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but uses only the long term model with order restricted to 1. 

Mean IC: 0.98026925

## idyom-select-maxlinks2-plus-ltm-ltmo2
```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm :ltmo '(:order-bound 2))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but uses only the long term model with order restricted to 2.

Mean IC: 0.9034804

## idyom-select-maxlinks2-plus-ltm-ltmo3
```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm :ltmo '(:order-bound 3))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but uses only the long term model with order restricted to 3.

Mean IC: 0.8771507

## idyom-select-maxlinks2-plus-ltm-ltmo4
```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm :ltmo '(:order-bound 4))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but uses only the long term model with order restricted to 4.

Mean IC: 0.8619554

## idyom-select-maxlinks2-plus-ltm-ltmo5
```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm :ltmo '(:order-bound 5))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but uses only the long term model with order restricted to 5.

Mean IC: 0.85403854

## idyom-select-maxlinks2-plus-ltm-ltmo6
```
(idyom:idyom 33 '(action) '((action agentinfront)(action agentright)(action agentleft)(action agentinfrontleft)(action agentinfrontleft)(action canseedoor)(action canseekey)(action distance)) :models :ltm :ltmo '(:order-bound 6))
```
This model uses the same features as [idyom-select-maxlinks2-plus](#idyom-select-maxlinks2-plus) but uses only the long term model with order restricted to 6. 

Mean IC: 0.8451378

