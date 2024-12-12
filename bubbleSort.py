def bubbleSort(array):
    n = len(array)

    for i in range(0, n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


array = [1, 124, 5, 6, 456, 34, 5345, 346, 34643, 3, 12, 214, 125, 15]

sorted_array = bubbleSort(array)

print(sorted_array)
