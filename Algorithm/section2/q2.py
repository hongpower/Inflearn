# k번째 수
import sys
t = int(sys.stdin.readline())
cnt = 0

for _ in range(t):
    n,s,e,k = map(int,sys.stdin.readline().split())
    nlst = list(map(int,sys.stdin.readline().split()))
    temp = nlst[s-1:e]
    temp.sort()
    for i in range(s-1,e):
        nlst[i] = temp[0]
        del(temp[0])
    cnt += 1
    print(f'#{cnt} {nlst[s-1 + k-1]}')

# 강사님 정답
# import sys
# t = int(input())
# for _ in range(t):
#     n, s, e, k = map(int, input().split())
#     a = list(map(int, input().split()))
#     a = a[s-1:e]
#     a.sort()
#     print("#%d %d" %(t+1, a[k-1]))