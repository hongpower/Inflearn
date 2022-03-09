# 네트워크 선 자르기(Bottom-up)

# import sys
# sys.stdin = open("input.txt", "r")
n=int(input())
dy = [0] * (n+1)

# 직관적으로 알 수 있는 부분 :
dy[1] = 1
dy[2] = 2
for i in range(3, n+1):
    dy[i] = dy[i-2] + dy[i-1]

print(dy[n])