# Метод двух указателей

# 13.1 Пары фиксированной суммы

# # n, k = map(int, input().split())
# n, k = 4, 5
# a = [1, 3, 4, 2]
# # a = list(map(int, input().split()))
# a.sort()
# j = n - 1
# ans = 0
# for ai in a:
#     while j > 0 and a[j] > k - ai:
#         j -= 1
#     if ai + a[j] == k and ai < a[j]:
#         ans += 1
# print(ans)

# Использование понятных имен переменных улучшает понимание кода.
# nums_count, total = 4, 5
# nums = [1, 3, 4, 2]
# nums.sort()  # [1, 2, 3, 4]
# r_idx = nums_count - 1
# ans = 0
# for num in nums:
#     while r_idx > 0 and nums[r_idx] > total - num:
#         r_idx -= 1
#     if num + nums[r_idx] == total and num < nums[r_idx]:
#         ans += 1
# print(ans)


# 13.2 Длиннейший подотрезок без повторов
# n = int(input())
# a = list(map(int, input().split()))
# n = 10
# a = [1, 3, 4, 2, 1, 5, 4, 4, 4, 2]
# ans = 0
# j = -1
# segment = set()
# for i in range(n):
#     while (j + 1 < n and a[j + 1] not in segment):
#         j += 1
#         segment.add(a[j])
#     ans = max(ans, j - i + 1)
#     segment.remove(a[i])
# print(ans)

# nums_count = 10
# nums = [1, 3, 4, 2, 1, 5, 4, 4, 4, 2]
# ans = 0
# j = -1
# segment = set()
# for num in range(nums_count):
#     while (j + 1 < nums_count and nums[j + 1] not in segment):
#         j += 1
#         segment.add(nums[j])
#     ans = max(ans, j - num + 1)
#     segment.remove(nums[num])
# print(ans)

# 13.3 Подотрезки со всеми числами
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# n = 9
# k = 4
# a = [1, 2, 1, 3, 1, 2, 1, 4, 1]
# cnt = [0] * (k + 1)
# present = 0
# j = -1
# ans = n
# for i in range(n):
#     while j + 1 < n and present < k:
#         j += 1
#         if not cnt[a[j]]:
#             present += 1
#         cnt[a[j]] += 1
#         if present == k:
#             ans = min(ans, j - i + 1)
#         cnt[a[i]] -= 1
#         if not cnt[a[i]]:
#             present -= 1
# print(ans)

