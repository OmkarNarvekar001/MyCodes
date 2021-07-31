list1 = []

class Vehicle:
    def __init__(self, veh_no, name, company, price):
        self.veh_no = veh_no
        self.name = name
        self.company = company
        self.price = price

def add_car_bike():
    name = input("Enter Vehicle name: ")
    veh_no = int(input("Enter Vehicle no: "))
    company = input("Enter company of car: ")
    price = int(input("Enter price: "))
    list1.append(Vehicle(veh_no, name, company, price))


def display():
    ac = int(input("Enter the Vehicle no to be displayed: "))
    for x in list1:
        if x.veh_no == ac:
            print(f" Vehicle Name: {x.name}\n")
            print(f" Vehicle No: {x.veh_no}\n")
            print(f" Company: {x.company}\n")
            print(f" Price: {x.price}\n")


def update():
    ac = int(input("Enter the Vehicle no of which price to be update: "))
    for x in list1:
        if x.veh_no == ac:
            # self.price = pr
            pr = int(input("Enter Updated Price: "))
            x.price = pr
            print("Updated price is : ", pr)
        else:
            print("No data found")


def delete():
    ac = int(input("Enter the vehicle no: "))
    for x in list1:
        if x.veh_no == ac:
            list1.remove(x)
        print("Deleted")


class Car(Vehicle):
    def init(self, veh_no, name, company, price):
        Vehicle.init(self, veh_no, name, company, price)

    def car(self):
        for i in list1:
            if i.type == "car":
                print("-----------------------------------------------------")
                print(f" Price IS:{i.price}\n")
                print(f" NAME IS: {i.name}\n")
                print(f" Company {i.company}\n")
                print("-----------------------------------------------------")

            else:
                print("-----------------------------------------------------")
                print("No Data Found")
                print("-----------------------------------------------------")


class Bike(Vehicle):
    def init(self, veh_no, name, company, price):
        Vehicle.init(self, veh_no, name, company, price)

    def bike(self):
        for i in list1:
            if i.type == "Bike":
                print("-----------------------------------------------------")
                print(f" Price IS:{i.price}\n")
                print(f" NAME IS: {i.name}\n")
                print(f" Company {i.company}\n")
                print("-----------------------------------------------------")

            else:
                print("-----------------------------------------------------")
                print("No Data Found")
                print("-----------------------------------------------------")


def main():
    while True:
        print("1. Add new Vehicle")
        print("2. Update price")
        print("3. To display mentioned vehicle details")
        print("4. Delete vehicle")
        print("5. Quit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            add_car_bike()

        elif ch == 2:
            update()
        elif ch == 3:
            display()
        elif ch == 4:
            delete()
        elif ch == 5:
            print(" Bye! Have a good day!")
            break


if __name__ == "__main__":
    main()