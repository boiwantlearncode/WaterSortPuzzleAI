def dls_solve(puzzle, limit, path=[], seen=None, depth=0):
    # Initialize the set of seen states if not provided
    if seen is None:
        seen = set()
    
    # Convert the current puzzle state into a hashable tuple
    state_tuple = tuple(tuple(tube) for tube in puzzle.tubes)
    
    # If the current state has been seen before or depth exceeds limit, stop recursion
    if state_tuple in seen or depth > limit:
        return None
    
    # Add the current state to the set of seen states
    seen.add(state_tuple)
    
    # If the puzzle is already solved, return the path and puzzle
    if puzzle.is_solved():
        return path, puzzle
    
    # Explore possible moves from the current state
    for move in puzzle.get_possible_moves():
        # Execute a move and get the next state
        next_state = puzzle.execute_move(*move)
        
        # Recursively call dls_solve with updated parameters
        result = dls_solve(next_state, limit, path + [move], seen, depth + 1)
        
        # If a solution is found, return the result
        if result:
            return result
    
    # If no solution is found at this depth, return None
    return None
