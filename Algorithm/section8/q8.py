# 알리바바와 20인의 도둑(bottom-top)
import sys
sys.stdin = open('in1.txt', 'r')
# n = int(input())
# ary = list(list(map(int, input().split())) for _ in range(n))
# dy = [list(0 for _ in range(n)) for _ in range(n)]
#
# dy[0][0] = ary[0][0]
#
# for i in range(1, n):
#     dy[0][i] = dy[0][i-1] + ary[0][i]
#     dy[i][0] = dy[i-1][0] + ary[i][0]
#
# for i in range(1, n):
#     for j in range(1, n):
#         dy[i][j] = min(dy[i][j-1], dy[i-1][j]) + ary[i][j]
#
# print(dy[n-1][n-1])

# 알리바바와 40인의 도둑(top-down)
def DFS(row, col):
    if dy[row][col] > 0:
        return dy[row][col]
    if row == 0 and col == 0:
        return ary[0][0]
    else:
        if row == 0:
            dy[row][col] = DFS(row, col-1) + ary[row][col]
        elif col == 0:
            dy[row][col] = DFS(row-1, col) + ary[row][col]
        else:
            dy[row][col] = min(DFS(row, col-1), DFS(row-1, col)) + ary[row][col]
        return dy[row][col]

n = int(input())
ary = list(list(map(int, input().split())) for _ in range(n))
dy = [list(0 for _ in range(n)) for _ in range(n)]

val = DFS(n-1, n-1)
print(val)
