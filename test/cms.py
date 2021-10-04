import csv
import os


test_mode = True

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
else:
    print("Please enter the VIN")
    vin = input(); #enter vin number here

path = vin+"/"

if not os.path.exists(path):
    os.makedirs(path)
    print("VIN not found in system, please input details about the vehicle")
    print("Please enter the Manufacturer of the Vehicle")
    if test_mode == True:
        make
    else:
        make = input()
    print("Please enter the Model")
    if test_mode == True:
        model
    else:
        model = input()

    print("Please enter the Year of Manufacture")
    if test_mode == True:
        year
    else:
        year = input()

    print("Please enter the Trim level")
    if test_mode == True:
        m_trim
    else:
        m_trim = input()

    print("Please enter the paint code")
    if test_mode == True:
        colour
    else:
        colour = input()

    print("Please enter the Engine specifications")
    if test_mode == True:
        engine
    else:
        engine = input()

    print("Please enter the Transmission type of the Vehicle")
    if test_mode == True:
        transmission
    else:
        transmission = input()

    print("Please enter the Chassis designation of the Vehicle")
    if test_mode == True:
        chassis
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
        print(n)
    headder = ["TIMESTAMP,","TIME_WORK_DONE,","TYPE_OF_WORK_DONE,","WORK_DONE_DESC,", "LOCATION_INFO","\n"]
    f.writelines(headder)

else:
    print("VIN Found, Please wait while maintainance records are being accessed")
    f = open((path+vin+".csv"), 'a')


f.close()





#print(head_info)
#f = open((path+vin+".csv"), 'a')
