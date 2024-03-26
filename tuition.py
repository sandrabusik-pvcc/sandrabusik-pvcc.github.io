# Name: Jaden Auville, Sandra Busik
# Prog Purpose: This program conputes PVCC college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

tuition_amt=0
inst_fee=0
act_fee=0
cap_fee=0
total=0
balance=0


############    define program functions ############
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations

############## define program functions ############
def main():
    promp_in = "\nWould you like to calculate tuition & fees for another student? (Y?N): "
    goodbye_msg = "Thank you for your order."
    more_data = True

    while more_data:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input(promp_in)
        if (yesno.upper() == "N"):
            more_data = False
            print(goodbye_msg)

def get_user_data():
    global inout, numcredits, scholarshipamt

    
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = float(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))


def perform_calculations():
    global tuition_amt, numcredits, cap_fee, inst_fee, act_fee, total, balance
    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
        cap_fee=0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE
    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE
    
    total= tuition_amt + inst_fee + act_fee + cap_fee
    balance= total - scholarshipamt


def display_results():
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]
    line = '-------------------------------------------------'
    currency = '8,.2f'
    print (dt_full)
    print (dt_short)
    print ('Piedmont Virginia Communnity College')
    print (line)
    print ('Tuition             $ ' + format(tuition_amt, currency) )
    print ('Capital Fee         $ ' + format(cap_fee, currency) )
    print ('Institution Fee     $ ' + format(inst_fee, currency) )
    print ('Activity Fee        $ ' + format(act_fee, currency) )
    print ('Scholarship Amount  $ ' + format(scholarshipamt, currency))
    print ('Balance             $ ' + format(balance, currency))
########## call on main program to execute ############
main()
