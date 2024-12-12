def combSort(array):
    n = len(array)
    gap = n
    shrink_factor = 1.3
    Sorted = False

    while not Sorted:
        gap = int(gap / shrink_factor)

        if gap <= 1:
            gap = 1
            Sorted = True

        i = 0

        while i + gap < n:
            if array[i] > array[i + gap]:

                array[i], array[i + gap] = array[i + gap], array[i]
                Sorted = False

            i += 1
    return array


array = [12, 3, 125, 346, 47, 5, 6, 7, 546, 32, 42, 564, 34345]

print(combSort(array))
