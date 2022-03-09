# 탑다운은 값을 저장할 테이블이 따로 필요 (메모이제이션 : 불필요한 재귀 호출하지 않는다)
# 바텀업은 동적 계획법 X, 넓은 의미만


# def DFS(len):
#     if len == 1 or len == 2:
#         return len
#     else:
#         dy[len] = DFS(len-1) + DFS(len-2)
#         return dy[len]
#
# if __name__ == "__main__":
#     n = int(input())
#     dy = [0]*(n+1)
#     print(DFS(n))

# ===== 이정도만 쓰면 가지치기를 못해서 불필요한 재귀가 일어나서 시간이 오래걸림 ======

## 수정본!
def DFS(len):
    if dy[len] != 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))