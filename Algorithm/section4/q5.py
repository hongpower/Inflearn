# 회의실 배정(그리디)
# import sys
# sys.stdin = open("in2.txt", "r")
n = int(input())
schd = []
for _ in range(n):
    s, e = map(int,input().split())
    schd.append((s, e))
# 여기서 x는 schd안에 들어있는 한 요소(set)이고 이거를 lambda식에 전달하고 lambda는 여기의 1번째 인덱스 값과 0번째 인덱스값을 반환
# 끝나는 시간 기준으로 정렬
schd.sort(key=lambda x : (x[1],x[0]))
cnt = 0
et = 0
for i in schd:
    s, e = i[0], i[1]
    if s >= et:
        cnt += 1
        et = e
print(cnt)