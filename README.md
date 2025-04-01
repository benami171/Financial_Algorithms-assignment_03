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


## Can llm solve these examples ? 
- if so, what is the algorithm it uses ?
- Does it gives good answers ? 
- **You can see here the results of o3-mini** [conversation](https://chatgpt.com/share/67ec0ace-42b8-8004-a939-10ff1721c27a)

## Prerequisites

The code requires the following Python packages:
- [NumPy](https://numpy.org/)
- [CVXPY](https://www.cvxpy.org/)

Install them using pip if you haven't already:

```bash
pip install numpy cvxpy
