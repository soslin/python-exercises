user_id = input("Please enter your user identification: ").strip()
print()
print(f"~~~ Welcome {user_id} to your terminal checkbook at the International Bank of Paducah! ~~~")

with open("debit_credit_log.txt", "r") as a:
    balance = float(a.readline()[-1])
    print(balance) #balance comes back 0.0

while True:
    print()
    print("What would you like to do?")
    print()
    print("\t 1) View current balance")
    print("\t 2) Make a withdrawal")
    print("\t 3) Make a deposit)")
    print("\t 4) Exit")
    print()
    select_option = input("Please select from options 1 - 4: ").strip()
    select_option = int(select_option)

    if select_option < 1 or select_option > 4:
        print('Invalid choice. Please try again.')
        continue

    if select_option == 1:
        print(f"Your current balance is {balance}.") #fix balance
        print('What would you like to do next?')
        continue

    if select_option == 2:
        while True:
            withdrawal = input('How much would you like to withdraw? ').strip()
            withdrawal = -float(withdrawal)
            if abs(withdrawal) > balance:
                print('Your withdrawal request exceeds your account balance. Please enter a new amount.')
                continue
            else:
                balance_after_withdrawal = balance - withdrawal # how get this amount to append to the text file?
                with open('debit_credit_log.py', "a"))
                print(f'Withdrawal successful. Your new balance is {balance}')
                print('What would you like to do next?')
                continue
        continue


    if select_option == 3:    
        deposit = input('How much would you like to deposit? ').strip()
            deposit = float(deposit)
            print(f'Your new balance is {current_balance}')
            continue

    if select_option == 4:
        print("Thank you for banking with us!")
        break
break
    





