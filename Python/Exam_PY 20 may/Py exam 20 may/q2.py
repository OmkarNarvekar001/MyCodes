
class Queue:

    def __init__(self):
        self.lst = []

    def push(self, x, count):
        self.lst.append(x)
        count += 1
        print(f"\n{x} PUSHED\n")
        return count

    def pop(self, count):
        if(count == 0):
            print("\nLIST IS EMPTY\n")
            return count
        
        x = self.lst[0]
        self.lst.pop(0)
        count -= 1
        print(f"\n{x} POPPED\n")
        return count

    def count(self, count):
        print(f"\nTHERE ARE {count} NUMBERS PRESENT IN LIST\n")
        return

    def display(self, pos, count):
        if(count == 0):
            print("\nLIST IS EMPTY\n")
            return
        
        try: 
            if(pos == -1):
                print("\nQUEUE:\n")
                for i in range(count):
                    print(f"\t{self.lst[i]}")
                print("\n")
                return
            
            else:
                print(f"\nELEMENT AT POSITION {pos} IS {self.lst[pos]}\n")
                return

        except IndexError:
            print(f"\nENTER VALID INDEX.\nONLY {count} ELEMENTS ARE PRESENT IN LIST\n")
            return
        



def main():
    choice = 0
    queue1 = Queue()
    count = 0
    
    print("\nWELCOME")

    while(choice != 5):
        
        print("\nMENU:")
        print("1. PUSH\n2. POP\n3. COUNT\n4. DISPLAY\n5. EXIT")
        choice = int(input("\nSELECT AN OPTION: "))

        if(choice == 1):
            x = int(input("\nENTER THE NUMBER YOU WANT TO PUSH: "))
            count = queue1.push(x, count)
        
        elif(choice == 2):
            count = queue1.pop(count)
        
        elif(choice == 3):
            queue1.count(count)
        
        elif(choice == 4):
            x = int(input("\nENTER THE INDEX: "))
            queue1.display(x, count)
        
        elif(choice == 5):
            print("\nTHANK YOU\n")
            break

        else:
            print("\nINVALID INPUT\n")


if __name__ == '__main__':
    main()