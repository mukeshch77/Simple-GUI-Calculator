import tkinter as tk
from tkinter import messagebox


# Create the main window with black background
window = tk.Tk()
window.title("Mukesh Calculator")
window.config(bg="black")  

# History of calculations
history = []

expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
        history.append(f"{entry.get()}") 
    except Exception as e:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Function to show history
def show_history():
    if not history:
        messagebox.showinfo("History", "No calculations yet.")
    else:
        history_string = "\n".join(history)
        messagebox.showinfo("Calculation History", history_string)

# Function to exit the application
def exit_app():
    window.quit()


equation = tk.StringVar()
entry = tk.Entry(window, textvariable=equation, width=30, font=("Arial", 14), borderwidth=2, relief="solid", justify="right", bg="#3e332f", fg="#000000")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)


buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]


for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), bg="black", fg="white", command=equalpress)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), bg="black", fg="white", command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create the clear, exit, and history buttons
clear_b = tk.Button(window, text="AC", width=5, height=2, font=("Arial", 14), bg="black", fg="white", command=clear)
clear_b.grid(row=1, column=0, padx=5, pady=10)

history_b = tk.Button(window, text="History", width=5, height=2, font=("Arial", 14), bg="black", fg="white", command=show_history)
history_b.grid(row=1, column=2, padx=5, pady=10)

exit_b = tk.Button(window, text="Exit", width=5, height=2, font=("Arial", 14), bg="black", fg="white", command=exit_app)
exit_b.grid(row=1, column=3, padx=5, pady=10)


window.mainloop()
