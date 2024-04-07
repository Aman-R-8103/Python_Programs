def main():
    array = []  # Dynamic array
    size = 0  # Current size of the array
    option = 0  # User's choice

    print("NAMASKARAM! This program allows insertion and deletion in a dynamic array.\n")

    while option != 5:
        print("\n\n\t\t**********MAIN MENU**********")
        print("1. Create a Dynamic Array")
        print("2. Display the Dynamic Array")
        print("3. Insert an element")
        print("4. Delete an element")
        print("5. Exit the program")
        option = int(input("\nEnter your choice: "))

        if option == 1:
            size = int(input("Enter size of array: "))
            array = [int(input(f"Enter element {i + 1}: ")) for i in range(size)]
        elif option == 2:
            print("The elements of the array are:", *array[:size])
        elif option == 3:
            element = int(input("Enter the element to insert: "))
            position = int(input("Enter the index number on which to insert: "))
            if position < 0 or position > size:
                print("\nInvalid position. Array insertion aborted.\n")
            else:
                array.insert(position, element)
                size += 1
        elif option == 4:
            position = int(input("Enter the index number of the element to delete: "))
            if position < 0 or position >= size:
                print("\nInvalid position. Array deletion aborted.\n")
            else:
                array.pop(position)
                size -= 1
        elif option == 5:
            print("\nExiting...\n")
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
