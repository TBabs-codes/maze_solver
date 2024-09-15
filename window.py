from tkinter import Tk, BOTH, Canvas

class Window():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root_widget = Tk()
        # self.root_widget.geometry(f'{height}x{width}')
        self.root_widget.title("Title of Widget")
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
        

        self.canvas = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)

        self.running = False

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True

        # Should I put this into a loop??? It says to keep redrawing as long as self.running == True.
        while self.running:
            self.redraw()
        print("window closed.")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color = "black"):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill= fill_color, width = 2)



