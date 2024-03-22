# Name: Sandra Busik
# Prog Purpose: Displays a customer receipt for Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee rate: 10%
#   Sales tax rate: 6.2%

import datetime

##################  define global variables   #################################
# define tax rate and prices
SALES_TAX_RATE = .062
PR_ADULT_MEAL = 19.95
PR_CHILD_MEAL = 11.95
SERVICE_FEE_RATE = .10

# define global variables
num_adult_meals = 0
num_child_meals = 0
subtotal_adult = 0
subtotal_child = 0
subtotal = 0
sales_tax_adult = 0
sales_tax_child = 0
service_fee_adult = 0
service_fee_child = 0
total_cost_adult = 0
total_cost_child = 0
total = 0

#################  define program functions  ###################################
def main():
    prompt_in = "Do you have another order (Y or N) "
    goodbye_msg = "Thank you for coming to Branch Barbeque Buffet!  Enjoy your meal."
    more_data = True

    while more_data:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input(prompt_in)
        if (yesno.upper() == "N"):
            more_data = False
            print(goodbye_msg)

def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("Number of adults in the party: "))
    num_child_meals = int(input("Number of children in the party: "))

def perform_calculations():
    global subtotal_adult, subtotal_child, sales_tax, total_cost_adult, total_cost_child, subtotal, sales_tax_adult, sales_tax_child, service_fee_adult, service_fee_child, total_cost_adult, total_cost_child, total
    subtotal_adult = num_adult_meals * PR_ADULT_MEAL 
    subtotal_child = num_child_meals * PR_CHILD_MEAL
    subtotal = subtotal_adult + subtotal_child
    sales_tax_adult = subtotal_adult * SALES_TAX_RATE
    sales_tax_child = subtotal_child * SALES_TAX_RATE
    service_fee_adult = subtotal_adult * SERVICE_FEE_RATE
    service_fee_child = subtotal_child * SERVICE_FEE_RATE
    total_cost_adult = subtotal_adult + sales_tax_adult + service_fee_adult
    total_cost_child = subtotal_child + sales_tax_child + service_fee_child
    total = total_cost_adult + total_cost_child

def display_results():
    line = '-------------------------------------'
    currency = '8,.2f'
    date = str(datetime.datetime.now())
    title1 = '****BRANCH BARBEQUE ****'
    
    
    print(line)
    print(title1)
    print(date)
    print(line)
    print('Adult Total        $ ' + format(total_cost_adult, currency ))
    print('Child Total        $ ' + format(total_cost_child, currency ))
    print('Subtotal           $ ' + format(subtotal, currency ))
    print('Service Fee        $ ' + format(SERVICE_FEE_RATE, currency ))
    print('Sales Tax          $ ' + format(SALES_TAX_RATE, currency ))
    print('Total              $ ' + format(total, currency ))
    print(line)
    
    #################  call on main program to execute #############################
main()
