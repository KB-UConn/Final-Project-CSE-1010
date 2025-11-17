import os
os.system('cls' if os.name == 'nt' else 'clear')
os.system('clear')

from library import functions
from library.classes_9 import Budget
import tkinter as tk

#Main Window Setup
window = tk.Tk()
window.title("Budget Buddy App")
window.geometry("500x400")

#Code for Sign in Screen
def toggle1():
    if button1.winfo_viewable():
        text_box1.destroy()
        button1.destroy()
        label1.destroy()
        #global name
        #global my_string_var
        #name = text_box1.get("1.0", tk.END)
        #my_string_var = name
        #smy_string_var = tk.StringVar()
        #label2.pack(side = "left")
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()
        button7.pack()

#Code for Main Menu Functions
def hide_all():
    for widget in window.winfo_children():
        widget.pack_forget()

def show_main_menu():
    hide_all()
    for b in main_buttons:
        b.pack(pady=8)

label1 = tk.Label(window, text="Please Enter your Name to Sign In", font = ("Montserrat", 12))
text_box1 = tk.Text(window, height=2, width=25, font = ("Montserrat", 12))

def sign_in():
    hide_all()
    show_main_menu()

button1 = tk.Button(window, text="Click Me to Sign In", command = toggle1, font = ("Montserrat", 12))

#Sign in Screen
label1.pack(padx=10, pady=10)
text_box1.pack(padx=10, pady=10)
button1.pack(padx=10, pady=10)

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
