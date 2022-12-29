from tkinter import *
from tkinter import ttk
import pyautogui as external_input


def get_mouse_pos():
    position = external_input.position()
    mouse_point = (position[0], position[1])
    print(mouse_point)
    
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Button(frm, text="get mouse position", command=get_mouse_pos).grid(column=1, row=0)
ttk.Button(frm, text="close", command=root.destroy).grid(column=2, row=0)
root.mainloop()