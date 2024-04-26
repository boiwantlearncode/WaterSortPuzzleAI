def dfs_solve(puzzle, path=[], seen=None):    
    # Initialize the set of seen states if not provided
    if seen is None:
        seen = set()    
        
    # Convert the current puzzle state to a hashable tuple
    state_tuple = tuple(tuple(tube) for tube in puzzle.tubes)

    # Check if this state has already been visited
    if state_tuple in seen:
        return None
    
    # Mark this state as visited
    seen.add(state_tuple)  

    # Check if the puzzle is already solved
    if puzzle.is_solved():
        return path, puzzle
    
    # Iterate through possible moves
    for move in puzzle.get_possible_moves():        
        # Execute the move to get the next state
        next_state = puzzle.execute_move(*move)
        
        # Recursively call dfs_solve with the next state
        result = dfs_solve(next_state, path + [move], seen)        
        
        # If a solution is found, return the result
        if result:
            return result    
    
    # If no solution is found, backtrack by removing the current state
    seen.remove(state_tuple)  
    
    # Return None if no solution is found
    return None
