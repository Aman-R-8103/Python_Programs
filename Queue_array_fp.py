def enqueue_element(queue_array, front_ptr, rear_ptr, size):
    value = int(input("Enter the value: "))
    
    if rear_ptr[0] == size - 1:
        print("Queue is FULL")
    elif front_ptr[0] == -1 and rear_ptr[0] == -1:
        front_ptr[0] = rear_ptr[0] = 0
        queue_array[rear_ptr[0]] = value
    else:
        rear_ptr[0] += 1
        queue_array[rear_ptr[0]] = value

def display_queue(queue_array, front, rear):
    if front[0] == -1 and rear[0] == -1:
        print("Queue is Empty")
    else:
        for i in range(front[0], rear[0] + 1):
            print(queue_array[i])

def dequeue_element(front_ptr, rear_ptr):
    if front_ptr[0] == -1 and rear_ptr[0] == -1:
        print("Queue is Empty")
    elif front_ptr[0] == rear_ptr[0]:
        print("Deleted Element is:", front_ptr[0])
        front_ptr[0] = rear_ptr[0] = -1
    else:
        print("Deleted Element is:", front_ptr[0])
        front_ptr[0] += 1

def peek_queue(queue_array, front):
    if front[0] == -1:
        print("Queue is Empty")
    else:
        print(queue_array[front[0]])

def main():
    size = int(input("Enter the size of the queue: "))
    queue_array = [0] * size
    front = [-1]
    rear = [-1]

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
            enqueue_element(queue_array, front, rear, size)
        elif choice == 2:
            display_queue(queue_array, front, rear)
        elif choice == 3:
            dequeue_element(front, rear)
        elif choice == 4:
            peek_queue(queue_array, front)
        elif choice == 5:
            print("Exiting...")

if __name__ == "__main__":
    main()

