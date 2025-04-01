import numpy as np
import cvxpy as cp
from tabulate import tabulate

def competitive_equilibrium(valuations, budgets, supply):
    """
    Parameters:
        valuations: NxM matrix where valuations[i][j] is the value that person i gave for resource j.
        budgets
        supply 

    Returns:
        allocation: NxM matrix representing the equilibrium allocation of resources to people.
        prices: array representing the equilibrium prices for each resource (In class we saw Pa,Pb,Pc). 
    """
    n, m = valuations.shape

    # Define the allocation variables: x[i][j] >= 0 represents allocation of resource j to person i.
    x = cp.Variable((n, m), nonneg=True)
    
    # Each person’s utility is the sum of the allocated amounts weighted by their valuations.
    utilities = cp.sum(cp.multiply(valuations, x), axis=1)
    
    # Maximize sum_i (B_i * log(utility_i))
    objective = cp.Maximize(cp.sum(cp.multiply(budgets, cp.log(utilities))))
    
    # Resource constraints: total allocation for each resource j must be <= its supply.
    # creating a constraint for each resource
    # what it does is sum(x[i][j] for i in range(n)) <= supply[j] for each resource j
    constraints = [cp.sum(x, axis=0) <= supply] 
    
    # Solve the program
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)
    
    # Retrieve the equilibrium allocation and the dual variables (prices).
    allocation = x.value
    prices = constraints[0].dual_value  # Dual variables correspond to resource prices.
    
    return allocation, prices


def print_equilibrium(allocation, prices, example_label=""):

    num_people, num_resources = allocation.shape
    # Prepare allocation data for tabulate
    headers = ["Person"] + [f"Resource {j}" for j in range(num_resources)]
    table = []
    for i in range(num_people):
        row = [f"{i}"] + [f"{allocation[i, j]:.4f}" for j in range(num_resources)]
        table.append(row)
    allocation_table = tabulate(table, headers=headers, tablefmt="grid")
    
    # Prepare prices data for tabulate
    price_headers = ["Resource", "Price"]
    price_table = []
    for j, price in enumerate(prices):
        price_table.append([f"{j}", f"{price:.4f}"])
    prices_table = tabulate(price_table, headers=price_headers, tablefmt="grid")
    
    # Print the tables with labels
    print(f"Equilibrium allocation {example_label}:")
    print(allocation_table)
    print("\nEquilibrium prices {0} :".format(example_label))
    print(prices_table, "\n")
    print("--------------------------------------------------\n")


if __name__ == "__main__":

    # Example 1
    valuations = np.array([[8, 4, 2],   
                           [2, 6, 5],], dtype=float)
    
    budgets = np.array([60, 40], dtype=float)
    supply = np.array([1, 1, 1], dtype=float)

    allocation, prices = competitive_equilibrium(valuations, budgets, supply)
    print_equilibrium(allocation, prices, "EXAMPLE 1")



    # Example 2
    valuations2 = np.array([[5, 5],
                            [5, 5],
                            [3, 6],], dtype=float)
    
    budgets2 = np.array([30,30,40], dtype=float)
    supply2 = np.array([1, 1], dtype=float)
    
    allocation2, prices2 = competitive_equilibrium(valuations2, budgets2, supply2)
    print_equilibrium(allocation2, prices2, "EXAMPLE 2")


    # Example 3
    valuations3 = np.array([[10, 4, 2],
                            [3, 9, 5],
                            [5, 2, 8]], dtype=float)

    budgets3 = np.array([50, 30, 20], dtype=float)  # budgets for the 3 people
    supply3 = np.array([1, 1, 1], dtype=float)         # supply of each resource

    allocation3, prices3 = competitive_equilibrium(valuations3, budgets3, supply3)
    print_equilibrium(allocation3, prices3, "EXAMPLE 3")


    # Example 4
    valuations4 = np.array([
        [6, 4, 3],    
        [3, 8, 5],    
        [5, 6, 7],    
        [4, 4, 4]     
    ], dtype=float)

    budgets4 = np.array([40, 40, 40, 40], dtype=float)  # equal budgets for all
    supply4 = np.array([1, 1, 1], dtype=float)        

    allocation4, prices4 = competitive_equilibrium(valuations4, budgets4, supply4)
    print_equilibrium(allocation4, prices4, "EXAMPLE 4")


    # Example 5
    valuations5 = np.array([
        [7, 3],   # Person 1's valuations
        [5, 6]    # Person 2's valuations
    ], dtype=float)

    budgets5 = np.array([50, 50], dtype=float)  # budgets for both people
    supply5 = np.array([2, 1], dtype=float)        # different supply: 2 units of resource 1 and 1 unit of resource 2

    allocation5, prices5 = competitive_equilibrium(valuations5, budgets5, supply5)
    print_equilibrium(allocation5, prices5, "EXAMPLE 5")
