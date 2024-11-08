import time
import random
from cell import Cell

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    self._cells = []

    if seed:
      random.seed(seed)
      
    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()
  
  def _create_cells(self):
    for col in range(self._num_cols):
      column = []
      for row in range(self._num_rows):
        cell = Cell(self._win)
        column.append(cell)
      self._cells.append(column)
    for col in range(self._num_cols):
      for row in range(self._num_rows):
        self._draw_cell(col, row)
  
  def _draw_cell(self, col, row):
    if self._win is None:
      return

    # Calculate x, y position of the cell
    x1 = self._x1 + row * self._cell_size_x
    y1 = self._y1 + col * self._cell_size_y

    # Determine the opposite corners
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y

    # Draw each cell
    self._cells[col][row].draw(x1, y1, x2, y2)

    # Animate to update the visualization
    self._animate()

  def _animate(self):
    self._win.redraw()
    time.sleep(0.05)

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    self._cells[-1][-1].has_bottom_wall = False
    self._draw_cell(self._num_cols - 1, self._num_rows - 1)

  def _break_walls_r(self, col, row):
    self._cells[col][row].visited = True
    while True:
      to_visit = []

      # Check if we can go right
      if row+1 < self._num_rows and not self._cells[col][row+1].visited:
        to_visit.append((col, row+1))
        
      # Check if we can go left
      if row-1 >= 0 and not self._cells[col][row-1].visited:
        to_visit.append((col, row-1))

      # Check if we can go up
      if col-1 >= 0 and not self._cells[col-1][row].visited:
        to_visit.append((col-1, row))

      # Check if we can go down
      if col+1 < self._num_cols and not self._cells[col+1][row].visited:
        to_visit.append((col+1, row))

      # If there is nowhere to go from here just break out of the loop
      if len(to_visit) == 0:
        self._draw_cell(col, row)
        return

      # Randomly choose the next direction to go
      chosen_index = random.randrange(0, len(to_visit))
      next_col, next_row = to_visit[chosen_index]

      # Break right wall
      if next_row > row:
        self._cells[col][row].has_right_wall = False
        self._cells[col][next_row].has_left_wall = False

      # Break left wall
      if next_row < row:
        self._cells[col][row].has_left_wall = False
        self._cells[col][next_row].has_right_wall = False

      # Break top wall
      if next_col < col:
        self._cells[col][row].has_top_wall = False
        self._cells[next_col][row].has_bottom_wall = False

      # Break bottom wall
      if next_col > col:
        self._cells[col][row].has_bottom_wall = False
        self._cells[next_col][row].has_top_wall = False

      self._break_walls_r(next_col, next_row)

  def _reset_cells_visited(self):
    for col in self._cells:
      for cell in col:
        cell.visited = False