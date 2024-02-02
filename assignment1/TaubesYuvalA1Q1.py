MB_PST = 7 #% of tax
MB_GST = 5 #% of tax
ON_HST = 13 #% of tax

PROFIT_MARGIN = 40 # % of profit

REWARD_POINTS = 8 # reward points earned per purchase
STAFF_DISCOUNT = 5 # % off

SHIPPING_COST = 8 # $ for shipping under 200$

#costs of the books
book1 = 10
book2 = 35
book3 = 25
book4 = 15
book5 = 30
book6 = 45

BOOK2_DISCOUNT = 20 # %
BOOK3_DISCOUNT = (5/book3) * 100 # %
BOOK5_DISCOUNT = 10 # %
BOOK6_DISCOUNT = (10/book6) * 100 # %

run_start_menu = True
#no texes
retail_cost = 0
sale_discount = 0
staff_discount_applied = 0
total_discount = 0
cost_amount = 0
reward_points_earned = 0
tax_amount = 0
shipping_cost = 0
pst = 0
gst = 0
hst = 0
#including taxes
total_cost = 0

#pre tax
total_bookstore_profit = 0

while(run_start_menu):
    run_quantity_menu = True
    province_input = input("what province are you shopping in?(ex. MB, ON):")
    province = None

    if(province_input.lower() == "mb"):
        province = "MB"
    elif(province_input.lower() == "on"):
        province = "ON"
    else:
        print("Not a valid input")
        continue
    
    is_staff_input = input("are you a staff (ex. Yes or No)")
    is_staff = False
    if is_staff_input.lower() == "yes":
        is_staff = True
        

    print("Welcome to my bookstore")
    book_selection_input = input("Please enter the book you want (ex. book1 - book6):")
    book_selection = None
    discount_per_book = 0

    if book_selection_input == "book1":
        print("book 1 was selected")
        book_selection = book1
    elif book_selection_input == "book2":

        print("book 2 was selected")
        book_selection = book2
        discount_per_book = BOOK2_DISCOUNT

    elif book_selection_input == "book3":
        print("book 3 was selected")
        book_selection = book3
        discount_per_book = BOOK3_DISCOUNT

    elif book_selection_input == "book4":
        print("book 4 was selected")
        book_selection = book4

    elif book_selection_input == "book5":
        print("book 5 was selected")
        book_selection = book5
        discount_per_book = BOOK5_DISCOUNT

    elif book_selection_input == "book6":
        print("book 6 was selected")
        book_selection = book6
        discount_per_book = BOOK6_DISCOUNT

    else:
        print("not a valid selection")
        run_quantity_menu = False

    while(run_quantity_menu):
        quantity=None
        quantity_input = (input("Please enter how many you want of {}:".format(book_selection_input)))
        if(quantity_input.isdecimal() == False):
            continue
        
        quantity=int(quantity_input)

        run_quantity_menu = False

        retail_cost = book_selection * quantity

        sale_discount = (discount_per_book / 100) * retail_cost

        staff_discount_applied = retail_cost * (STAFF_DISCOUNT / 100)

        total_discount = staff_discount_applied + sale_discount

        cost_amount = retail_cost - sale_discount - staff_discount_applied

        reward_points_earned = quantity * REWARD_POINTS

        if province == "MB":
            pst = (MB_PST / 100) * cost_amount
            gst = (MB_GST / 100) * cost_amount
        else:
            hst = (ON_HST/ 100) * cost_amount

        tax = pst + gst + hst

        if(cost_amount >= 200):
            shipping_cost = 0
        else:
            shipping_cost = 8
        
        total_cost = cost_amount + shipping_cost + tax

        total_bookstore_profit = cost_amount * (PROFIT_MARGIN / 100)
        #attempting to check if its an int but idk if I have the tools without a try catch
        # if(isinstance(quantity, int)):
        #     print("you want {} of books".format(quantity))
        # else:
        #     print("Invalid Selection")

    keep_shopping = input("do you want to keep shopping? (ex. Yes or No)")
    if keep_shopping.lower() == "no":
        print("the retail cost is ${}".format(retail_cost))
        print("you saved ${:.2f} from sales".format(sale_discount))
        print("you saved ${:.2f} from the staff discount".format(staff_discount_applied))
        print("you saved a total of ${:.2f}".format(total_discount))
        print("the new total before taxes is ${}".format(cost_amount))
        print("you earned {} reward points".format(reward_points_earned))
        print("pst: ${:.2f} \ngst: ${:.2f} \nhst: ${:.2f}".format(pst, gst, hst))
        print("the shipping cost is ${:.2f}".format(shipping_cost))
        print("the total cost is ${:.2f}".format(total_cost))
        print("The bookstore earned ${:.2f}".format(total_bookstore_profit))

        run_start_menu = False


print("thank you for shopping with us today")



    

    
