import unittest
from maze import Maze

class Tests(unittest.TestCase):
  def test_maze_create_cells(self):
    num_cols = 12
    num_rows = 10
    maze = Maze(0, 0, num_rows, num_cols, 10, 10)
    self.assertEqual(
      len(maze._cells),
      num_cols
    )
    self.assertEqual(
      len(maze._cells[0]),
      num_rows
    )

  def test_maze_create_cells_large(self):
    num_cols = 16
    num_rows = 20
    maze = Maze(5, 5, num_rows, num_cols, 50, 50)
    self.assertEqual(
      len(maze._cells),
      num_cols
    )
    self.assertEqual(
      len(maze._cells[0]),
      num_rows
    )

  def test_maze_break_entrance_and_exit(self):
    num_cols = 5
    num_rows = 5
    maze = Maze(0, 0, num_rows, num_cols, 10, 10)
    entrance_cell = maze._cells[0][0]
    exit_cell = maze._cells[-1][-1]
    self.assertEqual(entrance_cell.has_top_wall, False)
    self.assertEqual(exit_cell.has_bottom_wall, False)

  def test_maze_reset_cells_visited(self):
    num_cols = 3
    num_rows = 3
    maze = Maze(0, 0, num_rows, num_cols, 10, 10)
    for col in maze._cells:
      for cell in col:
        self.assertEqual(cell.visited, False)

if __name__ == "__main__":
  unittest.main()