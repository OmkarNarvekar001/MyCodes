import mynumbers

def main():
    while True:
        print("\n")
        print("Menu")
        print("1. Add number")
        print("2. Largest value")
        print("3. Lowest value")
        print("4. Sort")
        print("5. Multiples of the list ")
        print("6. Look")
        print("7. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            mynumbers.PyNumber.add()

        elif ch == 2:
            mynumbers.PyNumber.high()

        elif ch == 3:
            mynumbers.PyNumber.low()

        elif ch == 4:
            mynumbers.PyNumber.sort()

        elif ch == 5:
            mynumbers.PyNumber.multiples()

        elif ch == 6:
            mynumbers.PyNumber.look()


        elif ch == 7:
            print("Thankyou!")
            break

if __name__ == "__main__":
    main()
