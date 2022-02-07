# 숫자만 추출
# nums = ''
# cnt = 0
# lst = list(input())
#
#
# for i in lst:
#     try:
#         nums += str(int(i))
#     except:
#         pass
#
# nums = int(nums)
#
# # 약수의 개수
# for n in range(1,nums+1):
#     if nums % n == 0:
#         cnt += 1
# print(nums)
# print(cnt)

## 강사님 코드
# s = input()
# res = 0
# for letter in s:
#     if letter.isdecimal():
#         res = res*10 + int(letter)
# print(res)
#
# cnt = 0
# for i in range(1,res+1):
#     if res%i == 0:
#         cnt += 1
# print(cnt)