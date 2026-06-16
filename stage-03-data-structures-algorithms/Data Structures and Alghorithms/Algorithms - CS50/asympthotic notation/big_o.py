# O(1) — constant time
def get_first(lst):
    steps = 1
    result = lst[0]
    print(f"O(1): {steps} step regardless of n={len(lst)}")
    return result

# O(n) — linear time
def linear_search(lst, target):
    steps = 0
    for item in lst:
        steps += 1
        if item == target:
            print(f"O(n): {steps} steps for n={len(lst)}")
            return True
    print(f"O(n): {steps} steps (not found) for n={len(lst)}")
    return False

# O(log n) — logarithmic time
def binary_search(lst, target):
    steps = 0
    low, high = 0, len(lst) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            print(f"O(log n): {steps} steps for n={len(lst)}")
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"O(log n): {steps} steps (not found) for n={len(lst)}")
    return False

# Run on lists of increasing size
for size in [100, 1000, 10000]:
    sorted_list = list(range(size))
    print(f"\n--- List size: {size} ---")
    get_first(sorted_list)
    linear_search(sorted_list, -1)   # worst case: not found
    binary_search(sorted_list, -1)   # worst case: not found
