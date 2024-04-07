class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def create_dll():
    start = None
    num = int(input("Enter numbers to create a Doubly Linked List (enter -1 to end):\n"))

    while num != -1:
        new_node = Node(num)

        if start is None:
            start = new_node
        else:
            ptr = start
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr

        num = int(input("Enter data to create the Doubly Linked List (enter -1 to end): "))

    return start

def display_dll(start):
    ptr = start
    if start is None:
        print("\nList is empty.")
    else:
        print("\nDoubly Linked List: NULL <- ", end="")
        while ptr is not None:
            print(ptr.data, "<-> ", end="")
            ptr = ptr.next
        print("NULL")

def insert_Node(start):
    choice = int(input("\nChoose method of insertion:\n1. Insert at the beginning\n2. Insert at the end\n3. Insert after a specific value\n4. Insert before a specific value\n\nEnter your choice: "))
    num = int(input("Enter the data to be inserted: "))
    new_node = Node(num)

    if choice == 1:
        new_node.next = start
        if start:
            start.prev = new_node
        start = new_node
    elif choice == 2:
        if start is None:
            start = new_node
        else:
            ptr = start
            while ptr.next:
                ptr = ptr.next
            ptr.next = new_node
            new_node.prev = ptr
    elif choice == 3:
        val = int(input("Enter the value after which you want to insert: "))
        ptr = start
        while ptr and ptr.data != val:
            ptr = ptr.next
        if ptr:
            new_node.next = ptr.next
            if ptr.next:
                ptr.next.prev = new_node
            ptr.next = new_node
            new_node.prev = ptr
    elif choice == 4:
        val = int(input("Enter the value before which you want to insert: "))
        ptr = start
        while ptr and ptr.data != val:
            ptr = ptr.next
        if ptr:
            new_node.prev = ptr.prev
            if ptr.prev:
                ptr.prev.next = new_node
            else:
                start = new_node
            new_node.next = ptr
            ptr.prev = new_node
    else:
        print("\nInvalid choice.")

    return start

def delete_Node(start):
    if start is None:
        print("\nList is empty. Nothing to delete.")
        return start

    choice = int(input("\nChoose method of deletion:\n1. Delete at the beginning\n2. Delete at the end\n3. Delete a specific value\n\nEnter your choice: "))

    if choice == 1:
        start = start.next
        if start:
            start.prev = None
    elif choice == 2:
        ptr = start
        while ptr.next:
            ptr = ptr.next
        if ptr.prev:
            ptr.prev.next = None
        else:
            start = None
    elif choice == 3:
        val = int(input("Enter the value to be deleted: "))
        ptr = start
        while ptr and ptr.data != val:
            ptr = ptr.next
        if ptr:
            if ptr.prev:
                ptr.prev.next = ptr.next
            else:
                start = ptr.next
            if ptr.next:
                ptr.next.prev = ptr.prev
    else:
        print("\nInvalid choice.")

    return start

def main():
    start = None
    option = 0
    print("Namaskaram! This program demonstrates insertion and deletion in a doubly linked list.\n")

    while option != 5:
        print("\n\t\t**********MAIN MENU**********")
        print("1. Create a Doubly Linked List")
        print("2. Display the Doubly Linked List")
        print("3. Insert a node in the DLL")
        print("4. Delete a node in the DLL")
        print("5. Exit the program")
        option = int(input("\nEnter your choice : "))

        if option == 1:
            start = create_dll()
        elif option == 2:
            display_dll(start)
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
