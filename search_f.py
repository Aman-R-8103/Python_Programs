def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Return the index of the key if found
    return -1  # Return -1 if key not found


def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid  # Return the index of the key if found
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if key not found


def main():
    size = int(input("Enter the size of the array: "))
    arr = [int(input(f"Enter element {i + 1}: ")) for i in range(size)]
    key = int(input("Enter the element to search: "))

    choice = int(input("""
Choose the search algorithm:
1. Linear Search
2. Binary Search
Enter your choice: """))

    if choice == 1:
        print("\nLinear Search:")
        index = linear_search(arr, key)
        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found in the array")
    elif choice == 2:
        print("\nBinary Search:")
        index = binary_search(arr, key)
        if index != -1:
            print(f"Element found at index {index}")
        else:
            print("Element not found in the array")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
