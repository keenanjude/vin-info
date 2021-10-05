#important
##The first 9 lines of the CSV file contain information about the vehicle.
##The 10th line contains the table headder, and data about service begins on line 11. 

import csv
import os
from datetime import datetime


test_mode = True #MUST BE TRUE OR FALSE

if test_mode == True:
    vin = "123EK456"
    make = "HONDA MFG. Co."
    model = "CIVIC"
    year = "1999"
    m_trim = "DX"
    colour = "NH0"
    engine = "1.6L B16B"
    transmission = "5-Speed Manual"
    chassis = "EK"


if test_mode == True:
    vin
    print("TEST MODE")
else:
    print("Please enter the VIN")
    vin = input(); #enter vin number here

path = vin+"/"

if not os.path.exists(path):
    print("The entered VIN could not be found in the system, would you like to create a new entry?")
    os.makedirs(path)
    print("VIN not found in system, please input details about the vehicle")
    print("Please enter the Manufacturer of the Vehicle")
    if test_mode == True:
        make
        print("TEST MODE")
    else:
        make = input()
    print("Please enter the Model")
    if test_mode == True:
        model
        print("TEST MODE")
    else:
        model = input()

    print("Please enter the Year of Manufacture")
    if test_mode == True:
        year
        print("TEST MODE")
    else:
        year = input()

    print("Please enter the Trim level")
    if test_mode == True:
        m_trim
        print("TEST MODE")
    else:
        m_trim = input()

    print("Please enter the paint code")
    if test_mode == True:
        colour
        print("TEST MODE")
    else:
        colour = input()

    print("Please enter the Engine specifications")
    if test_mode == True:
        engine
        print("TEST MODE")
    else:
        engine = input()

    print("Please enter the Transmission type of the Vehicle")
    if test_mode == True:
        transmission
        print("TEST MODE")
    else:
        transmission = input()

    print("Please enter the Chassis designation of the Vehicle")
    if test_mode == True:
        chassis
        print("TEST MODE")
    else:
        chassis = input() #chassis code
    #head_info = {"VIN":vin, "Manufacturer":model, "Model": model, "Year": year, "Trim": m_trim, "Colour Code": colour, "Engine": engine, "Transmission": transmission, "Chassis Code": chassis}
    head_info = [vin, make, model, year, m_trim, colour, engine, transmission, chassis]
    head_info2 = ["VIN", "Manufacturer", "Model", "Year", "Trim", "Colour Code", "Engine", "Transmission", "Chassis"]
    f = open((path+vin+".csv"), 'w')
    n = 0
    for i in head_info2:
        f.write(i + "," + head_info[n] + "\n")
        n += 1
        #print(n)
    headder = ["TIMESTAMP,","TIME_WORK_DONE,","MILEAGE_AT_INTERVAL_KM,","TYPE_OF_WORK_DONE,","WORK_DONE_DESC,", "LOCATION_INFO","\n"]
    f.writelines(headder)
    print("A new vehicle has been added! Please restart the program")

else:
    print("VIN Found, Please wait while maintainance records are being accessed \n")
    f = open((path+vin+".csv"))
    readF = csv.reader(f)
    n = 0
    for line in f.readlines():
        if n < 9:
            print(line.rstrip())
            n += 1
        else:
            print("\nYour last service record as listed")
            pass
            last_line = line
            print(last_line)
            break

    f = open((path+vin+".csv"), 'a')
    
    print("would you like to update your service record? (Y/N)\n")
    choice = input().upper()
    if choice == "Y":
        nowtime = datetime.now()
        TIMESTAMP = nowtime.strftime("%m/%d/%Y")
        TIME_WORK_DONE = input('input the date work was done\n').upper()
        MILEAGE_AT_INTERVAL_KM = input('Enter the odometer readout in Kilometers\n').upper()
        TYPE_OF_WORK_DONE = input('Enter the general code for work done\n').upper()
        WORK_DONE_DESC = input('Enter the description for work done on vehicle\n').upper()
        LOCATION_INFO = input('Enter any location info of where the work was completed\n').upper()
        service = [TIMESTAMP,",",TIME_WORK_DONE,",",MILEAGE_AT_INTERVAL_KM,",",TYPE_OF_WORK_DONE,",",WORK_DONE_DESC,",",LOCATION_INFO]
        f.writelines(service)

    else:
        f.close()





f.close()





#print(head_info)
#f = open((path+vin+".csv"), 'a')
