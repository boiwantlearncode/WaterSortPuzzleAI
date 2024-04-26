import heapq

def ucs_solve(puzzle):
    # Initialize priority queue to store states with their associated costs
    priority_queue = []
    # Push the initial state into the priority queue with cost 0, ID 0, empty path
    heapq.heappush(priority_queue, (0, 0, puzzle, []))  # (cost, id, puzzle, path)
    # Keep track of seen states to avoid revisiting them
    seen = set([tuple(tuple(tube) for tube in puzzle.tubes)])
    # Start counting from 1 for unique IDs for each new state
    id_counter = 1  

    # Continue searching until priority queue is empty
    while priority_queue:
        # Pop the state with the lowest cost from the priority queue
        cost, _, current_puzzle, path = heapq.heappop(priority_queue)
        # If the current state is the goal state, return the solution path and the puzzle
        if current_puzzle.is_solved():
            return path, current_puzzle
        # Generate possible moves for the current state
        for move in current_puzzle.get_possible_moves():
            # Execute each move to get the next state
            next_state = current_puzzle.execute_move(*move)
            # Convert the next state into a tuple for hashability
            state_tuple = tuple(tuple(tube) for tube in next_state.tubes)
            # Check if the next state has not been seen before
            if state_tuple not in seen:
                # Mark the next state as seen
                seen.add(state_tuple)
                # Push the next state into the priority queue with updated cost and path
                heapq.heappush(priority_queue, (cost + 1, id_counter, next_state, path + [move]))
                # Increment the ID counter for the next state
                id_counter += 1
    # If no solution is found, return None
    return None, None
