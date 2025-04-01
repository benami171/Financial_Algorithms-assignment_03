# Competitive Equilibrium Solver

This repository contains a Python implementation to compute the competitive equilibrium allocation and prices in a Fisher market setting. In these markets, agents (people) with given budgets purchase divisible resources (goods) with specified supplies and valuations. The equilibrium is computed by solving a convex optimization problem using the Eisenberg–Gale formulation.

## Overview

The code defines two main functions:

- **competitive_equilibrium:**  
  This function takes as input:
  - A 2D NumPy array `valuations` of shape (n, m), where `valuations[i][j]` is the value that person *i* assigns to resource *j*.
  - A 1D NumPy array `budgets` of length *n* that specifies each person's budget.
  - A 1D NumPy array `supply` of length *m* that specifies the total available units for each resource.
  
  It solves a convex optimization problem that maximizes the sum of the weighted logarithms of the agents' utilities (where utility is defined as the sum of the allocated amounts weighted by the corresponding valuations). The dual variables of the resource constraints give the equilibrium prices.

- **print_equilibrium:**  
  This function nicely prints the equilibrium allocation and resource prices. It formats the output so that each row corresponds to a person’s allocation, and it displays the price for each resource.

## Results

```python
Equilibrium allocation EXAMPLE 1:
+----------+--------------+--------------+--------------+
|   Person |   Resource 0 |   Resource 1 |   Resource 2 |
+==========+==============+==============+==============+
|        0 |            1 |          0.3 |            0 |
+----------+--------------+--------------+--------------+
|        1 |            0 |          0.7 |            1 |
+----------+--------------+--------------+--------------+

Equilibrium prices EXAMPLE 1 :
+------------+---------+
|   Resource |   Price |
+============+=========+
|          0 | 52.1741 |
+------------+---------+
|          1 | 26.0869 |
+------------+---------+
|          2 | 21.7389 |
+------------+---------+

--------------------------------------------------

Equilibrium allocation EXAMPLE 2:
+----------+--------------+--------------+
|   Person |   Resource 0 |   Resource 1 |
+==========+==============+==============+
|        0 |          0.5 |          0.1 |
+----------+--------------+--------------+
|        1 |          0.5 |          0.1 |
+----------+--------------+--------------+
|        2 |          0   |          0.8 |
+----------+--------------+--------------+

Equilibrium prices EXAMPLE 2 :
+------------+---------+
|   Resource |   Price |
+============+=========+
|          0 | 49.9998 |
+------------+---------+
|          1 | 49.9999 |
+------------+---------+

--------------------------------------------------

Equilibrium allocation EXAMPLE 3:
+----------+--------------+--------------+--------------+
|   Person |   Resource 0 |   Resource 1 |   Resource 2 |
+==========+==============+==============+==============+
|        0 |       1.0001 |            0 |            0 |
+----------+--------------+--------------+--------------+
|        1 |       0      |            1 |            0 |
+----------+--------------+--------------+--------------+
|        2 |       0      |            0 |            1 |
+----------+--------------+--------------+--------------+

Equilibrium prices EXAMPLE 3 :
+------------+---------+
|   Resource |   Price |
+============+=========+
|          0 | 49.9936 |
+------------+---------+
|          1 | 30.0005 |
+------------+---------+
|          2 | 19.9989 |
+------------+---------+

--------------------------------------------------

Equilibrium allocation EXAMPLE 4:
+----------+--------------+--------------+--------------+
|   Person |   Resource 0 |   Resource 1 |   Resource 2 |
+==========+==============+==============+==============+
|        0 |         0.75 |         0    |         0    |
+----------+--------------+--------------+--------------+
|        1 |         0    |         0.75 |         0    |
+----------+--------------+--------------+--------------+
|        2 |         0    |         0    |         0.75 |
+----------+--------------+--------------+--------------+
|        3 |         0.25 |         0.25 |         0.25 |
+----------+--------------+--------------+--------------+

Equilibrium prices EXAMPLE 4 :
+------------+---------+
|   Resource |   Price |
+============+=========+
|          0 | 53.3334 |
+------------+---------+
|          1 | 53.3335 |
+------------+---------+
|          2 | 53.3335 |
+------------+---------+

--------------------------------------------------

Equilibrium allocation EXAMPLE 5:
+----------+--------------+--------------+
|   Person |   Resource 0 |   Resource 1 |
+==========+==============+==============+
|        0 |          1.6 |            0 |
+----------+--------------+--------------+
|        1 |          0.4 |            1 |
+----------+--------------+--------------+

Equilibrium prices EXAMPLE 5 :
+------------+---------+
|   Resource |   Price |
+============+=========+
|          0 | 31.2501 |
+------------+---------+
|          1 | 37.5001 |
+------------+---------+

--------------------------------------------------
```


## Can llm solve these examples ? 
- Yes! and it can do it actually very well.
**You can see [here](https://chatgpt.com/share/67ec0ace-42b8-8004-a939-10ff1721c27a) o3-mini's answers.**

## Prerequisites

The code requires the following Python packages:
- [NumPy](https://numpy.org/)
- [CVXPY](https://www.cvxpy.org/)

Install them using pip if you haven't already:

```bash
pip install numpy cvxpy
