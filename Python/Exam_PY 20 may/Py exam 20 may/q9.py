import sqlite3

print("Database connection successful")

stationarycount = 1


def insertIntoDB(id, name, category, price):
    conn = sqlite3.connect("test.db")
    conn.execute(
        f"Insert into stationary (id, name, category, price) values({id}, '{name}', '{category}', {price})",
    )
    conn.commit()
    print("Row Inserted successfully")
    conn.close()


def add_new_stationary():
    global stationarycount
    name = input("Enter company name: ")
    category = input("Enter category name: ")
    price = int(input("Enter price: "))
    id = stationarycount
    insertIntoDB(id, name, category, price)
    stationarycount += 1



def print_stationary():
    conn = sqlite3.connect("test.db")
    cur = conn.execute("Select * from stationary")
    for row in cur:
        print(f"Stationary id number: {row[0]}")
        print(f"Stationary Company name: {row[1]}")
        print(f"Stationary Category: {row[2]}")
        print(f"Stationary price: {row[3]}")
        print("")


choice = 0
# loadData()
while choice != 3:
    print()
    print("1. Add stationary")
    print("2. Print all stationaries")
    print("3. to exit")
    choice = int(input("Enter your choice: "))
    print("-----------------------------------------")

    if choice == 1:
        add_new_stationary()
    elif choice == 2:
        print_stationary()
    elif choice == 3:
        print("Thank you")
    else:
        print("Invalid number try again")