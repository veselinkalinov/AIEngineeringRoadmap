# O(n^2)

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if (arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


arr = [2, 6, 5, 1, 3, 4]
bubble_sort(arr)
print(arr)
