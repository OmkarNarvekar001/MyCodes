
import sqlite3

try:
    print("Hii,this is a Stationery management command line app.")
    con = sqlite3.connect("Stationery.db")
    con.execute(
        "create table product(product_id primary key, name text not null, price int not null,category not null)")
    con.commit()
except sqlite3.OperationalError:
    pass

product_list = []


def add_product():
    con = sqlite3.connect("Stationery.db")
    print("Enter the details of the Product.")
    roll = input("Enter Product_Id: ")
    name = input("Enter Products Name: ")
    price = input("Enter Products Price: ")
    category =input("Enter Category: ")
    try:
        con.execute("INSERT INTO product Values (?,?,?,?)", (roll, name, price,category))
        con.commit()
    except Exception as e:
        print("Enter proper values", e)
    product_list.append([roll, name, price ,category])
    print("New Product added Successfully")
    print("*******************************************")


def read_all():
    con = sqlite3.connect("Stationery.db")
    r_set = con.execute(""" Select * from product""")
    i = 0
    print("Product_Id Product_Name Price Category")
    for b in r_set:
        for j in range(len(b)):
            print(b[j], end=" ")
        i = i + 1
        print(" ")
    print("*******************************************")


if __name__ == "__main__":
    choice = 0
    con = sqlite3.connect("Stationery.db")
    while choice != 3:
        print()
        print("1. Add Products.")

        print("2. See all Products data.")
        print("3. Exit.")
        choice = int(input("Enter you choice: "))
        print("-----------------------------------------")

        if choice == 1:
            add_product()

        elif choice == 2:
            read_all()

        elif choice == 3:
            print("Thank you")
        else:
            print("Invalid number try again")
    con.commit()
    con.close()


