amount = []
category = []
description = []
date = []
choice = 0
while choice != '6':

    print(''' 1.ADD NEW EXPENSE 
    2.VIEW EXPENSES 
    3.DELETE EXPENSES 
    4.SEARCH EXPENSES 
    5.SAVE CHANGES
    6.QUIT APPLICATION''')

    
    choice = input('enter 1-6 for choice: ')
    if choice == '1':
        expense = input('expense: ')
        expensedetail = expense.split(",")
        print(expensedetail)
        amount.append(expensedetail[0])
        category.append(expensedetail[1])
        description.append(expensedetail[2])
        date.append(expensedetail[3])

    else:
        pass

    print(amount)