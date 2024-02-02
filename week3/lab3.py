#1.1
num_items = 0
run_quantity_loop = True
run_cost_loop = True
run_member_loop = True
while run_quantity_loop:
    user_input = input("Enter a quantity: ")

    if user_input.isnumeric():
        num_items = int(user_input)
        run_quantity_loop = False
    else:
        print("Invalid input. Please enter a valid number.")

print("You entered:", num_items)

#1.2

while run_cost_loop:
    cost_in_cents_input = input("Enter the cost per item in cents: ")

    if cost_in_cents_input.isnumeric():
        cost_in_cents = int(cost_in_cents_input)
        
        cost_in_dollars = cost_in_cents / 100.0
        run_cost_loop = False
    else:
        print("Invalid input. Please enter a valid integer representing cost in cents.")

print("Cost per item in dollars:", cost_in_dollars)


#2.1

# if num_items < 10:
#     total_cost = num_items * cost_in_dollars
# elif 10 <= num_items < 20:
#     total_cost = num_items * 0.9 * cost_in_dollars  # 10% discount
# else:
#     total_cost = num_items * 0.8 * cost_in_dollars  # 20% discount

# print(f"Total cost for {num_items} items: ${total_cost:.2f}")

# 2.1 and 2.2

while run_member_loop:
    member_input = input("Are you a store member? (Enter 'yes' or 'no'): ").lower()

    if member_input == 'yes':
        member = True
        run_member_loop = False
    elif member_input == 'no':
        member = False
        run_member_loop = False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

if member:
    if num_items < 10:
        total_cost = num_items * 0.85 * cost_in_dollars  # 15%
    else:
        total_cost = num_items * 0.75 * cost_in_dollars  # 25% 
else:
    if num_items < 10:
        total_cost = num_items * cost_in_dollars
    elif 10 <= num_items < 20:
        total_cost = num_items * 0.9 * cost_in_dollars  # 10% discount
    else:
        total_cost = num_items * 0.8 * cost_in_dollars  # 20% discount

print(f"Total cost for {num_items} items: ${total_cost:.2f}")