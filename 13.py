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

nums_count, total = 4, 5
nums = [1, 3, 4, 2]
nums.sort()  # [1, 2, 3, 4]
r_idx = nums_count - 1
ans = 0
for num in nums:
    while r_idx > 0 and nums[r_idx] > total - num:
        r_idx -= 1
    if num + nums[r_idx] == total and num < nums[r_idx]:
        ans += 1
print(ans)
