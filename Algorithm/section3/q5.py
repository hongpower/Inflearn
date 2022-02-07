# 수들의 합 (런타임 에러 ...ㅋㅋ)
# import sys
# n, m = map(int,sys.stdin.readline().split())
# lst = list(map(int,sys.stdin.readline().split()))
# cnt = 0
# for i in range(n):
#     if lst[i] == m:
#         cnt += 1
#     elif lst[i] < m:
#         for j in range(i+2, n+1):
#             ans = sum(lst[i:j])
#             if ans > m:
#                 break
#             elif ans == m:
#                 cnt += 1
#                 break
# print(cnt)

# 강사님 코드 중요중요!
# import sys
# sys.stdin = open("input.txt","r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
# 이거 tot를 a[0]으로 지정한게 신의 한수
tot = a[0]
cnt = 0
while True:
    if tot < m :
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)

