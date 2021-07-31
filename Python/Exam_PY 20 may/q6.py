books = {}

class Book:
    def __init__(self, id, name, author, price, quantitiy):
        self.id = id
        self.name = name
        self.author = author
        self.price = price
        self.quantity = quantitiy

    def __ge__(self, mrp):
        if (self.price >= mrp.price):
            return "Book1's price is greater than equal to Book2's price"
        else:
            return "Book2's price is greater than  Book1's price"

    def update_book(self, name):

        for i in books:
            if books[i].name == name:
                name_new = input("Enter updated name for book: ")
                price_new = int(input("Enter updated price: "))
                books[i].name = name_new
                books[i].price = price_new
                print(f"{books[i].name} is updated")
                break
        return


def add_new_book():
    global books
    name = input("Enter book name: ")
    author = input("Enter author name: ")
    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    i = len(books) + 1
    books[i]=Book(i, name, author, price, quantity)


def delete_book():
    global books
    print_book()

    name1 = input("Enter title of book to delete: ")
    x=-1
    for i in books:
        if books[i].name == name1:
            x=i
    if x in books:    
        del books[x]
        print("book deleted")
    else:
        print("invalid")


def print_book():
    # print(books)
    for i in books:
        print("Name: "+books[i].name)
        print("Author: "+books[i].author)
        print("Price: "+str(books[i].price))
        print("Quantity: "+str(books[i].quantity))
        print()

def costlier():
    print_book()

    name1 = input("Enter title of first book : ")
    name2 = input("Enter title of second book : ")
    ob1, ob2 = "", ""

    for i in (books):
        if books[i].name == name1:
            ob1 = Book(books[i].id, books[i].name,
                       books[i].author, books[i].price, books[i].quantity)
        if books[i].name == name2:
            ob2 = Book(books[i].id, books[i].name,
                       books[i].author, books[i].price, books[i].quantity)

            break
    print(ob1 >= ob2)


choice = 0
while choice != 10:
    print()
    print("1. Add a new book")
    print("2. Update cost of a book")
    print("3. Delete a book")
    print("4. Display details of all books")
    print("5. Compare books using operator overlaoding")
    print("6. To exit")
    choice = int(input("Enter you choice: "))
    print("-----------------------------------------")

    if choice == 1:
        add_new_book()

    elif choice == 2:

        name = input("Enter title of book to update: ")
        for i in books:
            if books[i].name == name:
                ob1 = Book(books[i].id, books[i].name,
                       books[i].author, books[i].price, books[i].quantity)

        ob1.update_book(name)

    elif choice == 3:
        delete_book()

    elif choice == 4:
        print_book()

    elif choice == 5:
        costlier()

    elif choice == 6:
        print("Thank you")
        break
    else:
        print("Invalid number try again")