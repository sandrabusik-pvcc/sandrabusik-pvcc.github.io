#Name: Sandra Busik
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type =="DR":
                subtotal = ROOM_RATES[1] * num_nights

            else: subtotal = ROOM_RATES[2] * num_nights
                
#STUDENTS: COMPLETE THESE CALCULATIONS        
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total     = subtotal + salestax + occupancy
             
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)
            guest[i].append(grandtotal)


def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style = "background-color:#999999; font-family: Arial, Helvetica, sans-serif;background-image: url(wp-beach.png);">')
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    td8 ='<tr><td colspan = 8>'
    td7 = '<tr><td colspan = 7>'
    endtr = '</td></tr>\n'

    f.write("<table border = 3 style='background-color:#3366ff;margin:auto; color:white;'>")
    f.write(td8 +"<h1>Emerald Beach Hotel & Resort Guest Report</h1></tr></td>")
    f.write(td8 +"<h2 style='text-align: center;'>Guest Sales Report </h2></tr></td>")
    f.write(tr + "Last" + td +"First" + td + "Type" + td + "Num Nights" + td + "Subtotal" + td + "Sales Tax" + td + "Occ. Tax" + td + "Total")

    for i in range(len(guest)):
            data1 = tr + guest[i][0] + td + guest[i][1] + td + guest[i][2] + td + str(guest[i][3])
            data2 = td + format(guest[i][4],currency) + td + format(guest[i][5],currency) + td +format(guest[i][6],currency) + td + format(guest[i][7],currency)
            f.write(data1 + data2)
    f.write(td7 + "Grand Total" + td + format(grandtotal, currency) + endtr)
    f.write(td7 + "Date/Time" + td + day_time + endtr)
    f.write('</table><br />')
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
