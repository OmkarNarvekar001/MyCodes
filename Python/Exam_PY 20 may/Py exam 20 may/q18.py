import math
def main():
    while True:
        print("1.TypeError")
        print("2.ValueError")
        print("3.ImportError")
        print("4.ZeroDivisionError")
        print("5.NameError")
        print("6.Exit")

        ch = int(input("Enter Choice"))

        if ch==1:
            try:
                x = int(input("Please enter a number: "))
                print("Successful!!!")

            except ValueError:
                print("Oops! That was not a valid number. Try again...")
            try:
                x = int(input("Please enter another number: "))
                print("no err")
            except TypeError:
                print("Oops! TypeError")

        elif ch==2:
            x = int(input('Please enter a positive number:\n'))

            try:
                print(f'Square Root of {x} is {math.sqrt(x)}')
            except ValueError as ve:
                print(f'You entered {x}, which is not a positive number.')

        elif ch==3:
            print("Program to demonstrate to handle ImportError:")
            print("\n")
            try:
                from crypt import pwd
            except ImportError as ie:
                print("It cannot import module and submodule", ie)

        elif ch==4:
            try:
                a = int(input("Enter a:"))
                b = int(input("Enter b:"))
                c = a / b
            except:
                print("Can't divide with zero")

        elif ch==5:

            def geek_message():
                try:
                    geek = "GeeksforGeeks"
                    return geek
                except NameError:
                    return "NameError occured. Some variable isn't defined."
            print(geek_message())


        elif ch==6:
            break

if __name__=="__main__":
    main()