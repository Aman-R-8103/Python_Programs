def read_array_size():
    size = int(input("Enter size of array: "))
    return size

def create_array(size):
    new_array = []
    print(f"Enter {size} elements for the array:")
    for _ in range(size):
        new_array.append(int(input()))
    return new_array

def display_array(array):
    print("The elements of the array are:", end=" ")
    for num in array:
        print(num, end=" ")
    print()

def main():
    size = read_array_size()
    new_array = create_array(size)
    display_array(new_array)

if __name__ == "__main__":
    main()

