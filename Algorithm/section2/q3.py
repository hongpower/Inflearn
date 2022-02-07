# k번째 큰 수
import sys

n, k = map(int,sys.stdin.readline().split())
val = list(map(int,sys.stdin.readline().split()))
sumlst = []
for first in range(len(val)):
    for second in range(first+1,len(val),1):
        for third in range(second+1,len(val),1):
            sumlst.append(val[first] + val[second] + val[third])

sumlst = list(set(sumlst))
sumlst.sort(reverse=True)
print(sumlst[k-1])

# 강사님 코드 :
# import sys
# sys.stdin=open("input.txt","rt")
# n, k = map(int,sys.stdin.readline().split())
# a = list(map(int,sys.stdin.readline().split()))
# res = set()
# for i in range(n):
#     for j in range(i+1,n):
#         for m in range(j+1,n):
#             ## set은 append 쓰기
#             res.add(a[i]+a[j]+a[m])
# res = list(res)
# res.sort(reverse=True)
# print(res[k-1])