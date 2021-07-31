list1 = []
list2 = []

class PyNumber:
    def __init__(self, numbers):
        self.number = numbers

    def add():
        num = int(input("Enter the number to be added: "))
        list1.append(num)
        print(f"{num} added successfully to the list.")

    def high():
        print("The largest value in the list is ", max(list1))

    def low():
        print("The smallest value in the list is ", min(list1))

    def sort():
        seq = int(input("Enter 0 for ascending and 1 for descending: "))
        if seq == 0:
            list1.sort()
            print("The list arranged in ascending order: ", list1)
        elif seq == 1:
            list1.sort(reverse = True)
            print("The list arranged in descending order: ", list1)
        else:
            print("Invalid input")

    def multiples():
        n = int(input("Enter number with which you want to multiply: "))
        list2 = [i * n for i in list1]
        print("Updated list: ", list2)

    def look():
        num = int(input("Enter the number to be searched: "))
        if num not in list1:
            print(f"{num} not found in list")
        else:
            index = list1.index(num)
            print(f"The number {num} is found at index {index}")


