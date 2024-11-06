from graphics import Point, Line

class Cell:
  def __init__(self, win=None):
    self.has_right_wall = True
    self.has_left_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self._win = win

  def draw(self, x1, y1, x2, y2):
    if self._win is None:
      return
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
    if self.has_left_wall:
      p1 = Point(x1, y1)
      p2 = Point(x1, y2)
      left_wall_line = Line(p1, p2)
      self._win.draw_line(left_wall_line)

    if self.has_right_wall:
      p1 = Point(x2, y1)
      p2 = Point(x2, y2)
      right_wall_line = Line(p1, p2)
      self._win.draw_line(right_wall_line)

    if self.has_top_wall:
      p1 = Point(x1, y1)
      p2 = Point(x2, y1)
      top_wall_line = Line(p1, p2)
      self._win.draw_line(top_wall_line)
    
    if self.has_bottom_wall:
      p1 = Point(x1, y2)
      p2 = Point(x2, y2)
      bottom_wall_line = Line(p1, p2)
      self._win.draw_line(bottom_wall_line)
  
  def draw_move(self, to_cell, undo=False):
    fill_color = "red"
    if undo:
      fill_color = "gray"

    half_length = abs(self._x2 - self._x1) // 2
    x_center = half_length + self._x1
    y_center = half_length + self._y1

    half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
    x_center2 = half_length2 + to_cell._x1
    y_center2 = half_length2 + to_cell._y1

    p1 = Point(x_center, y_center)
    p2 = Point(x_center2, y_center2)
    line = Line(p1, p2)
    self._win.draw_line(line, fill_color)