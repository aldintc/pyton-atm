
import time     

print("Welcome to Dominican bank\n")
restart = ('y')
chances = 3
balance = 2741.21

while chances >= 0:
    pin = int(input("please enter pin number: "))
    if pin == (4367):
        print('You entered pin correctly\n')
        while restart not in ('n' , 'N' , 'no' , 'NO'):
            print('please press 1 for your balance\n')
            print('please press 2 to make a withdraw\n')
            print('please press 3 to pay in\n')
            print('please press 4 to return card\n')
            option = int(input('What would you like to do?  '))
            if option == 1:
                print('your balance is $' , balance , '\n')
                restart = input('would you like to do something else?')
                if restart in ('n' , 'N' , 'no' , 'NO'):
                    print('Thank You')
                    break
            
            elif option ==2:
                option2 = ('y')
                withdrawl = float(input('How much would you like to withdraw? \n $10/$20/$50/$100 for other enter 1:  '))
                if withdrawl in [10 , 20 , 50 , 100]:
                    balance = balance - withdrawl
                    print('your balance is now $', balance)
                    restart = input('would you like to do something else?')
                    if restart in ('n' , 'N' , 'no' , 'NO'):
                        print('Thank You')
                        break
                
                elif withdrawl != [10 , 20 , 50 , 100]:
                    print('invalid amount, please retry\n')
                    restart('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please enter desired amount: '))

            elif option == 3:
                pay_in = float(input('how much would you like to pay in? '))
                balance = balance + pay_in
                print("\nYour balance is now $" , balance)
                restart = input('would you like to do something else?')
                if restart in ('n' , 'N' , 'no' , 'NO'):
                        print('Thank You')
                        break

            elif option == 4:
                print("Please wait while we return you card...\n")
                time.sleep(3)
                print('Thank you for using our services')
                break
            else:
                print('Please enter correct Pin number. \n')
                restart = ('y')

    elif pin != (4367):
        print("pin incorrect")
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries")
            break
