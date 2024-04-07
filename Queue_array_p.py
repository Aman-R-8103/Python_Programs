def main():
    size = int(input("Enter the size of the queue: "))
    queue_array = [None] * size
    front = 0
    rear = 0

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
            if rear - front == size - 1:
                print("Queue is FULL")
            else:
                queue_array[rear] = value
                rear += 1
        elif choice == 2:
            # Display Queue logic
            if front == rear:
                print("Queue is Empty")
            else:
                for i in range(front, rear):
                    print(queue_array[i])
        elif choice == 3:
            # Dequeue logic
            if front == rear:
                print("Queue is Empty")
            else:
                print("Deleted Element is:", queue_array[front])
                front += 1
        elif choice == 4:
            # Peek logic
            if front == rear:
                print("Queue is Empty")
            else:
                print(queue_array[front])

    print("Exiting...")

if __name__ == "__main__":
    main()
