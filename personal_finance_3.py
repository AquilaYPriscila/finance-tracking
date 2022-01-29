import Teststatement

class Transaction():
    """Record of money exchange"""
    def __init__(self):
        self.amount = 0

class Income(Transaction):
    """Record of receiving money"""
    category1 = ["Employment","Investment","Other"]
    print("These are you income categories:")
    for x in category1:
        print(x)

    def input_income():
        add_income = input("Enter the amount for all the Category separated by space:\n")

        income_list = add_income.split()
        print('Income: ', income_list)

        for i in range(len(income_list)):
            income_list[i] = int(income_list[i])

        print("Total Income: $", sum(income_list),"\n")
        return sum(income_list)

total_income = Income.input_income()


class Expense(Transaction):
    """Record of payment"""
    category2 = ["Rent","Utilities","Food","Other"]
    print("These are you expense categories:")
    for x in category2:
        print(x)
 
    def input_expense():
        add_expense = input("Enter the amount for all the Category separated by space:\n")
        expense_list = add_expense.split()
        print('Income: ', expense_list)

        for i in range(len(expense_list)):
            expense_list[i] = int(expense_list[i])
        
        print("Total Expense: $", sum(expense_list),"\n")
        return sum(expense_list)

total_expense = Expense.input_expense()

class Savings():
    """Represents monthly savings."""
    def __init__(self):
        self.binary = [True,False]

# Use while to input savings goal percentage
# Use if-else to see if savings goal is met

    def savings_goal():
        while True:
            try:
                goal = float(input("Enter your numeric percentage savings goal:\n"))
                break
            except ValueError:
                print("Oops! That was not a valid number. Please try again. Thank you!")
        print("Your savings rate goal is ",goal,"% of your income.")

        savings = total_income-total_expense
        save_percent = savings/total_income*100
        print("You are saving: $", savings)

        if save_percent < goal:
            print("Sadly, your savings rate of {:.2f}".format(save_percent),"% was less than your savings goal of", goal,"%.")
        else:
            print("Congratulations! You wanted to save", goal,"%, and you saved {:.2f}".format(save_percent),"%!.")
        return savings

amount_saved = Savings.savings_goal()

Teststatement.print_statement(total_income,total_expense,amount_saved)