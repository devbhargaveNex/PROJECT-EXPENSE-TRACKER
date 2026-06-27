choice = 0
expenses = []
def add(e):
    e = e.rstrip('\n')
    exp = e.split(',')
    expense1 = expense(exp[0],exp[1],exp[2],exp[3])
    expenses.append(expense1)
class expense():
    def __init__(self,amount,category,description,date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    
with open('expenses.txt','r') as f:
    for line in f:
        if line != '':
            add(line)
        else:
            break

while choice != '6':

    print('''   1.ADD NEW EXPENSE
    2.VIEW EXPENSES
    3.DELETE EXPENSES
    5.SAVE CHANGES
    6.QUIT APPLICATION''')
    choice = input('enter 1-6 for choice: ')
    if choice == '1':
        exp = input('expense: ')
        add(exp)
    elif choice == '2':
        for i in expenses:
            print(f'amount={i.amount} category={i.category} description={i.description} date={i.date}')
    elif choice == '5':
        with open('expenses.txt','w') as f:
            f.write('')
        for i in expenses:
            with open('expenses.txt','a') as f:
                f.write(i.amount)
                f.write(',')
                f.write(i.category)
                f.write(',')
                f.write(i.description)
                f.write(',')
                f.write(i.date)
                f.write('\n')
    elif choice == '3':
        dele = input('enter the expense to delete: ')
        dels = dele.split(',')
        n = -1
        for i in expenses:
            n += 1
            if i.amount == dels[0]:
                if i.category == dels[1]:
                    if i.description == dels[2]:
                        if i.date == (dels[3]):
                            rm = expenses.pop(n)
                            print(rm)