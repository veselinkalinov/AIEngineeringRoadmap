arr = [4, 12, 28, 33, 46, 57, 60, 71, 89, 95]
target = 12
start = 0
end = len(arr)-1

for _ in range(end):
    mid = end // 2
    if arr[mid] == target:
        print(f"Target is at idx:{mid}")
        break
    elif arr[mid] > target:
        end = mid - 1
        continue
    else:
        start = mid + 1
        continue
