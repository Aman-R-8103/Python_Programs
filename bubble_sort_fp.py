def input_array():
    size = int(input("Enter the size of the array: "))
    arr = []

    print(f"Enter {size} elements:")
    for _ in range(size):
        arr.append(int(input()))

    return arr, size


def display_array(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()


def bubble_sort(arr, size):
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr, size = input_array()

print("Unsorted array:")
display_array(arr, size)

bubble_sort(arr, size)

print("Sorted array:")
display_array(arr, size)
