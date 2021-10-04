import csv
import os

print("Please enter the VIN")
vin = input(); #enter vin number here

path = vin+"/"

if not os.path.exists(path):
    os.makedirs(path)
    print("Please enter the Manufacturer of the Vehicle")
    make = input()
    print("Please enter the Model")
    model = input()
    print("Please enter the Year of Manufacture")
    year = input()
    print("Please enter the Trim level")
    m_trim = input()
    print("Please enter the paint code")
    colour = input()
    print("Please enter the Engine specifications")
    engine = input()
    print("Please enter the Transmission type of the Vehicle")
    transmission = input()
    print("Please enter the Chassis designation of the Vehicle")
    chassis = "EJ" #chassis code
    #head_info = {"VIN":vin, "Manufacturer":model, "Model": model, "Year": year, "Trim": m_trim, "Colour Code": colour, "Engine": engine, "Transmission": transmission, "Chassis Code": chassis}
    head_info = [vin, make, model, year, m_trim, colour, engine, transmission, chassis]
    head_info2 = ["VIN", "Manufacturer", "Model", "Year", "Trim", "Colour Code", "Engine", "Transmission", "Chassis"]
    f = open((path+vin+".csv"), 'w')
    n = 0
    for i in head_info2:
        f.write(i + "," + head_info[n] + "\n")
        n += 1
        print(n)

else:
    f = open((path+vin+".csv"), 'a')







#print(head_info)
#f = open((path+vin+".csv"), 'a')
