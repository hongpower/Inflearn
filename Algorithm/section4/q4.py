# 마구간 정하기
import sys
# 말의 개수 새기:
def Count(x):
    cnt = 1
    dis = lst[0]
    for i in range(1,n):
        # 만약에 이미 임의로 설정한 최소 거리차이를 넘었다면:
        if lst[i]-dis >= x:
            # 삽입한 말의 개수를 올리고
            cnt += 1
            # 다시 시작한다
            dis = lst[i]
        # 만약 최소 거리차이를 넘지 못했다면, 말을 배치한 처음 위치에서 다음 위치의 차이를 빼야하는 거니 변화를 주지 않는다
    return cnt


n, c = map(int,input().split())
lst = []
for i in range(n):
    lst.append(int(input()))

# 정렬 먼저
lst.sort()

# 말의 최대 거리 가상 설정
lt = 1
rt = max(lst)
res = 0
while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c : # 말의 개수
        res = mid
        lt = mid +1
    else:
        rt = mid - 1
print(res)

