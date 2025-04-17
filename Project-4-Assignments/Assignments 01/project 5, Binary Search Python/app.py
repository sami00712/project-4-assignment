def binary_search(list, target):
    left, right = 0, len(list) - 1

    while left <= right :
        mid = (left + right) // 2

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

list = [1, 3, 5, 7, 9, 11, 15] 
target = 5

results = binary_search(list, target)
print(f"Element {target} is at index :", results)

