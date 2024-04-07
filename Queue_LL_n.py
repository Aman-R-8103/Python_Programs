class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Value {value} enqueued successfully.")

    def dequeue(self):
        if self.front is None:
            print("Queue is empty. Cannot dequeue.")
        else:
            temp = self.front
            value = temp.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            del temp
            print(f"Dequeued value: {value}")

    def display_queue(self):
        if self.front is None:
            print("Queue is empty.")
        else:
            temp = self.front
            print("Queue: ", end="")
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()

def main():
    queue = QueueLinkedList()
    choice = 0

    while choice != 4:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display Queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter the value to enqueue: "))
            queue.enqueue(value)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.display_queue()
        elif choice == 4:
            print("Exiting...")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
