from pathlib import Path
file = Path("expenses.txt")
choice = 0
expenses = []
def add(e):
    e = e.rstrip('\n')
    exp = e.split(',')
    expense1 = expense(exp[0],exp[1],exp[2],exp[3])
    expenses.append(expense1)

def save():
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

class expense():
    def __init__(self,amount,category,description,date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

if file.is_file():
    with open('expenses.txt','r') as f:
        for line in f:
            add(line)
else:
    with open('expenses.txt','w') as f:
        pass

while choice != '5':

    print('''   1.ADD NEW EXPENSE
    2.VIEW EXPENSES
    3.DELETE EXPENSES
    4.SAVE CHANGES
    5.QUIT APPLICATION''')
    choice = input('enter 1-5 for choice: ')
    if choice == '1':
        exp = input('expense: ')
        e = exp.split(',')
        if len(e) == 4:
            add(exp)
        else:
            print('plese enter in format amount,category,description,date')
    elif choice == '2':
        for i in expenses:
            print(f'amount={i.amount} category={i.category} description={i.description} date={i.date}')
    elif choice == '4':
        if len(expenses) != 0:
            save()
        else:
            print('file is empty if you save the entire log gets deleted')
            yn = input('if you wish to continue type y if not type n: ')
            print(yn)
            if yn == 'Y':
                save()
            elif yn == 'N':
                print('action cancelled')
            else:
                print('please enter y or n only')
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
    else:
        print('please choose correct option')