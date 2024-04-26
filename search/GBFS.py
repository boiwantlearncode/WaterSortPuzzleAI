import heapq

def gbfs_solve(puzzle):
    # Initialize priority queue to store states, initialize state_id for unique identification,
    # and push initial state into the priority queue
    priority_queue = []
    state_id = 0  # Unique identifier for each state to prevent comparison issues
    heapq.heappush(priority_queue, (puzzle.heuristic(), state_id, puzzle, []))  # Add state_id as a tie-breaker
    seen = set([tuple(tuple(tube) for tube in puzzle.tubes)])  # Set to store seen states
    state_id += 1

    # Main loop to explore states until the goal is reached or no more states to explore
    while priority_queue:
        # Pop the state with the highest priority from the priority queue
        _, _, current_puzzle, path = heapq.heappop(priority_queue)
        # Check if the puzzle is solved
        if current_puzzle.is_solved():
            # Return the solution path and the solved puzzle
            return path, current_puzzle
        
        # Explore possible moves from the current state
        for move in current_puzzle.get_possible_moves():
            # Execute the move to generate the next state
            next_state = current_puzzle.execute_move(*move)
            # Convert the next state into a hashable tuple for efficient lookup
            state_tuple = tuple(tuple(tube) for tube in next_state.tubes)
            # Check if the next state has been seen before
            if state_tuple not in seen:
                # If the next state is new, add it to the set of seen states
                seen.add(state_tuple)
                # Push the next state into the priority queue with its heuristic value,
                # state_id, the next state, and the path taken so far
                heapq.heappush(priority_queue, (next_state.heuristic(), state_id, next_state, path + [move]))
                # Increment the state_id for the next state
                state_id += 1
    
    # If no solution is found, return None for both path and puzzle
    return None, None
