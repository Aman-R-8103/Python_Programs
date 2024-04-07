def create_dynamic_array():
    new_size = int(input("Enter size of array: "))
    array = [0] * new_size

    print(f"Enter {new_size} elements for the array:")
    for i in range(new_size):
        array[i] = int(input())

    return array, new_size


def display_dynamic_array(array, size):
    print("The elements of the array are:", *array[:size])


def insert_element(array, size):
    element = int(input("Enter the element to insert: "))
    position = int(input("Enter the index number on which to insert: "))

    if position < 0 or position > size:
        print("\nInvalid position. Array insertion aborted.\n")
    else:
        array.insert(position, element)
        size += 1

    return size


def delete_element(array, size):
    position = int(input("Enter the index number of the element to delete: "))

    if position < 0 or position >= size:
        print("\nInvalid position. Array deletion aborted.\n")
    else:
        del array[position]
        size -= 1

    return size


def main():
    array = []
    size = 0
    option = 0

    print("NAMASKARAM! This program allows insertion and deletion in a dynamic array.\n")

    while option != 5:
        print("\n\n\t\t**********MAIN MENU**********")
        print("1:) Create a Dynamic Array")
        print("2:) Display the Dynamic Array")
        print("3:) Insert an element")
        print("4:) Delete an element")
        print("5:) Exit the program")
        option = int(input("\nEnter your choice: "))

        if option == 1:
            array, size = create_dynamic_array()
        elif option == 2:
            display_dynamic_array(array, size)
        elif option == 3:
            size = insert_element(array, size)
        elif option == 4:
            size = delete_element(array, size)
        elif option == 5:
            print("\nExiting...\n")
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
