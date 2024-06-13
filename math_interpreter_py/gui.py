import tkinter as tk
from tkinter.constants import LEFT, RAISED

root = tk.Tk()

# OUTPUT LABEL

var = tk.StringVar()
var.set("hello there")
entry_frame = tk.Label(root, textvariable=var, relief=RAISED)
entry_frame.pack()

# 1-9 BUTTONS

def button_cmd(c):
    lbl = tk.Label(num_frame, text=str(c))
    lbl.grid(row=4, column=4)

num_frame = tk.Frame(root)
num_frame.pack()

# DIGITS 1-9

button_1 = tk.Button(num_frame, text='1', padx=21, command=lambda: button_cmd(1))
button_2 = tk.Button(num_frame, text='2', padx=21, command=lambda: button_cmd(2))
button_3 = tk.Button(num_frame, text='3', padx=21, command=lambda: button_cmd(3))
button_4 = tk.Button(num_frame, text='4', padx=21, command=lambda: button_cmd(4))
button_5 = tk.Button(num_frame, text='5', padx=21, command=lambda: button_cmd(5))
button_6 = tk.Button(num_frame, text='6', padx=21, command=lambda: button_cmd(6))
button_7 = tk.Button(num_frame, text='7', padx=21, command=lambda: button_cmd(7))
button_8 = tk.Button(num_frame, text='8', padx=21, command=lambda: button_cmd(8))
button_9 = tk.Button(num_frame, text='9', padx=21, command=lambda: button_cmd(9))

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

# 0, ., CLR BUTTONS

bottom_frame = tk.Frame(root)
bottom_frame.pack()

button_pt = tk.Button(bottom_frame, text='.', padx=23, command=lambda: button_cmd('.'))
button_zero = tk.Button(bottom_frame, text='0', padx=21, command=lambda: button_cmd(0))
button_clr = tk.Button(bottom_frame, text="Clear", padx=10)

button_pt.pack(side=LEFT)
button_zero.pack(side=LEFT)
button_clr.pack(side=LEFT)

root.mainloop()
