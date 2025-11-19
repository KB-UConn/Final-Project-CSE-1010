import os
from library import functions
from library.final_classes import Budget
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.title("Budget Buddy App")
window.geometry("500x400")

budgets = {}
income = 0
user_name = ""

# Load categories
for filename in os.listdir():
    if filename.endswith(".txt"):
        cat = filename.replace(".txt", "")
        budgets[cat] = Budget(cat)

# Dropdown
expense_dropdown = ttk.Combobox(
    window, 
    values=list(budgets.keys()), 
    state="readonly",
    font=("Montserrat", 12)
)

# Update dropdown every new ctegory
def reset_dropdown():
    vals = list(budgets.keys())
    expense_dropdown['values'] = vals
    if vals:
        try:
            expense_dropdown.current(0)
        except tk.TclError:
            pass
    else:
        expense_dropdown.set("")




def hide_all():
    """Hide all pack() widgets."""
    for widget in window.winfo_children():
        try:
            widget.pack_forget()
        except:
            pass

def show_main_menu():
    hide_all()
    status_msg.config(text="")
    for b in main_buttons:
        b.pack(pady=8)
    status_msg.pack(pady=10)
    user_label.place(x=10, y=10)  



label1 = tk.Label(window, text="Please Enter your Name to Sign In", font=("Montserrat", 12))
text_name = tk.Entry(window, font=("Montserrat", 12))
label_income = tk.Label(window, text=" Enter Monthly Income", font=("Montserrat", 14))
text_income = tk.Entry(window, font=("Montserrat", 12))
status_msg = tk.Label(window, text="", fg="red", font=("Montserrat", 11))

user_label = tk.Label(window, text="", font=("Montserrat", 12), fg="green")

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

    # Hide sign-in stuff
    label1.pack_forget()
    text_name.pack_forget()
    label_income.pack_forget()
    text_income.pack_forget()
    button1.pack_forget()

    show_main_menu()
    user_label.config(text=f"Hello, {user_name}!")
    user_label.place(x=10, y=10)

button1 = tk.Button(window, text="Sign In", command=sign_in, font=("Montserrat", 12))

label1.pack(pady=10)
text_name.pack(pady=10)
label_income.pack(pady=10)
text_income.pack(pady=10)
button1.pack(pady=10)
status_msg.pack(pady=10)


# main menu

def go_create_category():
    hide_all()
    user_label.place_forget()
    label2.pack(pady=10)
    category_entry.pack(pady=5)
    create_button.pack(pady=5)
    back_button.pack(pady=15)

def go_add_expenses():
    hide_all()
    user_label.place_forget()
    label3.pack(pady=10)
    reset_dropdown()
    expense_dropdown.pack(pady=5)
    expense_type_entry.pack(pady=5)
    expense_amount_entry.pack(pady=5)
    add_expense_button.pack(pady=5)
    back_button.pack(pady=15)

def go_display_expenses():
    hide_all()
    user_label.place_forget()
    list_disp.pack(pady=10)

    box.delete(0, tk.END)

    if not budgets:
        box.insert(tk.END, "No categories available.")
    else:
        for cname, budget in budgets.items():
            box.insert(tk.END, f"Category: {cname}")

            if not budget.expenses_dict:
                box.insert(tk.END, "  (no expenses yet)")
            else:
                for tp, entries in budget.expenses_dict.items():
                    if isinstance(entries, list):
                        for i, amt in enumerate(entries, start=1):
                            box.insert(tk.END, f"  {tp} #{i}: ${amt}")
                    else:
                        box.insert(tk.END, f"  {tp}: ${entries}")

            
            total = sum(
                sum(v) if isinstance(v, list) else v
                for v in budget.expenses_dict.values()
            )
            box.insert(tk.END, f"  Total: ${total}")
            box.insert(tk.END, "")

    box.pack(pady=10)
    back_button.pack(pady=15)

