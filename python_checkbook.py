user_id = input("Please enter your user identification: ").strip() 
                # to take out blank spaces
print()         # add blank rows for spacing
print(f"~~~ Welcome {user_id} to your terminal checkbook at the International Bank of Paducah! ~~~")



select_option = 1 
                #select option to enter the while loop
while int(select_option) != 4: 
                #!= 4 so the loop only runs for options 1 -3. Option 4 will exit
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



    while select_option < 1 or select_option > 4: 
                #if they put in the wrong integer, the loop will repeat until the user puts in a valid number
        select_option = input('Invalid choice. Please try again. ') 
                #I know this will error if input is not a digit, not sure how to correct at this point.
        select_option = int(select_option) 
                #cast string from input as an integer



    with open("debit_credit_log.txt", "r") as a: 
                #read the last line of the txt file to get the balance
                # https://www.youtube.com/watch?v=Uh2ebFW8OYM 
                # https://www.geeksforgeeks.org/reading-writing-text-files-python/
        linelist = a.readlines() 
                #list of all the balances in the file
        balance = float(linelist[len(linelist)-1]) 
                #will find the last row balance and read it.
    


    if select_option == 1:
        print("Your current balance is $%.02f." %balance)
                # https://stackoverflow.com/questions/560517/make-a-float-only-show-two-decimal-places
        


    elif select_option == 2:
        withdrawal = input('How much would you like to withdraw? ').strip()
        withdrawal = float(withdrawal)
        while withdrawal > balance:
                #verify the account has enough money to prevent an overdraft.
            withdrawal = input('Your withdrawal request exceeds your account balance. Please enter a new amount: ')
            withdrawal = float(withdrawal) 
                # will loop around until they put in an amount less than or equal to the balance
        balance -= withdrawal
        with open('debit_credit_log.txt', "a") as f: 
                #append new data to txt file
            f.write(str(balance) + "\n") 
                #cast float balance to string for writing to the text file
                #write new balance to a new line (otherwise will append to the end of the preceding numbers)
                #https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
        print(f'Withdrawal successful. Your new balance is $%.02f.' %balance)



    elif select_option == 3:    
        deposit = input('How much would you like to deposit? ').strip()
        deposit = float(deposit)
        balance += deposit
        with open('debit_credit_log.txt', "a") as f:
            f.write(str(balance) + "\n")
        print(f'Your new balance is $%.02f.' %balance)
    


    elif select_option == 4:
        print(f"Thank you for banking with us, {user_id}!")
        print()
        print("We're a small town bank with a global reach!")
    


# Next steps (fixing the shortcomings)
# 1. rewrite the code so it is a function, to make it more compact and versatile
# 2. figure out how to add a ',' in the thousands' place of the amount
# 3. add isdigit so the menu only accept string numbers
# 4. find something that would allow me to reject float values that include non-numeric characters

    





