import random

class WaterSortPuzzle:
    def __init__(self, tubes):
        # Initialize the puzzle with the given tubes
        self.tubes = [tube[:] for tube in tubes]  # Deep copy to ensure states are not shared

    def is_solved(self):
        # Check if the puzzle is solved, i.e., all tubes in the goal area and others are empty
        return all(len(set(tube)) == 1 for tube in self.tubes[:3] if tube) and all(not tube for tube in self.tubes[3:])

    def get_possible_moves(self):
        # Get all possible moves that can be made from the current state
        moves = []
        for i, src in enumerate(self.tubes):
            if not src:
                continue
            for j, dst in enumerate(self.tubes):
                if i != j and (not dst or src[-1] == dst[-1]) and len(dst) < 4:
                    moves.append((i, j))
        return moves

    def execute_move(self, src_idx, dst_idx):
        # Execute a move by moving a unit of colour from the source tube to the destination tube
        new_tubes = [tube[:] for tube in self.tubes]
        new_tubes[dst_idx].append(new_tubes[src_idx].pop())
        return WaterSortPuzzle(new_tubes)

    def shuffle(self):
        # Shuffle the contents of the tubes to create a new puzzle state
        contents = sum((self.tubes[i][:] for i in range(3)), [])
        random.shuffle(contents)
        for i in range(3):
            self.tubes[i] = contents[i*4:(i+1)*4]

    def __str__(self):
        # String representation of the puzzle showing each tube's contents
        return '\n'.join(str(i + 1) + ": " + str(tube) for i, tube in enumerate(self.tubes))

    def heuristic(self):
        # Heuristic for Greedy Best First Search and A*: higher is better, combining counts of correct and empty tubes
        correct_tubes = sum(len(set(tube)) == 1 for tube in self.tubes if tube)
        empty_tubes = sum(1 for tube in self.tubes if not tube)
        return correct_tubes + empty_tubes
