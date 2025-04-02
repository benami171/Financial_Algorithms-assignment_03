# Competitive Equilibrium Solver

This repository contains a Python implementation to compute the competitive equilibrium allocation and prices in a Fisher market setting. In these markets, agents (people) with given budgets purchase divisible resources (goods) with specified supplies and valuations. The equilibrium is computed by solving a convex optimization problem using the Eisenberg–Gale formulation.

---

## Overview

The code defines two main functions:

### 1. `competitive_equilibrium`

- **Inputs:**
  - A 2D NumPy array `valuations` (shape **n × m**), where `valuations[i][j]` represents the value that person *i* assigns to resource *j*.
  - A 1D NumPy array `budgets` of length **n**, representing each agent's budget.
  - A 1D NumPy array `supply` of length **m**, outlining the total available units for each resource.

- **What It Does:**
  - Solves a convex optimization problem that maximizes the sum of the weighted logarithms of agent utilities.  
    (Each agent's utility is defined as the sum of allocated amounts, weighted by their valuations.)
  - The **dual variables** of the resource constraints are interpreted as the equilibrium prices.


### 2. `print_equilibrium`

- **What It Does:**
  - Neatly prints the equilibrium allocation and resource prices in formatted tables.
  - Each row represents a person’s allocation, and each resource's equilibrium price is displayed in its own column.

---

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

---

## LLM Capabilities

Yes, an LLM can solve these examples effectively!  
For more details, see [o3-mini's answers **Here**](https://chatgpt.com/share/67ec0ace-42b8-8004-a939-10ff1721c27a).

---

## Prerequisites

The code requires the following Python packages:
- [NumPy](https://numpy.org/)
- [CVXPY](https://www.cvxpy.org/)

Install them using pip if you haven't already:

```bash
pip install numpy cvxpy
