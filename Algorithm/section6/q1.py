# 재귀함수를 이용한 이진수 출력

def DFS(x):
    if x == 0:
        return
    DFS(x//2)
    print(x%2,end="")


if __name__== "__main__":
    x = int(input())
    DFS(x)