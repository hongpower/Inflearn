# 대표값
import sys
n = sys.stdin.readline()
math_score = list(map(int,sys.stdin.readline().split()))
closestlst = [0, 100]
avg = 0
total = 0
for score in math_score:
    total += score
avg = round(total / len(math_score))
for i in range(len(math_score)):
    num = i+1
    if abs(math_score[i]-avg) < abs(closestlst[1]):
        closestlst[0] = num
        closestlst[1] = math_score[i]-avg
    elif abs(math_score[i]-avg) == abs(closestlst[1]):
        if math_score[i]-avg > closestlst[1]:
            closestlst[0] = num
            closestlst[1] = math_score[i]-avg

print(avg, end=" ")
print(closestlst[0])

# # 강사님 코드
# import sys
# n = sys.stdin.readline()
# a = list(map(int,sys.stdin.readline().split()))
# ave = round(sum(a)/n) ## 소수 첫째자리에서 반올림, 평균이렇게 쉽게 구함...
# min = 2147000000 ## 정수형 가장 큰 값
# for idx, x in enumerate(a):
#     tmp = abs(x-ave)
#     if tmp<min:
#         min=tmp
#         score=x ##여기는 원래 점수
#         res=idx+1 # 여기는 학생번호
#     elif tmp==min:
#         if x>score:
#             score=x
#             res=idx+1
# print(ave, res)