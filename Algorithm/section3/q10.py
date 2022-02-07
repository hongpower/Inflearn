# # 스토쿠 검사
# # import sys
# # sys.stdin = open("in2.txt", 'r')
# lst = [list(map(int,input().split())) for _ in range(9)]
# lt = 0
# rt = 3
# ans = 'YES'
# while rt < 10:
#     first = lst[lt:rt][0]
#     second = lst[lt:rt][1]
#     third = lst[lt:rt][2]
#     oneset = []
#     for i in range(lt,rt):
#         oneset.append(first[i])
#         oneset.append(second[i])
#         oneset.append(third[i])
#
#     if len(set(oneset)) != 9:
#         ans = 'NO'
#         break
#
#     lt += 3
#     rt += 3
#
# print(ans)
#
# ## 강사님 코드 : 중요!
def check(x):
    # check1은 행 확인
    # check2는 열 확인
    for i in range(9):
        check1 = [0] * 10
        check2 = [0] * 10
        for j in range(9):
            check1[x[i][j]] = 1
            check2[x[j][i]] = 1
        if sum(check1) != 9 or sum(check2) != 9:
            return False
    # check3는 한 박스 확인
    ## 여긴 더 중요!!
    # 하나의 박스 생성
    for i in range(3):
        for j in range(3):
            #박스 내 요소들 카운트
            check3 = [0] * 10
            for r in range(3):
                for c in range(3):
                    check3[x[i*3 + r][j*3 +c]] = 1
            if sum(check3) != 9:
                return False
    return True

lst = [list(map(int,input().split())) for _ in range(9)]
if check(lst):
    print('YES')
else
    print('NO')