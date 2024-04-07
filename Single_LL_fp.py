class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_ll():
    start = None
    print("\nType numbers to create a Linked list (enter -1 to end):")
    num = int(input())
    while num != -1:
        newNode = Node(num)
        if start is None:
            start = newNode
        else:
            ptr = start
            while ptr.next:
                ptr = ptr.next
            ptr.next = newNode
        num = int(input("Enter data to create the Linked-List (enter -1 to end): "))
    return start

def display_ll(start):
    if start is None:
        print("\nList is empty.")
        return start
    ptr = start
    print("\nLinked List:")
    while ptr:
        print(ptr.data, "-> ", end="")
        ptr = ptr.next
    print("NULL")
    return start

def insert_node(start):
    choice = int(input("\nChoose method of insertion:\n1) Insert at the beginning\n2) Insert at the end\n3) Insert after a specific value\n4) Insert before a specific value\n\nEnter your choice: "))
    if choice not in [1, 2, 3, 4]:
        print("Invalid choice.")
        return start

    num = int(input("\nEnter the data to be inserted: "))
    newNode = Node(num)

    if choice == 1:
        newNode.next = start
        start = newNode
    elif choice == 2:
        if start is None:
            start = newNode
        else:
            ptr = start
            while ptr.next:
                ptr = ptr.next
            ptr.next = newNode
    elif choice == 3 or choice == 4:
        val = int(input("Enter the value after/before which to insert: "))
        ptr = start
        prev = None
        while ptr and ptr.data != val:
            prev = ptr
            ptr = ptr.next
        if ptr is None:
            print("Value not found in the list.")
            return start
        if choice == 3:
            newNode.next = ptr.next
            ptr.next = newNode
        elif choice == 4:
            if prev is None:
                newNode.next = start
                start = newNode
            else:
                newNode.next = ptr
                prev.next = newNode
    return start

def delete_node(start):
    if start is None:
        print("\nList is empty. Nothing to delete.")
        return start

    choice = int(input("\nChoose method of deletion:\n1) Delete at the beginning\n2) Delete at the end\n3) Delete at a specific position\n\nEnter your choice: "))
    if choice not in [1, 2, 3]:
        print("Invalid choice.")
        return start

    if choice == 1:
        start = start.next
    elif choice == 2:
        if start.next is None:
            start = None
        else:
            ptr = start
            while ptr.next.next:
                ptr = ptr.next
            ptr.next = None
    elif choice == 3:
        pos = int(input("Enter the position to be deleted (1-based indexing): "))
        if pos < 1:
            print("Invalid position.")
            return start
        if pos == 1:
            start = start.next
        else:
            count = 1
            ptr = start
            prev = None
            while ptr and count < pos:
                prev = ptr
                ptr = ptr.next
                count += 1
            if ptr is None:
                print("Position not found in the list.")
                return start
            prev.next = ptr.next
    return start

start = None
option = 0

print("Namaskaram! The following code is for both insertion and deletion in a single linked list.")

while option != 5:
    print("\n\n\t\t**********MAIN MENU**********")
    print("1) Create a Linked-List")
    print("2) Display the Linked-List")
    print("3) Insert a node in the LL")
    print("4) Delete a node in the LL")
    print("5) Exit the program")
    option = int(input("\nEnter your choice (1-5): "))

    if option == 1:
        start = create_ll()
    elif option == 2:
        start = display_ll(start)
    elif option == 3:
        start = insert_node(start)
    elif option == 4:
        start = delete_node(start)
    elif option == 5:
        print("\nExiting...")
    else:
        print("\nTry again, Moye More event occurs for you, lol!")
