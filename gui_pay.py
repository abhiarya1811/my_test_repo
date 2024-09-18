import tkinter as tk
from tkinter import messagebox

def calculate_pay():
    try:
        worked_hours = int(hours_entry.get())
        
        if worked_hours < 40:
            pay = 10 * worked_hours
        elif worked_hours > 40:
            pay = (10 * worked_hours) + (5 * (worked_hours - 40))
        
        result_label.config(text=f"Employee worked for {worked_hours} hours and earned {pay} $")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for hours worked.")


window = tk.Tk()
window.title("Employee Pay Calculator")

hours_label = tk.Label(window, text="Enter number of worked hours:")
hours_label.grid(row=0, column=0, padx=100, pady=100)

hours_entry = tk.Entry(window)
hours_entry.grid(row=0, column=1, padx=100, pady=10)

calculate_button = tk.Button(window, text="Calculate Pay", command=calculate_pay)
calculate_button.grid(row=1, column=0, columnspan=2, pady=20)

result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
