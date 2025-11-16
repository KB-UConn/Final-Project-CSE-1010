import os
os.system('cls' if os.name == 'nt' else 'clear')
os.system('clear')

from library import functions
from library.classes_9 import Budget
import tkinter as tk

window = tk.Tk()
window.title("Budget Buddy App")

label = tk.Label(window, text="Please Enter your Name to Sign In.")
label.pack()
text_box = tk.Text(window, height=10, width=50)
text_box.pack(padx=10, pady=10)
button = tk.Button(window, text="Click Me", command=lambda: print("Button clicked!"))
button.pack()
window.mainloop()





name_of_user = input("Enter your name:")
print(f"Hey {name_of_user}, this is BudgetBuddy! Your personal Budgesting Assistant.")
income = float(input("Enter your monthly income (only numbers):"))
total_expenses = []

grocery = Budget("Grocery")
car = Budget("Car")

grocery.add_expenses()
car.add_expenses()

total_expenses.append(grocery.get_expenses())
total_expenses.append(car.get_expenses())

balance = functions.calc_balance(income, sum(total_expenses))
functions.financial_status(balance)

grocery.get_expense_details()
car.get_expense_details()
