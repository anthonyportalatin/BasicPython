#This program runs a basic calculator

round = 1
choice = 0

while (round==1):
    print("\nWelcome to the calculator!\n")
    print("Please choose what you want to do:")
    choice = input("Press 1-Sum\nPress 2-Substract\n\
Press 3-Multiply\nPress 4-Divide\nPress 5-Quit\n")

    if(choice=='1'):
        print("\nPlease write the two numbers you want to add.")
        number1=int(input("First Number: "))
        number2=int(input("Second Number: "))
        total = number1 + number2
        print("Total: ", total)
        
    elif(choice=='2'):
        print("\nPlease write the two numbers you want to subtract.")
        number1=int(input("First Number: "))
        number2=int(input("Second Number: "))
        total = number1 - number2
        print("Total: ", total)
        
    elif(choice=='3'):
        print("\nPlease write the two numbers you want to multiply.")
        number1=int(input("First Number: "))
        number2=int(input("Second Number: "))
        total = number1 * number2
        print("Total: ", total)
        
    elif(choice=='4'):
        print("\nPlease write the two numbers you want to divide.")
        number1=int(input("First Number: "))
        number2=int(input("Second Number: "))
        total = number1 / number2
        print("Total: ", total)

    elif(choice=='5'):
        round = 0
        
    
