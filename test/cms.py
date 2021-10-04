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
else:
    vin = input()
    make = input()
    model = input()
    year = raw_input()
    m_trim = input()
    colour = input()
    engine = input()
    transmission = input()
    chassis = input()

print("Please enter the VIN")
vin; #enter vin number here

path = vin+"/"

if not os.path.exists(path):
    os.makedirs(path)
    print("Please enter the Manufacturer of the Vehicle")
    make
    print("Please enter the Model")
    model
    print("Please enter the Year of Manufacture")
    year
    print("Please enter the Trim level")
    m_trim
    print("Please enter the paint code")
    colour
    print("Please enter the Engine specifications")
    engine
    print("Please enter the Transmission type of the Vehicle")
    transmission
    print("Please enter the Chassis designation of the Vehicle")
    chassis #chassis code
    #head_info = {"VIN":vin, "Manufacturer":model, "Model": model, "Year": year, "Trim": m_trim, "Colour Code": colour, "Engine": engine, "Transmission": transmission, "Chassis Code": chassis}
    head_info = [vin, make, model, year, m_trim, colour, engine, transmission, chassis]
    head_info2 = ["VIN", "Manufacturer", "Model", "Year", "Trim", "Colour Code", "Engine", "Transmission", "Chassis"]
    f = open((path+vin+".csv"), 'w')
    n = 0
    for i in head_info2:
        f.write(i + "," + head_info[n] + "\n")
        n += 1
        print(n)
    headder = ["TIMESTAMP","TIME_WORK_DONE","TYPE_OF_WORK_DONE","WORK DONE DESC", "LOCATION INFO"]
    f.writelines(headder)

else:
    f = open((path+vin+".csv"), 'a')







#print(head_info)
#f = open((path+vin+".csv"), 'a')
