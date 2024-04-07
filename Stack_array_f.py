MAX_SIZE = 5
stack_list = []
top_index = -1

def peek_element():
    global top_index
    if top_index == -1:
        print("Stack is empty")
    else:
        print(stack_list[top_index])

def pop_element():
    global top_index
    if top_index == -1:
        print("Stack is empty")
    else:
        item = stack_list[top_index]
        top_index -= 1
        print(f"Popped value is: {item}")

def display_elements():
    global top_index
    for i in range(top_index, -1, -1):
        print(stack_list[i])

def push_element(value):
    global top_index
    if top_index == MAX_SIZE - 1:
        print("Stack is Full")
    else:
        top_index += 1
        stack_list.append(value)

def main():
    global top_index
    choice = 0
    while choice != 5:
        print("\t\tMAIN MENU for operations on Stack in array")
        print("1. Push the element")
        print("2. Pop the element")
        print("3. Peek the element")
        print("4. Display the elements")
        print("5. EXIT")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            value = int(input("Enter the value: "))
            push_element(value)
        elif choice == 2:
            pop_element()
        elif choice == 3:
            peek_element()
        elif choice == 4:
            display_elements()
        elif choice == 5:
            print("Exiting...")

if __name__ == "__main__":
    main()
