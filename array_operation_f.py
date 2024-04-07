def display_menu():
    print("\n\n\t\t**********MAIN MENU**********")
    print("1. Create an Array")
    print("2. Display the Array")
    print("3. Insert an Element")
    print("4. Delete an Element")
    print("5. Exit")
    return int(input("Enter your choice: "))


def enter_elements():
    global size
    size = int(input("Enter the number of elements: "))
    if size > max_size:
        print("Size exceeds array limit.")
    elif size == 0:
        print("NO MEMORY ALLOCATION")
    else:
        print("Enter elements: ")
        arr.extend(map(int, input().split()))


def display_array():
    print("Array contains:", *arr)


def insert_element():
    global size
    element = int(input("Enter the element to insert: "))
    position = int(input("Enter the position to insert: "))
    if position < 0 or position > size:
        print("Invalid position.")
    elif size >= max_size:
        print("Array is full.")
    else:
        arr.insert(position, element)
        size += 1
    display_array()


def delete_element():
    global size
    position = int(input("Enter the position to delete: "))
    if position < 0 or position >= size:
        print("Invalid position.")
    else:
        arr.pop(position)
        size -= 1
    display_array()


max_size = 100
size = 0
arr = []

while True:
    choice = display_menu()
    if choice > 5 or choice <= 0:
        print("INVALID CHOICE")
    elif choice == 1:
        enter_elements()
    elif choice == 2:
        display_array()
    elif choice == 3:
        insert_element()
    elif choice == 4:
        delete_element()
    elif choice == 5:
        print("Aapka Din Shub ho")
        break
