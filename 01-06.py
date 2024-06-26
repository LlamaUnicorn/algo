from collections import Counter

# 5.1  вернуть сумму
# a, b = input().split()
# print(int(a) + int(b))

# 5.2 вернуть n-ое число Фибоначчи
# optional: try recursive with memoization
# n = int(input())
# f = [0, 1]
# while len(f) <= n:
#     f.append(f[-1] + f[-2])
# print(f[n])


# 5.3 Манхэттенское расстояние
# x1, x2 = input().split()
# y1, y2 = input().split()
# dx = abs(int(x1)-int(x2))
# dy = abs(int(y1)-int(y2))
# print(dx, dy)


# 5.4 Путь до ксерокса
# n, k = map(int, input().split())
# i = max(n // k, 1)
# ans1 = abs(n - k * i)
# i += 1
# ans2 = abs(n - k * i)
# print(min(ans1, ans2))


# 5.5 Проверка перестановки
# nums = list(map(int, input().split()))
# nums = [4, 2, 3]
# cnt = Counter(nums)
# ans = (max(nums) == len(nums) and max(cnt.values()) == 1)
# print('OK' if ans else 'BAD')

# REPEAT 5.6 Циклы перестановки
# perm = map(int, input().split())
# perm = [1, 3, 2]
# perm = [x - 1 for x in perm]
# n = len(perm)
# ans = 0
# visited = [False] * n
# for start in range(n):
#     if visited[start]:
#         continue
#     ans += 1
#     current = start
#     while True:
#         visited[current] = True
#         current = perm[current]
#         if current == start:
#             break
# print(ans)


# 6.1 Пара с минимальным произведением
# n = int(input())
# a = list(map(int, input().split()))
# n = 4
# a = [1, 2, 3, 4]
# a.sort()
# ans1 = a[0] * a[1]
# ans2 = a[0] * a[-1]
# ans3 = a[-2] * a[-1]
# print(min(ans1, ans2, ans3))


# # 6.2 Тайная жизнь деревьев
# n = int(input())
# a = map(int, input().split())
# b = sorted(a)
# ans = max(cur - i for i, cur in enumerate(b))
# print(ans)
#
#
# # 6.3 Подписывание открыток
# a, b = map(int, input().split())
# a //= 10
# b //= 10
# c = (a + b) // 3
# print(min(a, b, c))


# 6.4 Исправление перестановки
# # n = int(input())
# # a = list(map(int, input().split()))
# n = 4
# a = [1, 100, 3, 3]
# free = set(range(1, n + 1))
# free -= set(a)
# print(len(free))
# used = set()
# for i in range(n):
#     if a[i] > n or a[i] in used:
#         a[i] = free.pop()
#     used.add(a[i])


# 6.5 Минимальный палиндром
# from collections import *
# # s = input()
# s = 'aabbcd'
# cnt = Counter(s)
# half = ''
# mid = ''
# for c in sorted(cnt.keys()):
#     half += c * (cnt[c] // 2)
#     if cnt[c] % 2 and not mid:
#         mid = c
# ans = half + mid + half[::-1]
# print(ans)


# 6.6 Исключающее ИЛИ от 1 до n
# n = int(input())
# k = n % 4
# if k == 1:
#     ans = 1
# elif k == 2:
#     ans = n + 1
# elif k == 3:
#     ans = 0
# else:
#     ans = n
# print(ans)


# 6.7 Врачи и посетители
# import sys
# n = int(input())
# a = []
# for index in range(n):
#     left, right = input().split()
#     a.append([int(left), int(right), index])
# doc_free_time = [0] * 2
# ans = [None] * n
# for left, right, index in sorted(a):
#     for doc in range(2):
#         if doc_free_time[doc] <= left:
#             doc_free_time[doc] = right
#             ans[index] = 'AB'[doc]
#             break
#     else:
#         print('No solution')
#         sys.exit(0)
# print(''.join(ans))

# # 6.8 Минимизация перепадов
# n = int(input())
# a = map(int, input().split())
# b = list(sorted((h, idx) for idx, h in enumerate(a)))
# ans = b[::2] + b[1::2][::-1]
# ans = list(idx for _, idx in ans)
# print(*ans)


# 6.9 Одномерный геометрический центр
n = int(input())
x = map(int, input().split())
ans = list(sorted(x))[n // 2]
print(ans)


