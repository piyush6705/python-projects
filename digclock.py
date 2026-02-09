
import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg='black')

use_24 = tk.BooleanVar(value=False)

def update_time():
    if use_24.get():
        t = strftime('%H:%M:%S')
    else:
        t = strftime('%I:%M:%S %p')
    d = strftime('%A, %B %d, %Y')
    time_label.config(text=t)
    date_label.config(text=d)
    root.after(1000, update_time)

time_label = tk.Label(root, font=('calibri', 64, 'bold'), bg='black', fg='white')
time_label.pack(padx=20, pady=(20, 5))

date_label = tk.Label(root, font=('calibri', 16), bg='black', fg='lightgray')
date_label.pack(padx=20, pady=(0, 20))

controls = tk.Frame(root, bg='black')
controls.pack(pady=(0, 12))

toggle = tk.Checkbutton(controls, text='24-hour', variable=use_24, bg='black', fg='white', selectcolor='black', activebackground='black', activeforeground='white')
toggle.pack(side='left', padx=10)

# Center the window on the screen
root.update_idletasks()
width, height = 520, 240
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
pos_x = (screen_w // 2) - (width // 2)
pos_y = (screen_h // 2) - (height // 2)
root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
root.resizable(False, False)

update_time()
root.mainloop()

