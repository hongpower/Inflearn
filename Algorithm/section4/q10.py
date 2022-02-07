# 역수열
# import sys
# sys.stdin = open("in1.txt",'r')
n = int(input())
ary = list(map(int,input().split()))

chk = [0 for _ in range(n)]

# 총길이는 8이니까 8개의 공간만들기
# ary의 첫번째 문자를 가져와서 0의 개수를 세고 개수가 ary가 될 때까지 반복하고, 개수가 ary의 첫번째문자가 되면 내가 찾은 값 집어넣기
for num in range(1,n+1):
    cnt = 0
    pos = ary[num-1]
    for i in range(n):
        ele = chk[i]
        if ele == 0:
            cnt += 1
        if cnt == pos + 1:
            chk[i] = num
            break

for i in chk:
    print(i, end=" ")