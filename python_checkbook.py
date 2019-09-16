user_id = input("Please enter your user identification ").strip() #always take out stray blank spaces with the input. 
print()
print(f"~~~ Welcome {user_id} to your terminal checkbook! ~~~")

starting_balance = 1_000.00

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

