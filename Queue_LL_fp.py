class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue_element(self, x):
        new_node = QueueNode(x)
        if self.head is None and self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue_element(self):
        if self.head is None and self.tail is None:
            print("Queue is Empty")
        else:
            print("Deleted element", self.head.value)
            self.head = self.head.next

    def peek_queue(self):
        if self.head is None and self.tail is None:
            print("Queue is Empty")
        else:
            print(self.head.value)

    def display_queue(self):
        if self.head is None and self.tail is None:
            print("Queue is Empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

def main():
    queue = QueueLinkedList()
    choice = 0

    while choice < 5:
        print("\n MENU FOR OPERATION ON QUEUE IN ll")
        print("1. Insert the element in the Queue.")
        print("2. Display")
        print("3. Delete the element from Queue")
        print("4. Peek the element")
        print("5. EXIT")
        choice = int(input("\nEnter your choice (1-5): "))

        if choice == 1:
            x = int(input("Enter the data: "))
            queue.enqueue_element(x)
        elif choice == 2:
            queue.display_queue()
        elif choice == 3:
            queue.dequeue_element()
        elif choice == 4:
            queue.peek_queue()
        elif choice == 5:
            print("OR BHAI AA GYE SAWAAD DSA KE")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

