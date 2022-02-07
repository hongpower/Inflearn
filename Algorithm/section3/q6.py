# 격자판 최대합
outerlst = []
n = int(input())
for _ in range(n):
    outerlst.append(list(map(int, input().split())))

maxSum = 0

# 행의 합
for i in range(n):
    if sum(outerlst[i]) > maxSum:
        maxSum = sum(outerlst[i])

# 열의 합
for i in range(n):
    total = 0
    for j in range(n):
        total += outerlst[j][i]
    if total > maxSum:
        maxSum = total

# 대각선 합
total = [0,0]
for i in range(n):
    total[0] += outerlst[i][i]
    total[1] += outerlst[i][n-i-1]

if max(total) > maxSum:
    maxSum = max(total)

print(maxSum)

# 강사님 코드
a=[list(map(int, input().split())) for _ in range(n)]
# 위에 거랑 행과 열 합쳐서 하신 거 빼고는 같음
