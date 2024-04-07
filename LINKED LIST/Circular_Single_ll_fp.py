class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_cll():
    start = None
    num = int(input("Enter numbers to create a Circular Linked List (enter -1 to end):\n"))

    while num != -1:
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

        num = int(input("Enter data to create the Circular Linked List (enter -1 to end): "))

    return start

def display_cll(start):
    ptr = start

    if start is None:
        print("\nList is empty.")
        return

    print("\nCircular Linked List: ", end="")
    while True:
        print(ptr.data, "-> ", end="")
        ptr = ptr.next
        if ptr == start:
            break
    print("... (circular)")

def insert_Node(start):
    choice = int(input("\nChoose method of insertion:\n1. Insert at the beginning\n2. Insert at the end\n3. Insert after a specific value\n4. Insert before a specific value\n\nEnter your choice: "))
    num = int(input("Enter the data to be inserted: "))
    new_node = Node(num)

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
        while True:
            if ptr.data == val:
                new_node.next = ptr.next
                ptr.next = new_node
                break
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                break
    elif choice == 4:
        val = int(input("Enter the value before which you want to insert: "))
        ptr = start
        while True:
            if ptr.next.data == val:
                new_node.next = ptr.next
                ptr.next = new_node
                break
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                break
    else:
        print("\nInvalid choice.")

    return start

def delete_Node(start):
    choice = int(input("\nChoose method of deletion:\n1. Delete at the beginning\n2. Delete at the end\n3. Delete a specific value\n\nEnter your choice: "))

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
        while ptr.next.next != start:
            ptr = ptr.next
        ptr.next = start
    elif choice == 3:
        val = int(input("Enter the value to be deleted: "))
        ptr = start
        prev = None
        while True:
            if ptr.data == val:
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
                break
            prev = ptr
            ptr = ptr.next
            if ptr == start:
                print("Value not found in the list.")
                break
    else:
        print("\nInvalid choice.")

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
            start = insert_Node(start)
        elif option == 4:
            start = delete_Node(start)
        elif option == 5:
            print("\nExiting...")
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
