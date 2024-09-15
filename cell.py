from window import *

class Cell():
    def __init__(self, x1, y1, x2, y2, _win = None):

        self.has_walls = [True, True, True, True] #left, right, top, bottom

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self._win = _win

        self.visited = False


    def draw(self):
        if self.has_walls[0]:
            # line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
            # self._win.draw_line(line)
            self._win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill= "black", width = 2)
        else:
            self._win.canvas.create_line(self.x1, self.y1, self.x1, self.y2, fill= "white", width = 2)

        if self.has_walls[1]:
            # line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
            # self._win.draw_line(line)
            self._win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill= "black", width = 2)
        else:
            self._win.canvas.create_line(self.x2, self.y1, self.x2, self.y2, fill= "white", width = 2)

        if self.has_walls[2]:
            # line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
            # self._win.draw_line(line)
            self._win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill= "black", width = 2)
        else:
            self._win.canvas.create_line(self.x1, self.y1, self.x2, self.y1, fill= "white", width = 2)


        if self.has_walls[3]:
            # line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
            # self._win.draw_line(line)
            self._win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill= "black", width = 2)
        else:
            self._win.canvas.create_line(self.x1, self.y2, self.x2, self.y2, fill= "white", width = 2)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        center = ((self.x1+self.x2)/2 , (self.y1+self.y2)/2)
        to_center = ((to_cell.x1+to_cell.x2)/2 , (to_cell.y1+to_cell.y2)/2)


        self._win.canvas.create_line(center[0], center[1], to_center[0], to_center[1], fill = color, width = 2)

    def destroy_wall(self, side, opposite = False):
        if opposite:
            match side:
                case "left":
                    self.has_walls[1] = False
                case "right":
                    self.has_walls[0] = False
                case "top":
                    self.has_walls[3] = False
                case "bottom":
                    self.has_walls[2] = False
                case _:
                    raise Exception("Invalid side input into cell's destroy method.")
        else:
            match side:
                case "left":
                    self.has_walls[0] = False
                case "right":
                    self.has_walls[1] = False
                case "top":
                    self.has_walls[2] = False
                case "bottom":
                    self.has_walls[3] = False
                case _:
                    raise Exception("Invalid side input into cell's destroy method.")
            