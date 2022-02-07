# 소수(에라토스테네스 체)
import sys
cnt = 0
n = int(sys.stdin.readline())
lst = [0 for _ in range(n + 1)]
for i in range(2, n+1):
    if lst[i] == 0:
        cnt += 1
        for j in range(i,n+1,i):
            lst[j] = 1
print(cnt)

## 강사님 코드
# import sys
# sys.stdin=open("input.txt","r")
# n=int(input())
# ch=[0]*(n+1)
## 이상 같음!
