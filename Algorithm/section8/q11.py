# 최대점수 구하기(냅색 알고리즘)
# import sys
# sys.stdin = open("in3.txt", "r")

n, m = map(int, input().split())
dy = [0] * (m + 1)
for _ in range(n):
    score, time = map(int, input().split())
    for i in range(m, time-1, -1):
        dy[i] = max(dy[i], dy[i-time] + score)

# print(dy)
print(max(dy))