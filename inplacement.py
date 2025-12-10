def merge_count(a, low, mid, high):
    left = a[low:mid]
    right = a[mid:high]
    i = j = 0
    k = low
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
            count += len(left) - i
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    return count

def merge_sort_count(a, low, high):
    if high - low <= 1:
        return 0
    mid = (low + high) // 2
    count = merge_sort_count(a, low, mid)
    count += merge_sort_count(a, mid, high)
    count += merge_count(a, low, mid, high)
    return count


size = int(input())
arr = list(map(int, input().split()))[:size]

count_count = merge_sort_count(arr, 0, size)
print(count_count)
