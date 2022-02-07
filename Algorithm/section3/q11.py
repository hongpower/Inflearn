# 격자판 회문수
# import sys
# sys.stdin = open("in2.txt",'r')
board = [list(map(int,input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(0,3):
        if board[i][j] == board[i][j+4]:
            if board[i][j+1] == board[i][j+3]:
                cnt += 1
        if board[j][i] == board [j+4][i]:
            if board[j+1][i] == board[j+3][i]:
                cnt += 1
print(cnt)

## 강사님 코드 : 비슷함! 방식은 좀 다름, 거꾸로 만들기 사용
board = [list(map(int,input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    # 행 확인
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1

    # 열 확인 (여기 중요!)
        for k in range(2):
            # 중간 빼고 앞 두자리와 뒤 두자리만 비교할 것이기 때문에 2번 반복
            if board[i + k][j] != board[i + 4 - k][j]:
                break
        else:
            cnt += 1
