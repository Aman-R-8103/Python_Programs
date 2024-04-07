def input_array():
    size = int(input("Enter the size of the array: "))
    arr = []

    print(f"Enter {size} elements:")
    for _ in range(size):
        arr.append(int(input()))

    return arr


def display_array(arr):
    print(" ".join(map(str, arr)))


def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = input_array()

print("Unsorted array:")
display_array(arr)

bubble_sort(arr)

print("Sorted array:")
display_array(arr)
