# Create a vehicle management system that will have three modules
# 1. first.py - have getters and setters
# 2. second.py - have all the necessary methods
# 3. third.py - have the menu
import second


def main():
    while True:
        print("------------------------------")
        print("1. Add vehicle details")
        print("2. Print vehicle details")
        print("------------------------------")
        try:
            print()
            ch = int(input("Enter your choice:"))
            print()

            if ch == 1:
                second.Vehicle().addVehicle()

            elif ch == 2:
                second.Vehicle().disp()

        except:
            print("Enter choice between 1 to 7")
            print()


if __name__ == "__main__":
    main()
