
import sqlite3

try:
    print("Hii,this is a Library management command line app.")
    con = sqlite3.connect("library.db")
    con.execute(
        "create table Book(book_id primary key, name text not null, price int not null,author not null)")
    con.commit()
except sqlite3.OperationalError:
    pass

product_list = []


def add_book():
    con = sqlite3.connect("library.db")
    print("Enter the details of the Book.")
    roll = input("Enter Book_Id: ")
    name = input("Enter Book Name: ")
    price = input("Enter Book Price: ")
    author =input("Enter Book's Author: ")
    try:
        con.execute("INSERT INTO Book Values (?,?,?,?)", (roll, name, price,author))
        con.commit()
    except Exception as e:
        print("Enter proper values", e)
    product_list.append([roll, name, price ,author])
    print("New Book added Successfully")
    print("*******************************************")


def read_all():
    con = sqlite3.connect("library.db")
    r_set = con.execute(""" Select * from Book""")
    i = 0
    print("Book_Id Book_Name Price Author")
    for b in r_set:
        for j in range(len(b)):
            print(b[j], end=" ")
        i = i + 1
        print(" ")
    print("*******************************************")


if __name__ == "__main__":
    choice = 0
    con = sqlite3.connect("library.db")
    while choice != 3:
        print()
        print("1. Add Books.")

        print("2. See all Books data.")
        print("3. Exit.")
        choice = int(input("Enter you choice: "))
        print("-----------------------------------------")

        if choice == 1:
            add_book()

        elif choice == 2:
            read_all()

        elif choice == 3:
            print("Thank you")
        else:
            print("Invalid number try again")
    con.commit()
    con.close()


