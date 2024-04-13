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

# 12.3 Объединение отрезков
def merge_segm(segms):
    res = []
    for left, right in sorted(segms):
        if res and left <= res[-1][1]:
            res[-1][1] = max(res[-1][1], right)
        else:
            res.append([left, right])
    return res

