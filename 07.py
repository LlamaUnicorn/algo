# 7.1 Морской бой
# import sys
# FIELD = 102
# a = [[0] * FIELD] * FIELD
# n = int(input())
# for _ in range(n):
#     x1, y1, x2, y2 = map(int, input().split())
#     if x1 > x2:
#         x1, x2 = x2, x1
#     if y1 > y2:
#         y1, y2 = y2, y1
#     for x in range(x1 - 1, x2 + 2):
#         for y in range(y1 - 1, y2 + 2):
#             if a[x][y] == 1:
#                 print('BAD')
#                 sys.exit(0)
#             a[x][y] = 2
#         for x in range(x1, x2 + 1):
#             for y in range(y1, y2 + 1):
#                 a[x][y] = 1
# print('OK')


# 7.2 Стоимость интернет-связи
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

n = int(input())
# n = 3
tariff = [None] * (n + 1)
for i in range(n):
    day, hour, price = input().split()
    day = DAYS.index(day)
    hour = int(hour)
    price = int(price)
    tariff[i + 1] = (day, hour, price)
tariff[0] = (0, 0, tariff[-1][2])

k = int(input())
cost = 0
for i in range(k):
    day, hour, mb = input().split()
    day = DAYS.index(day)
    hour = int(hour)
    mb = int(mb)
    for j in range (n + 1):
        if tariff[j][0] > day:
            break
        if tariff[j][0] == day and tariff[j][1] > hour:
            break
    cost += mb * tariff[j - 1][2]
print(cost)

