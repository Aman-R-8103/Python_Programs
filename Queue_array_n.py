def main():
    size = int(input("Enter the size of the queue: "))
    queue_array = [None] * size
    front = -1
    rear = -1

    choice = 0
    while choice < 5:
        print("\n1. Insert the element in the queue.")
        print("2. Display the elements")
        print("3. Delete the element from the Queue")
        print("4. Peek the element")
        print("5. EXIT")
        choice = int(input("\nEnter your choice (1-5): "))

        if choice > 5 or choice < 1:
            print("Invalid choice")

        if choice == 1:
            value = int(input("Enter the value: "))

            # Enqueue logic
            if rear == size - 1:
                print("Queue is FULL")
            elif front == -1 and rear == -1:
                front = rear = 0
                queue_array[rear] = value
            else:
                rear += 1
                queue_array[rear] = value
        elif choice == 2:
            # Display Queue logic
            if front == -1 and rear == -1:
                print("Queue is Empty")
            else:
                for i in range(front, rear + 1):
                    print(queue_array[i])
        elif choice == 3:
            # Dequeue logic
            if front == -1 and rear == -1:
                print("Queue is Empty")
            elif front == rear:
                print("Deleted Element is:", queue_array[front])
                front = rear = -1
            else:
                print("Deleted Element is:", queue_array[front])
                front += 1
        elif choice == 4:
            # Peek logic
            if front == -1 and rear == -1:
                print("Queue is Empty")
            else:
                print(queue_array[front])

    print("Exiting...")

if __name__ == "__main__":
    main()
