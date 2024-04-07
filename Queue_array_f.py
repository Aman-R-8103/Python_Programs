MAX_SIZE = 1001

queueArray = [0] * MAX_SIZE
frontIndex = -1
rearIndex = -1

def addElement(value):
    global frontIndex, rearIndex
    
    if rearIndex == MAX_SIZE - 1:
        print("Queue is FULL")
    elif frontIndex == -1 and rearIndex == -1:
        frontIndex = rearIndex = 0
        queueArray[rearIndex] = value
    else:
        rearIndex += 1
        queueArray[rearIndex] = value

def showElements(front, rear):
    if front == -1 and rear == -1:
        print("Queue is Empty")
    else:
        for i in range(front, rear + 1):
            print(queueArray[i])

def removeElement(front, rear):
    global frontIndex, rearIndex
    
    if front == -1 and rear == -1:
        print("Queue is Empty")
    elif front == rear:
        print("Deleted Element is:", queueArray[front])
        frontIndex = rearIndex = -1
    else:
        print("Deleted Element is:", queueArray[front])
        frontIndex += 1

def peek():
    global frontIndex
    
    if frontIndex == -1 and rearIndex == -1:
        print("Queue is Empty")
    else:
        print(queueArray[frontIndex])

def main():
    global frontIndex, rearIndex
    
    choice = 0

    while choice != 5:
        print("\n\t\tMain Menu for Operations on queue")
        print("1. Insert Element")
        print("2. Display the elements")
        print("3. Delete the element")
        print("4. Peek the element")
        print("5. EXIT")
        choice = int(input("\nEnter your choice (1-5): "))

        if choice > 5 or choice < 1:
            print("Invalid choice")

        if choice == 1:
            value = int(input("Enter the value: "))
            addElement(value)
        elif choice == 2:
            showElements(frontIndex, rearIndex)
        elif choice == 3:
            removeElement(frontIndex, rearIndex)
        elif choice == 4:
            peek()
        elif choice == 5:
            print("Exiting...")

if __name__ == "__main__":
    main()

