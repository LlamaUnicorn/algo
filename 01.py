# 5.1 return sum
# a, b = input().split()
# print(int(a) + int(b))


# 5.2 return the n-th Fibonacci num
# optional: try recursive with memoization
n = int(input())
f = [0, 1]
while len(f) <= n:
    f.append(f[-1] + f[-2])
print(f[n])


# 5.3

