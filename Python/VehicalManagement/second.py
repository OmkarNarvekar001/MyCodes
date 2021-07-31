from first import manage

veh = []
class Vehicle:

    def addVehicle(self):
        i = 1
        try:
            print()
            v = manage(input("Enter the owners name:"), input("Enter the Vehicle name:"), input("Enter the Vehicle number:"),
                       int(input("Enter the owners contact no:")), input("Enter the type of Vehicle i.e. Petrol/Diesel:"))
            veh.append(v)
            print()
            # for x in veh:
            #     print([x.oname, x.vname, x.vno, x.phno, x.type])
        except:
            print("All fields are mandatory")
            print()

    def disp(self):
        # try:
        vn = input("Enter the Vehicle number who's details are to be displayed:")
        for x in veh:
            if x.vno == vn:
                print()
                print("-----------Details Found-----------")
                print(f"Vehicle Owner name ={x.oname.upper()}")
                print(f"Vehicle name ={x.vname.upper()}")
                print(f"Vehicle number ={x.vno.upper()}")
                print(f"Owners contact={x.phno}")
                print(f"Vehicle type={x.type.upper()}")
                print("------------------------------------")
                print()
                s = vn
        if s == None:
            # else:
            print(f"-----------'{s.upper()}' vehicle number does not exist-----------")
            print()

        # except:
        #     print("Enter the correct vehicle number !!")
        #     print()

