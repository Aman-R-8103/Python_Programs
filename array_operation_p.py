MAX = 100

def create_array():
    size = int(input("Enter the number of elements: "))
    if size > MAX:
        print("Size exceeds array limit.")
        return [], 0
    elif size == 0:
        print("NO MEMORY ALLOCATION")
        return [], 0

    arr = []
    print("Enter elements:")
    for _ in range(size):
        element = int(input())
        arr.append(element)

    return arr, size

def display_array(arr, size):
    print("Array contains:", *arr[:size])

def insert_element(arr, size):
    element = int(input("Enter the element to insert: "))
    position = int(input("Enter the position to insert: "))
    
    if position < 0 or position > size:
        print("Invalid position.")
        return size

    arr.insert(position, element)
    size += 1
    return size

def delete_element(arr, size):
    position = int(input("Enter the position to delete: "))

    if position < 0 or position >= size:
        print("Invalid position.")
        return size

    arr.pop(position)
    size -= 1
    return size

def main():
    arr = []
    size = 0
    choice = 0

    print("NAMASKARAM! This program allows insertion and deletion in a dynamic array.")

    while choice != 5:
        print("\n\n\t\t**********MAIN MENU**********")
        print("1. Create an Array")
        print("2. Display the Array")
        print("3. Insert an Element")
        print("4. Delete an Element")
        print("5. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            arr, size = create_array()
        elif choice == 2:
            display_array(arr, size)
        elif choice == 3:
            size = insert_element(arr, size)
        elif choice == 4:
            size = delete_element(arr, size)
        elif choice == 5:
            print("\nGOODBYE")
        else:
            print("\nINVALID CHOICE")

if __name__ == "__main__":
    main()
