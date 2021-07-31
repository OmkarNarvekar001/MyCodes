import pickle
class Inventory:
    def __init__(self, id, name, manufacturer, price):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        
def add_new_product():
    name = input("Enter name: ")
    manufacturer = input("Enter manufacturer name: ")
    with open('bank.dat','rb') as bank:
        products = list(pickle.load(bank))
    price = int(input("Enter price: "))
    id = len(products) + 1
    products.append(Inventory(id, name, manufacturer, price))
    with open('bank.dat','wb')as bank:
        pickle.dump(products,bank)
        bank.close()



def update_price():
    display_product()
    list1 = []
    name = input("Enter name to update: ")
    with open('bank.dat','rb') as bank:
        list1=pickle.load(bank)
        bank.close()
    for index, product in enumerate(list1):
        if product.name == name:
            name_new = input("Enter updated name: ")
            price_new = int(input("Enter updated price: "))
            list1[index] = Inventory(product.id, name_new, product.manufacturer, price_new)
            print(f"{product.name} is updated")
            break
    with open('bank.dat','wb')as bank:
        pickle.dump(list1,bank)
        bank.close()


def delete_product():
    display_product()
    name = input("Enter product name to delete: ")
    p = []
    with open('bank.dat','rb') as bank:
        p = list(pickle.load(bank))
    for product in p:
        if product.name == name:
            p.remove(product)
            print(f"{product.name} was removed")
    with open('bank.dat','wb')as bank:
        pickle.dump(p,bank)
        bank.close()


def display_product():
    p = []

    with open('bank.dat','rb') as bank:
        p = list(pickle.load(bank))
    for counter, product in enumerate(p):
        print(f"{counter+1}. {product.name} by {product.manufacturer} at {product.price}")
    
with open('bank.dat','wb') as bank:
    pickle.dump([],bank)
choice = 0
while choice != 5:
    print()
    print("1. Add new product")
    print("2. delete product")
    print("3. display all products")
    print("4. Update price")
    print("5. to exit")
    choice = int(input("Enter you choice: "))
    print("-----------------------------------------")
    if choice == 1:
        add_new_product()
    elif choice == 2:
        delete_product()
    elif choice == 3:
        display_product()
    elif choice == 4:
        update_price()
    elif choice == 5:
        print("Thank you")
    else:
        print("Invalid number try again")