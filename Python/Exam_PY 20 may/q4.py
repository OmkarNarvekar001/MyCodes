class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
        print(self.items)

    def push(self, item):
        self.items.append(item)
        print(self.items)

    def pop(self):
        self.items.pop()
        print(self.items)

    def display(self, item = -1):
        print(self.items)
        print(self.items[item])

    def size(self):
        print("The number of element is stack is :")
        print(len(self.items))
        print(self.items)

st = Stack()

while True:
    print("Stack operations: ")
    print("1]Push a number")
    print("2]Pop a number")
    print("3]Print the list.")
    print("4]Count number of elements.")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        x = int(input("\nPush number: "))
        st.push(x)
        # print the stack.
    elif choice == 2:
        y = print("\n Last element is pop from list")
        st.pop()
        # print the stack.
    elif choice == 3:
        # print the stack
        z = int(input("Enter the position of the element to display"))
        st.display(z)
    elif choice == 4:
        print("\nNumber of elements present are: ")
        # count of the stack.
        st.size()
        break
    else:
        print("\nWrong choice.")


