# 뮤직비디오
# def Count(capacity):
#     cnt = 1
#     sum = 0
#     for x in lst:
#         if sum+x> capacity:
#             cnt += 1
#             sum = x
#         else:
#             sum += x
#     return cnt
# n, m = map(int,input().split())
# lst = list(map(int,input().split()))
# maxx=max(lst)
#
# # 용량은 쭐일수록 좋고, mid는 한 dvd당 용량을 찾기위한 작업이다
# lt = 1
# rt = sum(lst)
# res = 0
# while lt <= rt:
#     mid = (lt + rt)//2
#     if mid>=maxx and Count(mid)<=m:
#         res = mid
#         rt = mid-1
#     else:
#         # dvd가 count개 필요하고 이게 내가 만들고 싶은 개수보다 많으니 한 dvd당 용량을 늘려야겠지?
#         lt = mid + 1
# print(res)
def countAl(x):
    total = 0
    cnt = 1
    for i in lst:
        if total+i <= x:
            total += i
        else:
            cnt += 1
            total = i
    return cnt

n, m = map(int,input().split())
lst = list(map(int,input().split()))

lt = 1
rt = sum(lst)
res = 0
minStor = max(lst)
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= minStor & countAl(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
