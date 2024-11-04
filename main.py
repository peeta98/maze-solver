from graphics import Window, Point, Line
from tkinter import Tk

def main():
  print("Creating window...")
  win = Window(800, 600)
  print("Drawing line...")
  l = Line(Point(50, 50), Point(400, 400))
  win.draw_line(l, "black")
  print("Waiting for close...")
  win.wait_for_close()

main()