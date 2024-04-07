class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def display_list(start):
    if start is None:
        print("List is empty.")
        return
    current = start
    print("Circular Doubly Linked List: ", end='')
    while True:
        print(current.data, '-> ', end='')
        current = current.next
        if current == start:
            break
    print('(head)')

def insert_at_beginning(start, data):
    newNode = Node(data)
    if start is None:
        start = newNode
        start.next = start
        start.prev = start
    else:
        newNode.next = start
        newNode.prev = start.prev
        start.prev.next = newNode
        start.prev = newNode
        start = newNode
    return start

def insert_at_end(start, data):
    if start is None:
        return insert_at_beginning(start, data)
    newNode = Node(data)
    newNode.next = start
    newNode.prev = start.prev
    start.prev.next = newNode
    start.prev = newNode
    return start

def insert_after_value(start, value, data):
    if start is None:
        print("List is empty.")
        return start
    current = start
    while True:
        if current.data == value:
            newNode = Node(data)
            newNode.next = current.next
            newNode.prev = current
            current.next.prev = newNode
            current.next = newNode
            break
        current = current.next
        if current == start:
            print("Value not found in the list.")
            break
    return start

def insert_before_value(start, value, data):
    if start is None:
        print("List is empty.")
        return start
    current = start
    while True:
        if current.data == value:
            newNode = Node(data)
            newNode.next = current
            newNode.prev = current.prev
            current.prev.next = newNode
            current.prev = newNode
            if current == start:
                start = newNode
            break
        current = current.next
        if current == start:
            print("Value not found in the list.")
            break
    return start

def delete_at_beginning(start):
    if start is None:
        print("List is empty. Nothing to delete.")
        return start
    if start.next == start:
        start = None
    else:
        start.next.prev = start.prev
        start.prev.next = start.next
        start = start.next
    return start

def delete_at_end(start):
    if start is None:
        print("List is empty. Nothing to delete.")
        return start
    if start.next == start:
        start = None
    else:
        start.prev.prev.next = start
        start.prev = start.prev.prev
    return start

def delete_value(start, value):
    if start is None:
        print("List is empty. Nothing to delete.")
        return start
    current = start
    while True:
        if current.data == value:
            if current == start:
                start = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            break
        current = current.next
        if current == start:
            print("Value not found in the list.")
            break
    return start

# Main program
start = None

print("NAMASKARAM! This program demonstrates insertion and deletion in a circular doubly linked list.\n")

while True:
    print("\n\n\t\t**********MAIN MENU**********")
    print(" 1:) Create a Circular Doubly Linked List")
    print(" 2:) Display the Circular Doubly Linked List")
    print(" 3:) Insert a node in the CDLL")
    print(" 4:) Delete a node in the CDLL")
    print(" 5:) Exit the program")

    option = int(input("\nEnter your choice : "))

    if option == 1:
        nums = []
        print("Enter numbers to create a Circular Doubly Linked List (enter -1 to end):")
        while True:
            num = int(input())
            if num == -1:
                break
            nums.append(num)
        for num in nums:
            start = insert_at_end(start, num)

    elif option == 2:
        display_list(start)

    elif option == 3:
        print("Choose method of insertion:")
        print(" 1:) Insert at the beginning")
        print(" 2:) Insert at the end")
        print(" 3:) Insert after a specific value")
        print(" 4:) Insert before a specific value")
        choice = int(input("\nEnter your choice: "))
        data = int(input("Enter the data to be inserted: "))
        if choice == 1:
            start = insert_at_beginning(start, data)
        elif choice == 2:
            start = insert_at_end(start, data)
        elif choice == 3:
            value = int(input("Enter the value after which you want to insert: "))
            start = insert_after_value(start, value, data)
        elif choice == 4:
            value = int(input("Enter the value before which you want to insert: "))
            start = insert_before_value(start, value, data)
        else:
            print("Invalid choice.")

    elif option == 4:
        print("Choose method of deletion:")
        print(" 1:) Delete at the beginning")
        print(" 2:) Delete at the end")
        print(" 3:) Delete a specific value")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            start = delete_at_beginning(start)
        elif choice == 2:
            start = delete_at_end(start)
        elif choice == 3:
            value = int(input("Enter the value to be deleted: "))
            start = delete_value(start, value)
        else:
            print("Invalid choice.")

    elif option == 5:
        print("\nExiting...")
        break

    else:
        print("\nInvalid option. Please try again.")
