import tkinter

button_values = [
    ["AC","+/-","%","÷"],
    ["7","8","9","x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_ct = len(button_values) #5
column_ct= len(button_values) #4

color_light_gray = "#1D3075"
color_black ="#560763"
color_dark_gray= "#FF983A"
color_orange= "#BD3C3C"
color_white= "white"


window= tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)
window.mainloop()