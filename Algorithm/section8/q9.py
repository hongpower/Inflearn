# 가방문제(냅색 알고리즘)
# import sys
# sys.stdin = open('in1.txt', 'r')
if __name__ == "__main__":
    n, tot = map(int, input().split())
    dy = [0] * (tot+1)

    for _ in range(n):
        w, val = map(int, input().split())
        for j in range(w, tot+1):
            if dy[j-w] + val > dy[j]:
                dy[j] = dy[j - w] + val
    print(dy[tot])