size = int(input("Enter the size of the array: "))
arr = []

print(f"Enter {size} elements in sorted order:")
for _ in range(size):
    arr.append(int(input()))

key = int(input("Enter the element to search: "))

print("\nChoose the search algorithm:")
print("1. Linear Search")
print("2. Binary Search")
choice = int(input("Enter your choice: "))

found = False
index = -1

if choice == 1:
    print("\nLinear Search:")
    for i in range(size):
        if arr[i] == key:
            found = True
            index = i
            break
elif choice == 2:
    print("\nBinary Search:")
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
