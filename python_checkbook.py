user_id = input("Please enter your user identification: ").strip() # to take out blank spaces
print()
print(f"~~~ Welcome {user_id} to your terminal checkbook at the International Bank of Paducah! ~~~")

select_option = 1 #prime select option to enter the while loop
while int(select_option) != 4: #!= 4 is that the loop only runs for options 1 -3. Option 4 will exit
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

    while select_option < 1 or select_option > 4: #if they put in the wrong integer, the loop will repeat
        select_option = input('Invalid choice. Please try again. ') #I know this will error if input is a nondigit
        select_option = int(select_option)

    with open("debit_credit_log.txt", "r") as a: #read the last line of the txt file to get the balance
        linelist = a.readlines() #list of all the balances in the file
        balance = float(linelist[len(linelist)-1]) #will find the last row balance and read it.
    
    if select_option == 1:
        print(f"Your current balance is {balance}.")
        
    elif select_option == 2:
        withdrawal = input('How much would you like to withdraw? ').strip()
        withdrawal = float(withdrawal)
        while abs(withdrawal) > balance:
            withdrawal = input('Your withdrawal request exceeds your account balance. Please enter a new amount: ')
            withdrawal = float(withdrawal) # will loop around until they put in an amount less than or equal to the balance
        balance = balance - withdrawal
        with open('debit_credit_log.txt', "a") as f:
            f.write(str(balance) + "\n")
        print(f'Withdrawal successful. Your new balance is {balance}')

    elif select_option == 3:    
        deposit = input('How much would you like to deposit? ').strip()
        deposit = float(deposit)
        balance += deposit
        with open('debit_credit_log.txt', "a") as f:
            f.write(str(balance) + "\n")
        print(f'Your new balance is {balance}')
    
    elif select_option == 4:
        print("Thank you for banking with us!")
    

    





