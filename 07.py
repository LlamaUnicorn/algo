# 7.1 Морской бой
import sys
FIELD = 102
a = [[0] * FIELD] * FIELD
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1 - 1, x2 + 2):
        for y in range(y1 - 1, y2 + 2):
            if a[x][y] == 1:
                print('BAD')
                sys.exit(0)
            a[x][y] = 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                a[x][y] = 1
print('OK')
