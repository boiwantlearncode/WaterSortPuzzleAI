import heapq

def a_star_solve(puzzle):
    # Initialize priority queue
    priority_queue = []
    
    # Start state ID and corresponding values
    start_state_id = 0
    start_gn = 0
    start_fn = start_gn + puzzle.heuristic()
    
    # Push initial state into priority queue
    heapq.heappush(priority_queue, (start_fn, start_state_id, puzzle, [], start_gn))
    
    # Set to store seen states
    seen = set([tuple(tuple(tube) for tube in puzzle.tubes)])
    
    # Initialize state ID
    state_id = 1

    # Main loop
    while priority_queue:
        # Pop state with lowest f(n) value
        fn, _, current_puzzle, path, gn = heapq.heappop(priority_queue)
        
        # Check if puzzle is solved
        if current_puzzle.is_solved():
            return path, current_puzzle
        
        # Generate possible moves and explore
        for move in current_puzzle.get_possible_moves():
            next_state = current_puzzle.execute_move(*move)
            next_state_tuple = tuple(tuple(tube) for tube in next_state.tubes)
            
            # Check if next state is seen before
            if next_state_tuple not in seen:
                seen.add(next_state_tuple)
                
                # Calculate next g(n) and f(n) values
                next_gn = gn + 1
                next_fn = next_gn + next_state.heuristic()
                
                # Push next state into priority queue
                heapq.heappush(priority_queue, (next_fn, state_id, next_state, path + [move], next_gn))
                state_id += 1
                
    # If no solution found
    return None, None
