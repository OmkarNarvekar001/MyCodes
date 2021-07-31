file = open("notes.txt", "rt")
data = file.read()


def word_frequency():
    words = data.split()
    user = input("Enter a string to find the frequency: ")
    print("The frequency of {} is {}".format(user, words.count(user)))


def display_words():
    word = data.split()
    for w in word:
        if len(w) < 4:
            print(w, end=" ")
    print("")


def count_words():
    words = data.split()
    print("Number of words in text file :", len(words))


def convert_upper():
    new = data.upper()
    print(new)


choice = 0
while choice != 5:
    print("-------------------------------------------------")
    print("\nSelect one option : ")
    print(" 1. Find the frequency of a given word\n 2. Display the words having length less than 4 letters\n 3. Count the total number of words in the text file\n 4. Convert the text to upper case and print\n 5. Exit")

    print("\n-------------------------------------------------")

    choice = int(input("Your Choice: "))
    if choice == 1:
        word_frequency()
    elif choice == 2:
        display_words()
    elif choice == 3:
        count_words()
    elif choice == 4:
        convert_upper()
    elif choice == 5:
        exit()
    else:
        pass