size = int(input("Enter the size of the array: "))
arr = []

# Input array elements
print(f"Enter {size} elements:")
for _ in range(size):
    arr.append(int(input()))

# Display the unsorted array
print("Unsorted array:")
for elem in arr:
    print(elem, end=" ")
print()

# Bubble sort logic
for i in range(size - 1):
    for j in range(size - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap arr[j] and arr[j+1]
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Display the sorted array
print("Sorted array:")
for elem in arr:
    print(elem, end=" ")
print()
