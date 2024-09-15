from window import *
from cell import *
from maze import *
import time



# def main():

#     win = Window(800, 600)

#     map = Maze(5,5,12,16,50,50,win)

#     win.wait_for_close()

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    maze._break_entrance_and_exit()

    maze._break_walls_r(0,0)

    maze._reset_cells_visited()

    maze.solve()

    win.wait_for_close()


main()