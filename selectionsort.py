def selectionSort(array):
    size = len(array)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSort(arr)
print('The array after sorting in ascending order by selection sort is:')
print(arr)
