choice = 0
expenses = []
class expense():
    def __init__(self,amount,category,description,date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    

while choice != '6':

    print('''1.ADD NEW EXPENSE
    2.VIEW EXPENSES
    3.DELETE EXPENSES
    4.SEARCH EXPENSES
    5.SAVE CHANGES
    6.QUIT APPLICATION''')

    choice = input('enter 1-6 for choice: ')
    if choice == '1':
        exp = input('expense: ')
        exp = exp.split(',')
        expense1 = expense(exp[0],exp[1],exp[2],exp[3])
        expenses.append(expense1)
        for i in expenses:
            print(i.amount,i.category,i.description,i.date)