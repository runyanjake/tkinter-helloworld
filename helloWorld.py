from tkinter import *

tk = Tk()

window_width = 800
window_height = 600

win = Canvas(tk, width=window_width, height=window_height)
win.pack()

y = int(window_height / 2)
win.create_line(0, y, window_width, y, fill="#476042")

win.mainloop()