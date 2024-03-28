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


# Проверка перестановки
# nums = list(map(int, input().split()))
# nums = [4, 2, 3]
# cnt = Counter(nums)
# ans = (max(nums) == len(nums) and max(cnt.values()) == 1)
# print('OK' if ans else 'BAD')

# 5.6 Циклы перестановки
# perm = map(int, input().split())
perm = [1, 3, 2]
perm = [x - 1 for x in perm]
n = len(perm)
ans = 0
visited = [False] * n
for start in range(n):
    if visited[start]:
        continue
    ans += 1
    current = start
    while True:
        visited[current] = True
        current = perm[current]
        if current == start:
            break
print(ans)

