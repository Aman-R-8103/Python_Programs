class Node:
    def __init__(self, value):
        self.value = value
        self.nextPtr = None

class StackLinkedList:
    def __init__(self):
        self.topPtr = None

    def peekElement(self):
        if self.topPtr is None:
            print("Stack is Empty")
        else:
            print("The top of the Data is", self.topPtr.value)

    def displayElements(self):
        if self.topPtr is None:
            print("Stack is Empty")
        else:
            temp = self.topPtr
            while temp:
                print(temp.value)
                temp = temp.nextPtr

    def popElement(self):
        if self.topPtr is None:
            print("The stack is Empty")
        else:
            temp = self.topPtr
            self.topPtr = self.topPtr.nextPtr
            del temp

    def pushElement(self, data):
        newNode = Node(data)
        newNode.nextPtr = self.topPtr
        self.topPtr = newNode

stack = StackLinkedList()

while True:
    print("\t\tMAIN MENU for operations on Stack in array")
    print("1. Push the element")
    print("2. Peek the element")
    print("3. Pop the element")
    print("4. Display")
    print("5. EXIT")
    choice = int(input("\nEnter your choice (1-5): "))

    if choice > 5 or choice < 1:
        print("Invalid choice")
        continue

    if choice == 1:
        data = int(input("Enter the data: "))
        stack.pushElement(data)
    elif choice == 2:
        stack.peekElement()
    elif choice == 3:
        stack.popElement()
    elif choice == 4:
        stack.displayElements()
    elif choice == 5:
        print("Exiting...")
        break
