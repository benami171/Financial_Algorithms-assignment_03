import numpy as np
import cvxpy as cp

def competitive_equilibrium(valuations, budgets, supply):
    """
    Computes the competitive equilibrium allocation and prices for a Fisher market.

    Parameters:
        valuations (np.ndarray): A 2D array of shape (n, m) where valuations[i][j] is the value that person i 
                                 has for resource j. (Assumed strictly positive.)
        budgets (np.ndarray): A 1D array of length n representing the budget for each person.
        supply (np.ndarray): A 1D array of length m representing the supply for each resource.

    Returns:
        allocation (np.ndarray): A 2D array of shape (n, m) representing the equilibrium allocation x[i][j].
        prices (np.ndarray): A 1D array of length m representing the equilibrium prices for each resource.
    """
    n, m = valuations.shape

    # Define the allocation variables: x[i][j] >= 0 represents allocation of resource j to person i.
    x = cp.Variable((n, m), nonneg=True)
    
    # Each person’s utility is the sum of the allocated amounts weighted by their valuations.
    utilities = cp.sum(cp.multiply(valuations, x), axis=1)
    
    # Maximize sum_i (B_i * log(utility_i))
    objective = cp.Maximize(cp.sum(cp.multiply(budgets, cp.log(utilities))))
    
    # Resource constraints: total allocation for each resource j must be <= its supply.
    constraints = [cp.sum(x, axis=0) <= supply] # this function works like this: sum(x[i][j] for i in range(n)) <= supply[j]
    
    # Solve the convex program
    problem = cp.Problem(objective, constraints)
    problem.solve(solver=cp.SCS)
    
    # Retrieve the equilibrium allocation and the dual variables (prices).
    allocation = x.value
    prices = constraints[0].dual_value  # Dual variables correspond to resource prices.
    
    return allocation, prices


def print_equilibrium(allocation, prices, example_label=""):
    """
    Prints a nicely formatted equilibrium allocation and prices.

    Parameters:
        allocation (np.ndarray): 2D array where each row corresponds to a person.
        prices (np.ndarray): 1D array of resource prices.
        example_label (str): Example label to display (e.g., "EXAMPLE 2").
    """
    # Print header for allocation.
    header_title = f"Equilibrium allocation {example_label} (each row corresponds to a person):"
    print(header_title)
    num_people, num_resources = allocation.shape

    # Print header row.
    header = "Person".ljust(10) + "".join([f"Resource {j}".rjust(15) for j in range(num_resources)])
    print(header)
    print("-" * len(header))

    # Print each person's allocation with four decimal places.
    for i in range(num_people):
        row_str = f"{i}".ljust(10)
        for j in range(num_resources):
            row_str += f"{allocation[i, j]:15.4f}"
        print(row_str)

    # Print equilibrium prices.
    price_header_title = f"\nEquilibrium prices {example_label} (for each resource):"
    print(price_header_title)
    price_header = "Resource".ljust(10) + "Price".rjust(15)
    print(price_header)
    print("-" * len(price_header))
    for j, price in enumerate(prices):
        print(f"{j}".ljust(10) + f"{price:15.4f}")

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
