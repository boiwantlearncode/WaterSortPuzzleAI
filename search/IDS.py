from search.DLS import dls_solve

def ids_solve(puzzle, max_depth=1000):
    """
    Iterative Deepening Search (IDS) algorithm to find a solution for a given puzzle.
    
    Args:
        puzzle: The puzzle to be solved.
        max_depth (int): The maximum depth to search. Defaults to 1000.
        
    Returns:
        result: A tuple containing the solution (if found) and the depth at which it was found.
                If no solution is found within the maximum depth, returns (None, None).
    """
    # Iterate through depths from 0 to max_depth
    for depth in range(max_depth):
        # Attempt to solve the puzzle using Depth-Limited Search (DLS) with current depth
        result = dls_solve(puzzle, depth)
        
        # If a solution is found at this depth, return it
        if result:
            return result  # Return solution and depth
        
    # If no solution is found within the maximum depth, return None
    return None, None
