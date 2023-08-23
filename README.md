# Puzzle-Solver-
# Eight Puzzle Solver Project

## Overview

This project aims to solve the Eight Puzzle using state-space search algorithms. The Eight Puzzle is a classic sliding puzzle with a 3x3 grid and eight numbered tiles, along with an empty tile. The goal is to arrange the tiles in ascending order to reach the configuration:
```
1 2 3
4 5 6
7 8 0
```

## Code Structure

The project consists of three Python files: `board.py`, `state.py`, and `searcher.py`, each serving specific roles.

### `board.py`

This file defines the `Board` class, responsible for representing the puzzle configuration. The `Board` class includes methods to initialize a puzzle board, move tiles, generate a digital string representation, compute the number of misplaced tiles, compare boards, and perform heuristic evaluations.

### `state.py`

The `State` class in this file represents a state in the state-space search tree of the Eight Puzzle. It maintains information about the puzzle board, predecessor state, performed move, number of moves, and various methods for generating successors, checking for goal state, detecting cycles, and printing the sequence of moves.

### `searcher.py`

In this file, the `Searcher` class is implemented as a base class for state-space search algorithms. It includes methods for adding and prioritizing states, selecting the next state to explore, and performing a search for the solution. Additional classes, such as `BFSearcher`, `DFSearcher`, `GreedySearcher`, and `AStarSearcher`, inherit from the `Searcher` class and implement different search algorithms.


## Tech Stack

The project employs the following technologies:

- Python: The primary programming language used for implementation.
- Object-Oriented Design: Utilized to create modular and organized code through class structures.
- State-Space Search: Algorithms implemented to solve the Eight Puzzle, including breadth-first search, depth-first search, greedy search, and A* search.
- Git: Version control system to manage and track code changes.

## Contributors

- Shashank Ramachandran (sr31@bu.edu)
- Michael Krah (mickra@bu.edu)
