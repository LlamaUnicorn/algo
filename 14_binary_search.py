# 14.3 binary search
# def bin_search(a, x):
#     left = 0
#     right = len(a) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if a[mid] < x:
#             left = mid + 1
#         else:
#             right = mid
#         return (left < len(a) and a[left] == x)


# print(bin_search([1, 5, 8, 10, 20], 5))
# print(bin_search([1, 3, 5, 7, 9], 3))


# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == target:
#             return mid
#         elif guess > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# arr = [1, 3, 5, 7, 9]
# print(binary_search(arr, 3))  # Output: 1
# print(binary_search(arr, -1))  # Output: None

# 14.5 Подсчет меньших чисел
from bisect import *
n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = map(int, input().split())
a.sort()
for query in q:
    print(bisect_left(a, query), end=" ")
