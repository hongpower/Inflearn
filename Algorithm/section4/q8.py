# 침몰하는 타이타닉
# import sys

# sys.stdin = open("in1.txt","r")

# 타이타닉의 구명보트는 2명이하만 가능. 그래서 1명인지 2명인지 계속 확인
#n은 lst의 길이, m은 구명보트 최대 수용 몸무게
# n, m = map(int,input().split())
# lst = list(map(int,input().split()))
#
# # 구명 보트의 최소 개수는?
# cnt = 0
#
# # 젤 큰애랑 마지막애랑 비교해서 탈 수 있다면 얘 빼
# lst.sort()
# while len(lst) > 1:
#     if lst[0] + lst[-1] <= m:
#         cnt += 1
#         lst.pop()
#         lst.pop(0)
#     else:
#         cnt += 1
#         lst.pop()
# cnt += len(lst)
# print(cnt)

# 강사님 코드
from collections import deque

n, m = map(int,input().split())
p = list(map(int,input().split()))
p.sort()
p = deque(p) #리스트 맨 앞을 지정
print(p)
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > m:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt += 1
print(cnt)