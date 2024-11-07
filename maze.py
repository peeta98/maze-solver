import time
from cell import Cell

class Maze:
  def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    self._cells = []
    self._create_cells()
    self._break_entrance_and_exit()
  
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