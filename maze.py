from cell import *
from window import *
import time
import random


class Maze():
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y, _win = None, seed = None):

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        self._win = _win

        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        
        x0 = self.x1
        y0 = self.y1
        for i in range(self.num_cols):

            col = []
            for j in range(self.num_rows):
                col.append(Cell(x0 + i*self.cell_size_x, y0 + j*self.cell_size_y, x0 + (i+1)*self.cell_size_x, y0 + (j+1)*self.cell_size_y, self._win))
                
                
            self._cells.append(col)

        

        for col in self._cells:
            for c in col:
                
                c.draw()
                self._animate()

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_walls[2] = False
        self._draw_cell(0,0)
        self._animate()
        self._cells[-1][-1].has_walls[3] = False
        self._draw_cell(-1,-1)
        self._animate()

    def valid_cell(self,i,j):
        if i>=0 and i<self.num_cols:
            if j>=0 and j<self.num_rows:
                return True
            
        return False
    
    def find_adjacent(self, i, j):
        c = []
        
        if self.valid_cell(i-1, j) and not self._cells[i-1][j].visited: #left
            c.append("left")

        if self.valid_cell(i+1, j) and not self._cells[i+1][j].visited: #right
            c.append("right")

        if self.valid_cell(i, j-1) and not self._cells[i][j-1].visited: #top
            c.append("top")
            
        if self.valid_cell(i, j+1) and not self._cells[i][j+1].visited: #bottom
            c.append("bottom")
            
        return c


    def _break_walls_r(self, i, j):

        self._cells[i][j].visited = True
        
        
        
        while True:
            to_visit = []

            possible_adjacent_cells = self.find_adjacent(i,j)

            if len(possible_adjacent_cells) == 0:
                return
            else:
                direction = possible_adjacent_cells[random.randint(0,len(possible_adjacent_cells)-1)]

                self._cells[i][j].destroy_wall(direction)
                self._draw_cell(i,j)
                match direction:
                    case "left":
                        self._cells[i-1][j].destroy_wall(direction, True)
                        self._break_walls_r(i-1,j)
                        self._draw_cell(i-1,j)
                    case "right":
                        self._cells[i+1][j].destroy_wall(direction, True)
                        self._break_walls_r(i+1,j)
                        self._draw_cell(i+1,j)
                    case "top":
                        self._cells[i][j-1].destroy_wall(direction, True)
                        self._break_walls_r(i,j-1)
                        self._draw_cell(i,j-1)
                    case "bottom":
                        self._cells[i][j+1].destroy_wall(direction, True)
                        self._break_walls_r(i,j+1)
                        self._draw_cell(i,j+1)

            self._animate()

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def find_possible_moves(self, i, j):
        c = []
        
        if self.valid_cell(i-1, j) and not self._cells[i][j].has_walls[0] : #left
            c.append("left")

        if self.valid_cell(i+1, j) and not self._cells[i][j].has_walls[1]: #right
            c.append("right")

        if self.valid_cell(i, j-1) and not self._cells[i][j].has_walls[2]: #top
            c.append("top")
            
        if self.valid_cell(i, j+1) and not self._cells[i][j].has_walls[3]: #bottom
            c.append("bottom")
            
        return c
    
    def direction_to_move(self, facing, possible):
        match facing:
            case "north":
                if possible.__contains__("left"):
                    return "left"
                elif possible.__contains__("top"):
                    return "up"
                elif possible.__contains__("right"):
                    return "right"
                else:
                    return "down"
            case "east":
                if possible.__contains__("top"):
                    return "up"
                elif possible.__contains__("right"):
                    return "right"
                elif possible.__contains__("bottom"):
                    return "down"
                else:
                    return "left"
            case "south":
                if possible.__contains__("right"):
                    return "right"
                elif possible.__contains__("bottom"):
                    return "down"
                elif possible.__contains__("left"):
                    return "left"
                else:
                    return "up"
            case "west":
                if possible.__contains__("bottom"):
                    return "down"
                elif possible.__contains__("left"):
                    return "left"
                elif possible.__contains__("top"):
                    return "up"
                else:
                    return "right"

    def solve(self):
        return self._solve_r(0,0)      
                
    def _solve_r(self, i, j):

        facing = "south"
        not_at_end = True
        while not_at_end:
            
            self._cells[i][j].visited = True
            possible_moves = self.find_possible_moves(i,j)
            

            if len(possible_moves) == 0:
                print("failed")
                return False
            else:
                direction = self.direction_to_move(facing, possible_moves)
                
                #move and draw move
                match direction:
                    case "left":
                        self._cells[i][j].draw_move(self._cells[i-1][j], self._cells[i-1][j].visited)
                        i-=1
                    case "up":
                        self._cells[i][j].draw_move(self._cells[i][j-1], self._cells[i][j-1].visited)
                        j-=1
                    case "right":
                        self._cells[i][j].draw_move(self._cells[i+1][j], self._cells[i+1][j].visited)
                        i+=1
                    case "down":
                        self._cells[i][j].draw_move(self._cells[i][j+1], self._cells[i][j+1].visited)
                        j+=1


                #change facing
                if direction == "up":
                    facing = "north"
                elif direction == "right":
                    facing = "east"
                elif direction == "down":
                    facing = "south"
                else:
                    facing = "west"
                

            self._animate()
            if i == self.num_cols-1 and j == self.num_rows-1:
                not_at_end = False

        return True