def linear_search(arr, size, key):
    found = False
    index = -1
    for i in range(size):
        if arr[i] == key:
            found = True
            index = i
            break
    if found:
        print(f"Element found at index {index}")
    else:
        print("Element not found in the array")


def binary_search(arr, size, key):
    found = False
    index = -1
    low = 0
    high = size - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            found = True
            index = mid
            break
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        print(f"Element found at index {index}")
    else:
        print("Element not found in the array")


def main():
    size = int(input("Enter the size of the array: "))
    arr = []
    print(f"Enter {size} elements in sorted order:")
    for _ in range(size):
        arr.append(int(input()))
    key = int(input("Enter the element to search: "))

    choice = int(input("""
Choose the search algorithm:
1. Linear Search
2. Binary Search
Enter your choice: """))

    if choice == 1:
        print("\nLinear Search:")
        linear_search(arr, size, key)
    elif choice == 2:
        print("\nBinary Search:")
        binary_search(arr, size, key)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
