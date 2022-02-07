# 창고 정리
# import sys
# sys.stdin = open("in1.txt","r")
# 가로길이
l =int(input())
lst = list(map(int,input().split()))
# 높이 지정 횟수
m = int(input())

for _ in range(m):
    lst.sort(reverse=True)
    lst[0] -= 1
    lst[-1] += 1

lst.sort(reverse=True)
print(lst[0] - lst[-1])