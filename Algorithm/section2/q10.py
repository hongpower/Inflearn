# 점수계산
score = 0
n = int(input())
lst = list(map(int,input().split()))
smalls = 0
for i in range(n):
    if lst[i] == 1:
        smalls = smalls + 1
        score += smalls
    else:
        smalls = 0
print(score)

## 강사님 코드 (완전 같음)
# import sys
# sys.stdin=open("input.txt","r")
# n = int(input())
# a = list(map(int, input().split()))
# sum = 0
# cnt = 0
# for x in a:
#     if x == 1:
#         cnt += 1
#         sum += cnt
#     else:
#         cnt = 0
# print(sum)
