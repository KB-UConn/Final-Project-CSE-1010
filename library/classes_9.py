class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.expenses = []
        self.categories = []
    
    def add_expenses(self):
        while True:
            try:
                num_expenses = int(input(f"Enter number of {self.expense_type} expenses you want to add (integer only):"))
                break
            except (TypeError, ValueError):
                print("** Wrong Input **, \n Please enter integers only!")
        print(f"Enter {self.expense_type} expenses in \"type Cost\" Format. For example, \"Milk 10\"")
        for i in range(num_expenses):
            while True:
                try:
                    type, exp = input(f"Enter expense {i+1}: ").split()
                    self.expenses.append(float(exp))
                    self.categories.append(type)
                    break
                except:
                    print()
                    print(" ## Error ## ")
                    print("Enter \"type Cost\" Format. For example, \"Oil 10\"")
                    print()
            
    def get_expenses(self):
        total = sum(self.expenses)
        print(f"\nTotal money you spent on {self.expense_type} is {total}")
        return total
    
    def get_expense_details(self):
        print(f"\nExpense Details:")
        for i in range(len(self.expenses)):
            print(f"{self.categories[i]} : {self.expenses[i]}")