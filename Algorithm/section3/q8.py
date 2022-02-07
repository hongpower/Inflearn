# 곳감
import copy
import sys
sys.stdin = open("in2.txt","r")

# outerlst = []
# n = int(input())
# for _ in range(n):
#     outerlst.append(list(map(int, input().split())))
# newlst = copy.deepcopy(outerlst)
#
# m = int(input())
# for _ in range(m):
#     a, b, c = map(int,input().split())
#     a -= 1
#     for i in range(n):
#         # 왼쪽으로
#         if b == 0:
#             newlst[a][(i-c)%n] = outerlst[a][i]
#         # 오른쪽으로
#         else:
#             newlst[a][(i+c)%n] = outerlst[a][i]
# middle = n//2
# total = newlst[middle][middle]
# left = 0
# right = n
# for i in range(0,middle):
#     total += sum(newlst[i][left:right])
#     total += sum(newlst[-i-1][left:right])
#     left += 1
#     right -= 1
# print(total)

# 강사님 코드 참고 내가 작성
n = int(input())
grd = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    row, pos, step = map(int, input().split())
    if pos == 0:
        for _ in range(step):
            grd[row-1].append(grd[row-1].pop(0))
    else:
        for _ in range(step):
            grd[row-1].insert(0,grd[row-1].pop())

s = 0
e = n
total = 0
for i in range(n):
    for j in range(s,e):
        total += grd[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(total)
