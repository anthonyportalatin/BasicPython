#This program will run as a cash register

choice = 0
status = 0
cash = 0

print('Welcome to the cash register!\n')

while (status != 1):

    print('\nSelect the items you wish to purchase:\n')
    choice = int(input('1) Burger - $2.99\n2) Taco - $1.99\n3) Wrap - $4.50\n4)\
 Drink - $1.00\n5) Done\n'))

    if (choice == 1):
        cash = cash + 2.99
        print('\nSubtotal: ', cash)
    elif (choice == 2):
        cash = cash + 1.99
        print('\nSubtotal: ', cash)
    elif (choice == 3):
        cash = cash + 4.50
        print('\nSubtotal: ', cash)
    elif (choice == 4):
        cash = cash + 1.00
        print('\nSubtotal: ', cash)
    elif (choice == 5):
        tax = float(input('\nPlease insert the tax percent: '))
        print('\nSubtotal: $%.2f' % cash)
        tax = cash * tax / 100
        print('Tax: $%.2f' % tax)
        total = cash + tax
        print('Total: $%.2f' % total)
        status = 1