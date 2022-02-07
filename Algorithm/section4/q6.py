# 씨름 선수
# import sys
# sys.stdin = open("in1.txt",'r')
n = int(input())
lst = []
winners = []

for _ in range(n):
    height, weight = map(int,input().split())
    lst.append((height, weight))

maxW = 0
cnt = 0
# key없이 정렬을 하면 첫번째 인자를 기준으로 정렬
lst.sort(reverse=True)
for height, weight in lst:
    if weight > maxW:
        maxW = weight
        cnt += 1
print(cnt)