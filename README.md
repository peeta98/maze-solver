# Maze Solver 🧩

Welcome to the Maze Solver project! 

This program is designed to tackle maze challenges using depth-first search (DFS) and breadth-first search (BFS) algorithms. The solution navigates through the maze, marking visited paths and backtracking as needed.

## Features

- **Maze Generation with Breadth-First Search**: Uses BFS logic to randomly remove walls and generate the initial maze structure.
- **Maze Solving with Depth-First Search**: Utilizes DFS to explore possible paths within the maze.
- **Backtracking**: Efficiently handles dead ends by reversing movements.
- **Animated Visualization**: Watch the algorithm in action as it solves the maze step-by-step.
- **Customizable Mazes**: Experiment with different maze structures and configurations.

## How It Works

The program starts at the maze's starting cell, marking it as visited. It then checks all neighboring cells for possible moves, preferring unvisited cells without walls. When it encounters a dead end or a previously visited cell, it backtracks to explore alternative routes.

## Getting Started

Follow these steps to get the project running on your local machine for development and testing.

### Prerequisites

  * **Python 3.10 or higher**: Ensure Python is installed on your machine. You can download it from [python.org](https://www.python.org/).
  * **Tkinter**: Used to create the graphical interface. Tkinter is usually included with Python, but if not, it can be installed separately.

### Running the Project

1. **Clone the repository**:
  ```bash
    git clone https://github.com/peeta98/maze-solver.git
  ```

2. **Nagivate into the project directory**:
  ```bash
    cd maze-solver
  ```

3. **Run the main script** to start the maze-solving visualization:
  ```bash
    python3 main.py
  ````