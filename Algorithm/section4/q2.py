# 랜선자르기
# import sys
# sys.stdin = open("in1.txt",'r')
k, n = map(int,input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))

res = 0
lt = 1 ## 왜 1부터냐면 lst index가 아니라 값이 중요한거기 때문에
rt = max(lst)
while lt <= rt:
    mid = (lt + rt)//2
    cnt = 0
    for i in lst:
        cnt += (i//mid)
    if cnt >= n:
        res = mid # 이게 최대값이라서 더 못찾더라도 최소 이정도는 만들 수 있어!
        lt = mid+1
    else:
        rt = mid-1
print(res)