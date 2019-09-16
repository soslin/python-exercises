user_id = input("Please enter your user identification ").strip() #always take out stray blank spaces with the input. 
print()
print(f"~~~ Welcome {user_id} to your terminal checkbook at Bank of Usury! ~~~")

import debit_credit log as balance
## current_balance = starting_balance - withdrawal + deposit ## needs to be moved down

while True:
    print() #blank line
    print("What_would_you_like_to_do?")
    print()
    print("\t 1) view current balance")
    print("\t 2) record a debit (withdraw)")
    print("\t 3) record a credit (deposit)")
    print("\t 4) exit")
    print()
    select_option = input("Please select from options 1 - 4: ").strip()
    select_option = int(select_option) # convert text string from input to an integer

    if select_option < 1 or select_option > 4:
        print('Invalid choice. Please try again.')
        break

    if select_option == 1:
        print(f"Your current balance is {balance}.")
        print('What would you like to do next?')
        break


    if select_option == 2:
        while True:
            withdraw = input('How much would you like to withdraw? ').strip()
            withdraw = float(withdraw)
            if withdraw > balance:
                print('Your withdrawal request exceeds your account balance. Please enter a new amount.')
                break
            else:
                ## balance - withdraw = open('debit_credit_log.py', "ra"))
            print(f'Withdrawal successful. Your new balance is {balance}')
    
            print('What would you like to do next?')
            break


    if select_option == 3:    
        deposit = input('How much would you like to deposit? ').strip()
            deposit = float(deposit)
            print(f'Your new balance is {current_balance}')
            break

    if select_option == 4:
        print("Thank you for banking with us!")
        break
break
    





