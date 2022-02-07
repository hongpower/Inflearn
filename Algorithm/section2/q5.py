## 정다면체
import sys
n, m = map(int,sys.stdin.readline().split())

totals = []
for i in range(1, n+1):
    for j in range(1, m+1):
        totals.append(i+j)
temp = set(totals)
num = []
percent = []
for n in temp:
    num.append(n)
    percent.append(totals.count(n)/len(totals) * 100)

maxCnt = percent.count(max(percent))
for _ in range(maxCnt):
    idx = percent.index(max(percent))
    print(num[idx], end=" ")
    percent.remove(max(percent))
    num.remove(num[idx])

# ## 강사님 코드
# import sys
# sys.stdin = open("input.txt", "r")
# n, m = map(int,sys.stdin.readline().split())
# cnt=[0]*(n+m+3) ## 0으로 초기화된 list를 넉넉하게 잡아서 n+m+3크기의 list 생성
# max=-2147000000
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         # 인덱스를 활용한다!
#         cnt[i+j]+=1
# for i in range(n+m+1):
#     if cnt[i]>max:
#         max=cnt[i]
# for i in range(n+m+1):
#     if cnt[i]==max:
#         print(i, end=' ')

