## 자릿수의 합

def digit_sum(x):
    # 각 자연수의 자릿수 합 구하기
    total = 0
    for i in range(len(x)):
        total += int(x[i])
    return total

maxN = 0
max = 0
n = int(input())
numlst = list(input().split())
for i in range(n):
    num = numlst[i]
    total = digit_sum(num)
    if total > max:
        max = total
        maxN = num
print(maxN)

## 강사님 코드
# import sys
# sys.stdin=open("input.txt","r")
# n=int(input())
# a=list(map(int, input().split()))
# def digit_sum(x):
#     sum = 0
#     while x>0:
#         sum+=x%10
#         x=x//10
#     return sum
#
# max = -2147000000
# for x in a:
#     tot=digit_sum(x)
#     if tot>max:
#         max=tot
#         res=x
# print(res)