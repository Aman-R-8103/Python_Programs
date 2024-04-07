class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_cdll():
    start = None
    while True:
        num = int(input("Enter a number to create a Circular Doubly Linked List (enter -1 to end): "))
        if num == -1:
            break
        new_node = Node(num)
        if start is None:
            start = new_node
            start.next = start
            start.prev = start
        else:
            new_node.prev = start.prev
            new_node.next = start
            start.prev.next = new_node
            start.prev = new_node
    return start

def display_cdll(start):
    if start is None:
        print("\nList is empty.")
        return
    ptr = start
    print("\nCircular Doubly Linked List:", end=" ")
    while True:
        print(ptr.data, "->", end=" ")
        ptr = ptr.next
        if ptr == start:
            break
    print("(head)")

def insert_Node(start):
    if start is None:
        print("List is empty. Cannot insert.")
        return start

    new_data = int(input("\nEnter the data to be inserted: "))
    choice = int(input("Choose method of insertion:\n1. Insert at the beginning\n2. Insert at the end\n3. Insert after a specific value\n4. Insert before a specific value\n"))
    new_node = Node(new_data)

    if choice == 1:
        new_node.next = start
        new_node.prev = start.prev
        start.prev.next = new_node
        start.prev = new_node
        start = new_node
    elif choice == 2:
        new_node.next = start
        new_node.prev = start.prev
        start.prev.next = new_node
        start.prev = new_node
    elif choice == 3:
        val = int(input("Enter the value after which you want to insert: "))
        ptr = start
        while ptr.data != val:
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                return start
        new_node.prev = ptr
        new_node.next = ptr.next
        ptr.next.prev = new_node
        ptr.next = new_node
    elif choice == 4:
        val = int(input("Enter the value before which you want to insert: "))
        ptr = start
        while ptr.data != val:
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                return start
        new_node.prev = ptr.prev
        new_node.next = ptr
        ptr.prev.next = new_node
        ptr.prev = new_node
        if ptr == start:
            start = new_node
    else:
        print("Invalid choice.")
    return start

def delete_Node(start):
    if start is None:
        print("List is empty. Nothing to delete.")
        return start

    choice = int(input("\nChoose method of deletion:\n1. Delete at the beginning\n2. Delete at the end\n3. Delete a specific value\n"))
    if choice == 1:
        start.next.prev = start.prev
        start.prev.next = start.next
        start = start.next
    elif choice == 2:
        start.prev.prev.next = start
        start.prev = start.prev.prev
    elif choice == 3:
        val = int(input("Enter the value to be deleted: "))
        ptr = start
        while ptr.data != val:
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                return start
        ptr.prev.next = ptr.next
        ptr.next.prev = ptr.prev
        if ptr == start:
            start = start.next
    else:
        print("Invalid choice.")
    return start

def main():
    start = None
    option = 0
    print("NAMASKARAM! This program demonstrates insertion and deletion in a circular doubly linked list.\n")

    while option != 5:
        print("\n\t\t**********MAIN MENU**********")
        print("1. Create a Circular Doubly Linked List")
        print("2. Display the Circular Doubly Linked List")
        print("3. Insert a node in the CDLL")
        print("4. Delete a node in the CDLL")
        print("5. Exit the program")
        option = int(input("\nEnter your choice : "))

        if option == 1:
            start = create_cdll()
        elif option == 2:
            display_cdll(start)
        elif option == 3:
            start = insert_Node(start)
        elif option == 4:
            start = delete_Node(start)
        elif option == 5:
            print("\nExiting...")
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
