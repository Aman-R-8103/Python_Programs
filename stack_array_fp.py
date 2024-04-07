MAX_SIZE = 101

stackArray = [0] * MAX_SIZE
topPtr = -1  # Pointer to the top of the stack

def pushElement(value):
    global topPtr
    if topPtr == MAX_SIZE - 1:
        print("Stack is Full")
    else:
        topPtr += 1  # Move the pointer to the next available position
        stackArray[topPtr] = value  # Store the value at the top position

def displayElements():
    global topPtr
    if topPtr == -1:
        print("Stack is empty")
    else:
        print("Stack elements:")
        ptr = topPtr
        while ptr >= 0:
            print(stackArray[ptr])
            ptr -= 1  # Move the pointer down

def popElement():
    global topPtr
    if topPtr == -1:
        print("Stack is Empty")
    else:
        item = stackArray[topPtr]  # Get the value at the top position
        topPtr -= 1  # Move the pointer down to the previous position
        print("Popped value is:", item)

def peekElement():
    global topPtr
    if topPtr == -1:
        print("Stack is empty")
    else:
        print("Top element is:", stackArray[topPtr])

def main():
    global topPtr
    topPtr = -1  # Initialize topPtr to -1

    while True:
        print("\t\tMAIN MENU for operations on Stack in array")
        print("1. Push the element")
        print("2. Pop the element")
        print("3. Peek the element")
        print("4. Display the elements")
        print("5. EXIT")

        choice = int(input("\nEnter your choice (1-5): "))
        if choice > 5 or choice < 1:
            print("Invalid choice")
            continue

        if choice == 1:
            value = int(input("Enter the value: "))
            pushElement(value)
        elif choice == 2:
            popElement()
        elif choice == 3:
            peekElement()
        elif choice == 4:
            displayElements()
        elif choice == 5:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
