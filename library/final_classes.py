class Budget:
    def __init__(self, expense_type):
        self.expense_type = expense_type
        self.expenses_dict = {}
        self.expenses = []
        self.filename = f"{expense_type}.txt"
        self.load_from_file()
    
    def add_expense(self, type_, amount):
        if type_ in self.expenses_dict:
            self.expenses_dict[type_] += amount
        else:
            self.expenses_dict[type_] = amount
        self.expenses.append(amount)
        self.write_to_file()
        
        '''while True:
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
                    self.expenses_dict[type] = float(exp)
                    self.expenses.append(float(exp))
                    break
                except:
                    print()
                    print(" ## Error ## ")
                    print("Enter \"type Cost\" Format. For example, \"Oil 10\"")
                    print()
        self.write_to_file()   '''     
    
    def get_expenses(self):
        total = sum(self.expenses)
        print(f"\nTotal money you spent on {self.expense_type} is {total}")
        return total
    
    def get_expense_details(self):
        print(f"\nExpense Details:")
        for type, exp in self.expenses_dict.items():
            print(f"{type} : ${exp}")
    
    def write_to_file(self):
        with open(self.filename, "w") as data:
            for type_, exp in self.expenses_dict.items():
                data.write(f"{type_}:{exp}\n")
    
    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            type_, exp = line.split(":")
                            self.expenses_dict[type_] = float(exp)
                            self.expenses.append(float(exp))
                        except ValueError:
                            pass  # ignore bad lines
        except FileNotFoundError:
            pass