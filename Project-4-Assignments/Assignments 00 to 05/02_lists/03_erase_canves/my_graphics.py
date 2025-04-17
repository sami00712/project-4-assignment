import tkinter as tk

class Canvas:
    def __init__(self, width, height, title="Canvas"):
        """Initialize the Canvas with given width, height, and title"""
        self.root = tk.Tk()
        self.root.title(title)
        self.canvas = tk.Canvas(self.root, width=width, height=height, bg="blue")
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.window_closed = False

        # Bind mouse events
        self.canvas.bind("<Motion>", self.update_mouse)
        self.canvas.bind("<Button-1>", self.get_last_click)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_mouse(self, event):
        """Update mouse position"""
        self.mouse_x, self.mouse_y = event.x, event.y

    def get_mouse_x(self):
        """Get current mouse x position"""
        return self.mouse_x

    def get_mouse_y(self):
        """Get current mouse y position"""
        return self.mouse_y

    def get_last_click(self, event):
        """Get last click position"""
        self.last_click_x, self.last_click_y = event.x, event.y

    def create_rectangle(self, x1, y1, x2, y2, color="black"):
        """Create a rectangle on the canvas"""
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def find_overlapping(self, x1, y1, x2, y2):
        """Find objects overlapping with given coordinates"""
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def set_color(self, obj, color):
        """Change color of an object"""
        self.canvas.itemconfig(obj, fill=color)

    def run(self):
        """Run the Tkinter event loop"""
        self.root.mainloop()

    def on_close(self):
        """Handle window close event"""
        self.window_closed = True
        self.root.destroy()
