# 가장 높은 탑 쌓기
import sys

sys.stdin = open('in1.txt', 'r')
n = int(input())
ary = list()
for _ in range(n):
    a, b, c = map(int,input().split())
    ary.append((a, b, c))

ary.sort(reverse=True)
print(ary)

# 본격 시작
dy = [0] * n
dy[0] = ary[0][1]
res = ary[0][1]
for i in range(1, n):
    max = 0
    for j in range(i-1, -1, -1):
        if ary[j][2] > ary[i][2] and dy[j] > max:
            max = dy[j]

    dy[i] = max + ary[i][1]
    res = max(res, dy[i])
print(res)