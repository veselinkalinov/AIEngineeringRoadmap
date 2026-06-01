# O(n^2)

def selection_sort(arr):
    for i in range(len(arr)-2):
        min_idx = i
        for j in range(i+1, len(arr)-1):
            if (arr[j] < arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [2, 6, 5, 1, 3, 4]
selection_sort(arr)
print(arr)
