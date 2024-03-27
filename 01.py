# 5.1 return sum
# a, b = input().split()
# print(int(a) + int(b))


# 5.2 return the n-th Fibonacci num
# optional: try recursive with memoization
# n = int(input())
# f = [0, 1]
# while len(f) <= n:
#     f.append(f[-1] + f[-2])
# print(f[n])


# 5.3 Manhattan distance
# x1, x2 = input().split()
# y1, y2 = input().split()
# dx = abs(int(x1)-int(x2))
# dy = abs(int(y1)-int(y2))
# print(dx, dy)


# 5.4
n, k = map(int, input().split())
i = max(n // k, 1)
ans1 = abs(n - k * i)
i += 1
ans2 = abs(n - k * i)
print(min(ans1, ans2))
