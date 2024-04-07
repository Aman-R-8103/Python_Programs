def main():
    size = int(input("Enter the size of the array: "))

    # Dynamically allocate memory for the array
    new_array = [0] * size

    # Read array elements using a loop
    print(f"Enter {size} elements for the array:")
    for i in range(size):
        new_array[i] = int(input())

    # Display array elements using a loop
    print("The elements of the array are:", end=" ")
    for num in new_array:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    main()

