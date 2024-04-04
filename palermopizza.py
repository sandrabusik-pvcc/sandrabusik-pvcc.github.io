# Name: Tre Williams, Sandra Busik
# Prog Purpose: Compute and display a receipt for items purchsed

import datetime
# define menu
S = 9.99
M = 12.99
L = 17.99
E = 21.99

DRINK = 3.99
ORDER_OF_BREADSTICKS = 6.99
SALES_TAX_RATE = .055


#define global variables
inout_pizza_size =0
inout_pizza_amt=0
inout_num_drinks =0
inout_num_breadsticks=0
pizza_cost = 0
drink_cost=0
breadstick_cost = 0
subtotal=0
sales_tax_amt =0
pizza=0
total=0
balance=0


############### define program functions ############
def main():
    promp_in = "\nWould you like to make another order? (Y?N): "
    goodbye_msg = "Thank you for your order."
    more_data = True

    while more_data:
        display_menu()
        get_pizza_size_user_data()
        get_pizza_amt_user_data()
        get_num_drinks()
        get_num_breadsticks()
        perform_calculations()
        display_receipt()

        yesno = input(promp_in)
        if (yesno.upper() == "N"):
            more_data = False
            print(goodbye_msg)

def get_pizza_size_user_data():
    global inout_pizza_size
    inout_pizza_size =(input("Enter a S, M, L, or X: "))

def get_pizza_amt_user_data():
    global inout_pizza_amt
    inout_pizza_amt = int(input("Enter number of pizzas: "))

def get_num_drinks():
    global inout_num_drinks
    inout_num_drinks = int(input("Enter number of drinks: "))

def get_num_breadsticks():
    global inout_num_breadsticks
    inout_num_breadsticks = int(input("Enter number of breadsticks: "))    

def perform_calculations():
    global pizza, total, pizza_cost, drink_cost, breadstick_cost, subtotal, sales_tax_amt
    if inout_pizza_size.upper() == "S":
        pizza = 9.99
    elif inout_pizza_size.upper() == "M":
            pizza = 12.99
    elif inout_pizza_size.upper() == "L":
            pizza = 12.99
    elif inout_pizza_size.upper() == "X":
            pizza = 12.99
    pizza_cost = inout_pizza_amt * pizza
    drink_cost = inout_num_drinks * DRINK
    breadstick_cost = inout_num_breadsticks * ORDER_OF_BREADSTICKS
    subtotal = pizza_cost + drink_cost + breadstick_cost
    sales_tax_amt =subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax_amt


def display_menu():
    line = '-------------------------------------------------'
    title = 'Palermo Pizza Menu'
    currency = '8,.2f'
    
    print (title)
    print (line)
    print ('Please choose a pizza size, drink, and if you would like breadsticks.')
    print (line)
    print ('Pizza Size:')
    print ('S  Small                     $ ' + format(S, currency) )
    print ('M  Medium                    $ ' + format(M, currency) )
    print ('L  Large                     $ ' + format(L, currency) )
    print ('X  Extra Large               $ ' + format(E, currency))
    print (line)
    print ('Drink                        $ ' + format(DRINK, currency))
    print (line)
    print ('Breadsticks                  $ ' + format(ORDER_OF_BREADSTICKS, currency))
    print (line)

def display_receipt():
    title2 = '*******Palermo Pizza********'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]
    line = '-------------------------------------------------'
    currency = '8,.2f'
    
    print (title2)
    print (dt_full)
    print (dt_short)
    print (line)
    print ('Pizza Size:                  $ ' + format(pizza))
    print ('Number of pizzas:              ' + format(inout_pizza_amt, currency))
    print ('Number of drinks:              ' + format(inout_num_drinks, currency))
    print ('Number of breadsticks:         ' + format(inout_num_breadsticks, currency))
    print ('Sales tax                    $ ' + format(SALES_TAX_RATE, currency))
    print ('Total                        $ ' + format(total, currency))
########## call on main program to execute ############
main()
