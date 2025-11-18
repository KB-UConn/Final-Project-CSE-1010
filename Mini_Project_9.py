import os
from library import functions
from library.final_classes import Budget
import matplotlib.pyplot as plt
import tkinter as tk

#Main Window Setup
window = tk.Tk()
window.title("Budget Buddy App")
window.geometry("500x400")

#Global Variables
budgets = {}
income = 0
user_name = ""

# Load saved categories
for filename in os.listdir():
    if filename.endswith(".txt"):
        category_name = filename.replace(".txt", "")
        budgets[category_name] = Budget(category_name)

#Code for Main Menu Functions
def hide_all():
    for widget in window.winfo_children():
        widget.pack_forget()

def show_main_menu():
    hide_all()
    status_msg.config(text="")
    for b in main_buttons:
        b.pack(pady=8)
    status_msg.pack(pady=10)

label1 = tk.Label(window, text = "Please Enter your Name to Sign In", font = ("Montserrat", 12))
text_name = tk.Entry(window, font = ("Montserrat", 12))
label_income = tk.Label(window, text = " Enter Monthly Income", font = ("Montserrat", 14))
text_income = tk.Entry(window, font = ("Montserrat", 12))
status_msg = tk.Label(window, text = "", fg="red", font =("Montserrat", 11))

def sign_in():
    global income, user_name
    user_name = text_name.get().strip()
    if not user_name:
        status_msg.config(text="Error: Please enter your name.")
        return
    try:
        income = float(text_income.get())
    except ValueError:
        status_msg.config(text="Error: Income must be a number.")
        return
    
    # Hide sign-in widgets
    label1.pack_forget()
    text_name.pack_forget()
    label_income.pack_forget()
    text_income.pack_forget()
    button1.pack_forget()
    
    # Show main menu buttons
    for b in main_buttons:
        b.pack(pady=8)
    status_msg.config(text="")

button1 = tk.Button(window, text="Sign In", command = sign_in, font = ("Montserrat", 12))

label1.pack(pady=10)
text_name.pack(pady=10)
label_income.pack(pady=10)
text_income.pack(pady=10)
button1.pack(pady=10)
status_msg.pack(pady=10)

#Main Menu Widgets:
#Main Menu Widgets:
def go_create_category():
    hide_all()
    label2.pack(pady=10)
    category_entry.pack(pady=5)
    back_button.pack(pady=15)

def go_add_expenses():
    hide_all()
    label3.pack(pady=10)
    expense_category_entry.pack(pady=5)
    expense_amount_entry.pack(pady=5)
    back_button.pack(pady=15)

def go_display_expenses():
    hide_all()
    label4.pack(pady=10)
    expenses_listbox.pack(pady=10)
    back_button.pack(pady=15)

def go_financial_status():
    hide_all()
    label5.pack(pady=10)
    status_label.pack(pady=10)
    back_button.pack(pady=15)

button2 = tk.Button(window, text = "Create New Expenses Category", font = ("Montserrat", 12), command = go_create_category)
button3 = tk.Button(window, text = "Add Expenses into Category", font = ("Montserrat", 12), command = go_add_expenses)
button4 = tk.Button(window, text = "Display Expenses List", font = ("Montserrat", 12), command = go_display_expenses)
button5 = tk.Button(window, text = "My Financial Status", font = ("Montserrat", 12), command = go_financial_status)
button6 = tk.Button(window, text = "Save Changes", font = ("Montserrat", 12))
button7 = tk.Button(window, text = "Exit Program", font = ("Montserrat", 12), command = window.destroy)

main_buttons = [button2, button3, button4, button5, button6, button7]

#Create New Expenses Category Screen 
label2 = tk.Label(window, text = "Create New Expenses Category", font = ("Montserrat", 14))
category_entry = tk.Entry(window, font = ("Montserrat", 12))

#Add Expenses into Category Screen
label3 = tk.Label(window, text = "Add Expenses into Category", font = ("Montserrat", 14))
expense_category_entry = tk.Entry(window, font = ("Montserrat", 12))
expense_amount_entry = tk.Entry(window, font = ("Montserrat", 12))

# Display Expenses List Screen
label4 = tk.Label(window, text = "Display Expenses List", font = ("Montserrat", 14))
expenses_listbox = tk.Listbox(window, width = 50, height = 10, font=("Montserrat", 12))

# My Financial Status Screen
label5 = tk.Label(window, text="My Financial Status", font=("Montserrat", 14))
status_label = tk.Label(window, text = "Your status will appear here", font = ("Montserrat", 12))

def show_chart():
    if not budgets:
        status_msg.config(text="Error: No categories to chart.")
        return

    categories = []
    totals = []

    for name, budget in budgets.items():
        categories.append(name)
        totals.append(sum(budget.expenses_dict.values()))
    
    # Bar chart
    plt.figure(figsize=(6, 4))
    plt.bar(categories, totals, color='skyblue')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Spent ($)")
    plt.tight_layout()
    plt.show()

chart_button = tk.Button(window, text="Show Spending Chart", font=("Montserrat", 12), command = show_chart)

# Save Changes Screen
def save_all_categories():
    for budget in budgets.values():
        budget.write_to_file()
    status_msg.config(text="All categories saved!", fg="green")

button6.config(command = save_all_categories)

# Return Button
back_button = tk.Button(window, text = "Return to Main Menu", font = ("Montserrat", 12), command = show_main_menu)

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
