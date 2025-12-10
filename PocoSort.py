# def partition(arr, lo, hi):
#     """ Hoare Partition function """
#     pivot = arr[(lo + hi) // 2]
#     i = lo - 1
#     j = hi + 1
#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
#         if i >= j:
#             return j
#         arr[i], arr[j] = arr[j], arr[i]
#
# def quick_sort(arr, lo, hi):
#     """ Quick sort function using Hoare Partitioning"""
#     if lo < hi:
#         p = partition(arr, lo, hi)
#         quick_sort(arr, lo, p)
#         quick_sort(arr, p + 1, hi)
#
#
# def test_parity(arr, sorted_arr):
#     for index in range(len(arr)):
#         if arr[index] % 2 == 0 and sorted_arr[index] % 2 == 0:
#             pass
#         elif arr[index] % 2 == 1 and sorted_arr[index] % 2 == 1:
#             pass
#         else:
#             return False
#     return True
# tests_num = int(input())
# test_list = []
# sort_list = []
# for i in range(tests_num):
#     test_size = int(input())
#     a = list(map(int, input().split()))
#     test_list.append(a.copy())
#     quick_sort(a, 0, len(a)-1)
#     sort_list.append(a)
#
#
# for i in range(tests_num):
#     if test_parity(test_list[i],sort_list[i]):
#         print("YES")
#     else:
#         print("NO")