def main():
    size = int(input("Enter size of array: "))  # Read the size of the array
    new_array = []  # Create an empty list to store the array elements

    print(f"Enter {size} elements for the array:")
    for i in range(size):
        new_array.append(int(input()))  # Read each element and append it to the list

    print("The elements of the array are", end=" ")
    for num in new_array:
        print(num, end=" ")

if __name__ == "__main__":
    main()
