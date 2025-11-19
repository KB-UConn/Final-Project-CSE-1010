def calc_balance(income, expenses):
    print(f"Total exexpenses are {expenses}")
    balance = income - expenses
    return balance

def financial_status(balance):
    if balance > 0:
        return("Great! You are saving money!")
    elif balance == 0:
        return("You are breaking even.")
    else:
        return("**WARNING** You are overspending!")
