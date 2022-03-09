# 최대 부분 증가수열
# import sys
# sys.stdin = open('in1.txt', 'r')
n = int(input())
lst = list(map(int, input().split()))

## 중요!
lst.insert(0, 0)


# 각 index의 위치가 array의 마지막이라 가정했을 때 가장 긴 증가수열을 원소로하는 dy
if __name__ == "__main__":
    dy = [0] * (n+1)
    dy[1] = 1
    res = 0
    for i in range(2, n+1):
        max = 0
        for j in range(i-1, 0, -1):
            if lst[i] > lst[j]:
                if dy[j] > max:
                    max = dy[j]
        dy[i] = max + 1
        if dy[i] > res:
            res = dy[i]
    print(res)