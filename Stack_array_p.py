MAX_SIZE = 101
stack_list = []
top_index = 0

while True:
    print("\t\tMAIN MENU for operations on Stack in array")
    print("1. Push the element")
    print("2. Pop the element")
    print("3. Display the elements")
    print("4. Peek the element")
    print("5. EXIT")
    choice = int(input("\nEnter your choice (1-5): "))

    if choice > 5 or choice < 1:
        print("Invalid choice")
        continue

    if choice == 1:
        if top_index == MAX_SIZE:
            print("Stack is Full")
        else:
            value = int(input("Enter the value: "))
            stack_list.append(value)
            top_index += 1
    elif choice == 2:
        if top_index == 0:
            print("Stack is Empty")
        else:
            value = stack_list.pop()
            top_index -= 1
            print(f"Popped value is: {value}")
    elif choice == 3:
        if top_index == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(top_index):
                print(stack_list[i])
    elif choice == 4:
        if top_index == 0:
            print("Stack is empty")
        else:
            print(f"Top element is: {stack_list[top_index - 1]}")
    elif choice == 5:
        print("Exiting...")
        break

