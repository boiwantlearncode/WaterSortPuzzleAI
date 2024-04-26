import random
from collections import deque
import heapq
import sys
import pygame

from WaterSortPuzzle import WaterSortPuzzle
from search.BFS import bfs_solve
from search.DFS import dfs_solve
from search.DLS import dls_solve
from search.IDS import ids_solve
from search.UCS import ucs_solve
from search.GBFS import gbfs_solve
from search.ASTAR import a_star_solve

import os

random.seed(41)

# Increase recursion depth limit
sys.setrecursionlimit(10000)
frame_count = 0

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 400, 300
HEIGHT_TESTTUBE = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Sort Puzzle")

# Initialize the puzzle with the default state
initial_tubes = [
    ["red"] * 4,
    ["blue"] * 4,
    ["green"] * 4,
    [],
    []
]

print("Goal State:")
goal_puzzle = WaterSortPuzzle(initial_tubes)
print(goal_puzzle)

puzzle = WaterSortPuzzle(initial_tubes)
puzzle.shuffle()  # Shuffle the first three tubes only
print("\nRandomized Puzzle State:")
print(puzzle)

'''
The following is mainly the drawing of the canvas.
'''




# Define colors
colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "black": (0, 0, 0), "white": (55, 55, 55), "grey": (30, 30, 30)}

# Function to draw colored rectangles with a grey border and black borders between units
def draw_colored_rectangles(tubes):
    global frame_count
    num_tubes = len(tubes)
    rect_width = WIDTH // num_tubes  # Adding 1 for spacing
    for j in range(num_tubes):
        tube = tubes[j]

        for i in range(len(tube)):
            if tube[i]:
                # Draw filled rectangle
                pygame.draw.rect(screen, colors[tube[i]], (j * rect_width + 2, HEIGHT - (i + 1) * (HEIGHT // 4) + 2, rect_width - 4, HEIGHT // 4 - 4))
                # Draw grey border
                pygame.draw.rect(screen, colors["grey"], (j * rect_width, HEIGHT - (i + 1) * (HEIGHT // 4), rect_width, HEIGHT // 4), 4)
            else:
                # Draw black rectangle for empty tube
                pygame.draw.rect(screen, colors["white"], (j * rect_width, 0, rect_width, HEIGHT))
                # Draw grey border
                pygame.draw.rect(screen, colors["grey"], (j * rect_width, 0, rect_width, HEIGHT), 4)

    # Draw grey border on the rightmost side
    pygame.draw.rect(screen, colors["grey"], ((num_tubes) * rect_width, 0, rect_width, HEIGHT), 4)
    # screenshot_path = os.path.join('screenshots', f'screenshot_{frame_count:04d}.png')
    # pygame.image.save(screen, screenshot_path)
    # frame_count += 1

# Drawing of optimal path
def optimal_path_animation(puzzle, moves):
    for i in range(len(moves)):
        move = moves[i]
        puzzle = puzzle.execute_move(*move)
        screen.fill((55, 55, 55))
        draw_colored_rectangles(puzzle.tubes)
        pygame.display.flip()
        pygame.time.delay(150)

# Main program
screen.fill((55, 55, 55))

# Draw initial configuration
draw_colored_rectangles(puzzle.tubes)
pygame.display.flip()
pygame.time.delay(1000)

# puzzle.shuffle()  # Shuffle the first three tubes only

# Clear the screen
screen.fill((55, 55, 55))

# Draw randomized configuration
draw_colored_rectangles(puzzle.tubes)
pygame.display.flip()
pygame.time.delay(1000)


# Solve the puzzle using different methods
bfs_solution, bfs_final_puzzle = bfs_solve(puzzle)
dfs_solution, dfs_final_puzzle = dfs_solve(puzzle)
ucs_solution, ucs_final_puzzle = ucs_solve(puzzle)
ids_solution, ids_final_puzzle = ids_solve(puzzle)
dls_solution, dls_final_puzzle = dls_solve(puzzle, 30)  # Example depth limit
gbfs_solution, gbfs_final_puzzle = gbfs_solve(puzzle)
astar_solution, astar_final_puzzle = a_star_solve(puzzle)


# Compare and print the best solution
solutions = [
    ('BFS', bfs_solution, bfs_final_puzzle),
    ('DFS', dfs_solution, dfs_final_puzzle),
    ('UCS', ucs_solution, ucs_final_puzzle),
    ('IDS', ids_solution, ids_final_puzzle),
    ('DLS', dls_solution, dls_final_puzzle),
    ('GBFS', gbfs_solution, gbfs_final_puzzle),
    ('A*', astar_solution, astar_final_puzzle)
]

print("---------------------------------------------------------------")

# Compute the minimum number of moves among all successful methods 
min_moves = min(len(sol) for _, sol, _ in solutions) if solutions else None 
 
# Find all methods that have this minimum number of moves 
best_solutions = [(method, sol, final) for method, sol, final in solutions if len(sol) == min_moves] 
solutions = [(method, sol, final) for method, sol, final in solutions if sol]

 
# Print the names of all best methods and their moves 
if solutions:
    for i in solutions:
        print(f"\nNumber of moves for {i[0]}: {len(i[1])}")

if best_solutions: 
    methods = ", ".join([method for method, _, _ in best_solutions]) 
    print(f"\nBest Solutions found using {methods} with the following moves:") 
 
    for method, solution, final_puzzle in solutions: 
        print(f"\nSearch algorithm: {method}\n") 
        for index, move in enumerate(solution, 1): 
            if method == 'DFS' and (index > 5 and len(solution) - index > 4): 
                if index == 6: 
                    print("...") 
                continue 
            print(f"Move {index}: Transfer from tube {move[0]+1} to tube {move[1]+1}") 
        print(f"\nFinal Solved Puzzle using {method}:") 
        print(final_puzzle) 
        print("---------------------------------------------------------------") 
else: 
    print("No solution found.")

optimal_path_animation(puzzle, solution)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
sys.exit()