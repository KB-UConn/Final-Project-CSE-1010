# Task 1. Modify classes_9.py to collect input expenses with expense type and handle error
    # a. Collect inout expenses form users as "Type Cost", for e.g., Mile 10, and store them in appropreate 
    #       variable
    # b. Add error handling functionality to check if inout is provided in the correct format and in 
    #       correct order
    # c. if no error, add category and cost in the category ad expenses list
    # d. If there is error, print a user-friendly message and take the input again
# Task 2. Create a method get_expense_details to print the list of expenses

import os
from library import functions
from library.classes_9 import Budget
os.system('cls' if os.name == 'nt' else 'clear')
os.system('clear')
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