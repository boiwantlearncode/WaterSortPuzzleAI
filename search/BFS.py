from collections import deque

def bfs_solve(puzzle):
    # Initialize a queue with the initial puzzle state and an empty path
    queue = deque([(puzzle, [])])
    
    # Initialize a set to keep track of seen states to avoid duplicates
    seen = set([tuple(tuple(tube) for tube in puzzle.tubes)])
    
    # Loop until the queue is empty
    while queue:
        # Dequeue the current puzzle state and its corresponding path
        current_puzzle, path = queue.popleft()
        
        # Check if the current puzzle state is solved
        if current_puzzle.is_solved():
            # If solved, return the solution path and the final puzzle state
            return path, current_puzzle
        
        # Iterate over all possible moves from the current state
        for move in current_puzzle.get_possible_moves():
            # Execute the move to get the next state
            next_state = current_puzzle.execute_move(*move)
            
            # Convert the next state to a tuple representation
            state_tuple = tuple(tuple(tube) for tube in next_state.tubes)
            
            # Check if the next state has not been seen before
            if state_tuple not in seen:
                # If unseen, add it to the set of seen states
                seen.add(state_tuple)
                # Enqueue the next state and update the path
                queue.append((next_state, path + [move]))
    
    # If no solution is found, return None for both path and puzzle state
    return None, None

