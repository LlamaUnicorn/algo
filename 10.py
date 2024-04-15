# # Наибольший общий делитель. Алгоритм Евклида
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# def gcd_recursive(a, b):
#     return gcd(b, a % b) if b else a
#
#
# def gcd_iterative(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# print(gcd(12, 18))
# print(gcd_recursive(12, 18))
# print(gcd_iterative(12, 18))
#
#
# # 10.9 НОД нескольких чисел
# def gcd_list(a):
#     result = 0
#     for item in a:
#         return gcd(result, item)
#     return result


# 11.2 Парковочные места
from heapq import *
n = int(input())
events = []
for car in range(n):
    tadd, tremove = map(int, input().split())
    events.append((tadd, 0, car))
    events.append((tremove, 1, car))
ans = [None] * n
free_slots = list(range(1, n + 1))
heapify(free_slots)
for t, type, car in sorted(events):
    if type == 0:
        ans[car] = heappop(free_slots)
    else:
        heappush(free_slots, ans[car])
print(*ans)


# 12.3 Объединение отрезков
# def merge_segm(segms):
#     res = []
#     for left, right in sorted(segms):
#         if res and left <= res[-1][1]:
#             res[-1][1] = max(res[-1][1], right)
#         else:
#             res.append([left, right])
#     return res


# 12.5 Стрельба по отрезкам
# n = int(input())
# events = []
# for i in range(n):
#     l, r = map(int, input().split())
#     events.append((l, -1, i))
#     events.append((r, +1, i))
# ans = 0
# is_shot = [False] * n
# active = []
# for x, tp, idx in sorted(events):
#     if tp == -1:
#         active.append(idx)
#         continue
#     if is_shot[idx]:
#         continue
#     ans += 1
#     for i in active:
#         is_shot[i] = True
#     active = []
# print(ans)
