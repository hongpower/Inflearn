# 동전교환
# import sys
# sys.stdin = open('in1.txt', 'r')

## 내꺼 :
# n = int(input())
# coins = list(map(int, input().split()))
# tot = int(input())
#
# dy = [0] * (tot + 1)
#
# for i in range(n):
#     p = coins[i]
#     for j in range(p, tot + 1):
#         if dy[j] == 0:
#             if j%p == 0:
#                 dy[j] = j/p
#         else:
#             if j%p == 0:
#                 dy[j] = min(j/p, dy[j])
#             else:
#                 temp = j%p
#                 dy[j] = min(dy[temp] + j//p, dy[j])
#
# dy = list(map(int, dy))
# # print(dy)
# print(dy[tot])

## 강사님꺼 :
n = int(input())
coins = list(map(int, input().split()))
tot = int(input())

# 최소값을 찾을 예정이기 때문에 큰 값으로 처음에는 초기화 :
dy = [1000] * (tot + 1)
dy[0] = 0
for i in range(n):
    p = coins[i]
    for j in range(p, tot + 1):
        dy[j] = min(dy[j], dy[j-p] + 1)

# print(dy)
print(dy[tot])