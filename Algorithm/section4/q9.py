# 증가 수열 만들기
# import sys
# from collections import deque
# # sys.stdin = open("in1.txt","r")
# n = int(input())
# queue = list(map(int,input().split()))
#
# queue = deque(queue)
# ord = ""
# start = 0
# cnt = 0
# while True:
#     if len(queue) == 1:
#         ord += 'L'
#         break
#     if queue[0] <= start and queue[-1] <= start:
#         break
#     elif queue[0] < queue[-1]:
#         ord += 'L'
#         start = queue.popleft()
#     else:
#         ord += 'R'
#         start = queue.pop()
#
# print(len(ord))
# print(ord)

# 강사님 코드 : append활용하기
import sys
sys.stdin = open("in1.txt","r")
n = int(input())
t = list(map(int,input().split()))

tmp =[]
start = 0

lt = 0
rt = n-1

ans = ""

while lt <= rt :
    print(lt,rt)
    if t[lt] > start:
        tmp.append((t[lt],'L'))
    if t[rt] > start:
        tmp.append((t[rt],'R'))
    if len(tmp) == 0:
        break

    # 숫자가 작은 순서로 tmp 순서 정렬 되어있음
    tmp.sort()
    print(tmp)
    # 만약에, lt = rt라면 tmp[0][0]이나 tmp[1][0]은 같은 값
    start = tmp[0][0]
    ans += tmp[0][1]
    # 'L'을 쓰는게 중요
    if tmp[0][1] == 'L':
        lt += 1
    else:
        rt -= 1

    tmp.clear()
print(len(ans))
print(ans)


