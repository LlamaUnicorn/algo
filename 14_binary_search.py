from utils import timer


# 14.3 binary search
# @timer
# def bin_search(array, x):
#     """
#     Binary search algorithm
#
#     :param array: array
#     :param x: value we're looking for in an array
#     :return:
#     """
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if array[mid] < x:
#             left = mid + 1
#         else:
#             right = mid
#     return left < len(array) and array[left] == x


# @timer
# def bin_search(array, x):
#
#
# print(bin_search([1, 5, 10, 10, 19], 5))
# print(bin_search([1, 5, 8, 10, 20], 4))



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
# from bisect import *
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# q = map(int, input().split())
# a.sort()
# for query in q:
#     print(bisect_left(a, query), end=" ")

# 14.6 Грузовой лифт в отеле
from bisect import *
from itertools import *
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# q = map(int, input().split())
n = 4
a = [10, 10, 10, 10]
m = 6
q = [1, 5, 10, 15, 20, 25]
b = list(accumulate([1] + a))
for query in q:
    floor = bisect(b, query)
    print(floor if floor <= n else -1, end=' ')

