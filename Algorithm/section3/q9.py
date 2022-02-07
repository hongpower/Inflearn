# 봉우리
# import sys
# sys.stdin = open("in2.txt",'r')

# n = int(input())
# lst = [[0 for _ in range(n+2)] for _ in range(n+2)]
# lst2 = [list(map(int,input().split())) for _ in range(n)]
# cnt = 0
#
# for i in range(n):
#     for j in range(n):
#         lst[i+1][j+1] = lst2[i][j]
#
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         me = lst[i][j]
#         up = lst[i-1][j]
#         down = lst[i+1][j]
#         left = lst[i][j-1]
#         right = lst[i][j+1]
#         everyone = [me, up, down, left, right]
#         if (max(everyone) == me) & (everyone.count(me) == 1):
#             cnt += 1
# print(cnt)

## 강사님 코드 : 틀은 비슷
# 0이 모서리로 둘러싸진 2차원 리스트 만들기.
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
# 중요!
dx = [-1,0,+1,0]
dy = [0,-1,0,+1]
cnt = 0

# 0으로 둘러싸진 이차원 배열 만들기
lst.append([0]*n)
lst.insert(0, [0]*n)
for i in lst:
    i.append(0)
    i.insert(0, 0)

# 봉우리 찾기
for i in range(1, n+1):
    for j in range(1, n+1):
        #### 진짜진짜진짜 중요
        if all(lst[i][j]>lst[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)