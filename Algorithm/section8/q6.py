# 최대 선 연결하기
# import sys
#
# sys.stdin = open('in1.txt', 'r')
n = int(input())
ary = list(map(int,input().split()))
ary.insert(0,0)

dy = [0] * (n+1)
dy[1] = 1
res = 0

# ary : 입력값,
for i in range(2,n+1):
    max = 0
    # 숫자의 위치 찾기
    loc = ary.index(i)
    for j in range(loc-1, 0, -1):
        if dy[ary[j]] > max:
            max = dy[ary[j]]

    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)
