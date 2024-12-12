def insertionSort(array):
    for i in range(1, len(array)):

        key = array[i]

        j = i - 1

        while j >= 0 and array[j] > key:

            array[j + 1] = array[j]

            j -= 1

        array[j + 1] = key

    return array


array = [1, 124, 124, 12, 31, 3124, 52, 12, 4432, 5, 634]

sortedArray = insertionSort(array)

print(sortedArray)
