class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_cll():
    start = None
    while True:
        num = int(input("Enter a number to create a Circular Linked List (enter -1 to end): "))
        if num == -1:
            break
        new_node = Node(num)
        if start is None:
            start = new_node
            new_node.next = start  # Circular link
        else:
            ptr = start
            while ptr.next != start:
                ptr = ptr.next
            ptr.next = new_node
            new_node.next = start  # Circular link
    return start

def display_cll(start):
    if start is None:
        print("\nList is empty.")
        return
    ptr = start
    print("\nCircular Linked List:", end=" ")
    while True:
        print(ptr.data, "->", end=" ")
        ptr = ptr.next
        if ptr == start:
            break
    print("... (circular)")

def insert_node(start):
    if start is None:
        print("List is empty. Cannot insert.")
        return start

    new_data = int(input("\nEnter the data to be inserted: "))
    choice = int(input("Choose method of insertion:\n1. Insert at the beginning\n2. Insert at the end\n3. Insert after a specific value\n4. Insert before a specific value\n"))
    new_node = Node(new_data)

    if choice == 1:
        new_node.next = start
        ptr = start
        while ptr.next != start:
            ptr = ptr.next
        ptr.next = new_node
        start = new_node
    elif choice == 2:
        ptr = start
        while ptr.next != start:
            ptr = ptr.next
        ptr.next = new_node
        new_node.next = start
    elif choice == 3:
        val = int(input("Enter the value after which you want to insert: "))
        ptr = start
        while ptr.data != val:
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                return start
        new_node.next = ptr.next
        ptr.next = new_node
    elif choice == 4:
        val = int(input("Enter the value before which you want to insert: "))
        prev = None
        ptr = start
        while ptr.data != val:
            prev = ptr
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                return start
        if prev is None:
            new_node.next = start
            ptr = start
            while ptr.next != start:
                ptr = ptr.next
            ptr.next = new_node
            start = new_node
        else:
            new_node.next = ptr
            prev.next = new_node
    else:
        print("Invalid choice.")
    return start

def delete_node(start):
    if start is None:
        print("List is empty. Nothing to delete.")
        return start

    choice = int(input("\nChoose method of deletion:\n1. Delete at the beginning\n2. Delete at the end\n3. Delete a specific value\n"))
    if choice == 1:
        ptr = start
        while ptr.next != start:
            ptr = ptr.next
        if ptr == start:
            start = None
        else:
            ptr.next = start.next
            start = start.next
    elif choice == 2:
        ptr = start
        prev = None
        while ptr.next != start:
            prev = ptr
            ptr = ptr.next
        prev.next = start
        del ptr
    elif choice == 3:
        val = int(input("Enter the value to be deleted: "))
        prev = None
        ptr = start
        while ptr.data != val:
            prev = ptr
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                return start
        if prev is None:
            while ptr.next != start:
                ptr = ptr.next
            if ptr == start:
                start = None
            else:
                ptr.next = start.next
                start = start.next
        else:
            prev.next = ptr.next
            del ptr
    else:
        print("Invalid choice.")
    return start

def main():
    start = None
    option = 0
    print("NAMASKARAM! This program demonstrates insertion and deletion in a circular linked list(SINGLE).\n")

    while option != 5:
        print("\n\t\t**********MAIN MENU**********")
        print("1. Create a Circular Linked List")
        print("2. Display the Circular Linked List")
        print("3. Insert a node in the CLL")
        print("4. Delete a node in the CLL")
        print("5. Exit the program")
        option = int(input("\nEnter your choice : "))

        if option == 1:
            start = create_cll()
        elif option == 2:
            display_cll(start)
        elif option == 3:
            start = insert_node(start)
        elif option == 4:
            start = delete_node(start)
        elif option == 5:
            print("\nExiting...")
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
