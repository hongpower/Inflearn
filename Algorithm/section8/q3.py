## 계단 오르기
# 바텀업
# n = int(input())
# dy = [0] * (n + 1)
#
# dy[1] = 1
# dy[2] = 2
#
# for i in range(3, n+1):
#     dy[i] = dy[i-2] + dy[i-1]
#
# print(dy[n])

# 탑다운
def DFS(len):
    if dy[len] != 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


n = int(input())
dy = [0] * (n+1)
print(DFS(n))