def go_financial_status():
    hide_all()
    user_label.place_forget()

    # ttl of categories
    total = sum(b.get_expenses() for b in budgets.values())

    balance = functions.calc_balance(income, total)
    msg = functions.financial_status(balance)

    label5.pack(pady=10)
    status_label.config(text=f"Balance: ${balance:.2f}")
    status_label.pack(pady=10)
    status_msg_label.config(text=msg)
    status_msg_label.pack(pady=5)
    chart_button.pack(pady=10)
    back_button.pack(pady=10)

button2 = tk.Button(window, text="Create New Expenses Category", font=("Montserrat", 12), command=go_create_category)
button3 = tk.Button(window, text="Add Expenses into Category", font=("Montserrat", 12), command=go_add_expenses)
button4 = tk.Button(window, text="Display Expenses List", font=("Montserrat", 12), command=go_display_expenses)
button5 = tk.Button(window, text="My Financial Status", font=("Montserrat", 12), command=go_financial_status)
button6 = tk.Button(window, text="Save Changes", font=("Montserrat", 12))
button7 = tk.Button(window, text="Exit Program", font=("Montserrat", 12), command=window.destroy)

main_buttons = [button2, button3, button4, button5, button6, button7]




label2 = tk.Label(window, text="Create New Expenses Category", font=("Montserrat", 14))
category_entry = tk.Entry(window, font=("Montserrat", 12))

def create_category():
    name = category_entry.get().strip()

    budgets[name] = Budget(name)
    budgets[name].write_to_file()

    category_entry.delete(0, tk.END)
    reset_dropdown()

    show_main_menu()
    status_msg.config(text=f"Category '{name}' created!", fg="green")

create_button = tk.Button(window, text="Create Category", font=("Montserrat", 12), command=create_category)



label3 = tk.Label(window, text="Add Expenses into Category", font=("Montserrat", 14))
expense_type_entry = tk.Entry(window, font=("Montserrat", 12))
expense_amount_entry = tk.Entry(window, font=("Montserrat", 12))

def add_expense_to_category():
    category = expense_dropdown.get()
    expense_type = expense_type_entry.get().strip()
#doesn't work
    try:
        amount = float(expense_amount_entry.get().strip())
    except ValueError:
        status_msg.config(text="Error: Amount must be numeric.", fg="red")
        return

    budgets[category].add_expense(expense_type, amount)
    status_msg.config(text=f"Added ${amount} to {category} ({expense_type}).", fg="green")

    expense_amount_entry.delete(0, tk.END)

add_expense_button = tk.Button(window, text="Add Expense", font=("Montserrat", 12), command=add_expense_to_category)


# disp changes

list_disp = tk.Label(window, text="Display Expenses List", font=("Montserrat", 14))
box = tk.Listbox(window, width=50, height=10, font=("Montserrat", 12))


label5 = tk.Label(window, text="My Financial Status", font=("Montserrat", 14))
status_label = tk.Label(window, text="Your status will appear here", font=("Montserrat", 12))
status_msg_label = tk.Label(window, text="", font=("Montserrat", 12), fg="blue")

def show_chart():
    if not budgets:
        status_msg.config(text="Error: No categories to chart.")
        return

    categories = []
    totals = []

    for name, budget in budgets.items():
        categories.append(name)
        total = sum(
            sum(v) if isinstance(v, list) else v
            for v in budget.expenses_dict.values()
        )
        totals.append(total)

    plt.figure(figsize=(6, 4))
    plt.bar(categories, totals, color='skyblue')
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Spent ($)")
    plt.tight_layout()
    plt.show()

chart_button = tk.Button(window, text="Show Spending Chart", font=("Montserrat", 12), command=show_chart)


def save_all_categories():
    for budget in budgets.values():
        budget.write_to_file()
    status_msg.config(text="All categories saved!", fg="green")

button6.config(command=save_all_categories)


back_button = tk.Button(window, text="Return to Main Menu", font=("Montserrat", 12), command=show_main_menu)


window.mainloop()
