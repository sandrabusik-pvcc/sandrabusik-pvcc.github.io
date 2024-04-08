# Name: Sandra Busik
# Prog Purpose: This program finds the personal property tax for 6 mon
#  PPT rate: 4.2%
# Relief rate: 3% (for personal vehicles only)

import datetime

##################  define global variables   #################################
# define tax rate and prices
PPT_RATE = .042
RELIEF_RATE = .33

# define global variables
assessed_value = 0
relief_yn = "N"

#################  define program functions  ###################################
def main():
    promp_in = "\nIs there another PPT payer(Y or N) "
    goodbye_msg = "Personal Property Taxes are due DEC 5, 2024"
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input(promp_in)
        if (yesno.upper() == "N"):
            more = False
            print(goodbye_msg)

def get_user_data():
    global assessed_value, relief_yn
    assessed_value = int(input("What is the assessed value of the vehicle? "))
    relief_yn = input("Is the vehicle eligible for relief? (Y/N) ")
    relief_yn = relief_yn.upper()
                      
def perform_calculations():
    global ppt_amount_annual,ppt_amount_6months, relief_amount, aount_owed, biannual_amount_owed
    ppt_amount_annual = assessed_value * PPT_RATE

    if relief_yn == "Y":
        relief_amount = ppt_amount_annual * RELIEF_RATE
    else:
        relief_amount = 0 


    amount_owed = ppt_amount_annual - relief_amount
    biannual_amount_owed = amount_owed / 2
    

def display_results():
    line = '-------------------------------------'
    currency = '8,.2f'
    date = str(datetime.datetime.now())
    title1 = '****Personal Property Tax ****'
    title2 = 'City of Charlottesville, VA'
    tax_yr_title = 'Tax Year'
    tax_yr = '2023/2'
    months = 6
    regular = '8,.0f'
    
    print(line)
    print(title1)
    print(title2)
    print(date)
    print(line)
    print(tax_yr_title)
    print(tax_yr)
    print('Assessed Value      $ ' + format(assessed_value, currency ))
    print('Biannual Tax Amount $ ' + format(ppt_amount_annual, currency))
    print('Relief              $ ' + format(relief_amount, currency ))
    print('Tax Due             $ ' + format(biannual_amount_owed, currency ))
    print(line)
    print('TOTAL AMOUNT DUE    $ ' + format(biannual_amount_owed, currency ))
    print(line)
    
    #################  call on main program to execute #############################
main()
