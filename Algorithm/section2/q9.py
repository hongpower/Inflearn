# 주사위 게임 => 나는 set 사용!
n = int(input())
winner = -1
for i in range(n):
    money = 0
    lst = list(map(int,input().split())) # int안할거면 map함수없이 그냥 input().split()만 해도 리스트로 출력
    setLst = set(lst)
    if len(setLst) == 1:
        money += (10000 + (lst[0]*1000))
    elif len(setLst) == 2:
        sameN = 0
        for num in setLst:
            if lst.count(num) == 2:
                sameN = num
        money += (1000 + (sameN * 100))
    else:
        money += (max(lst) * 100)

    if money > winner:
        winner = money
print(winner)

# 강사님 코드 ( 좀 많이 다름 )
# import sys
# sys.stdin=open("input.txt","rt")
# n=int(input())
# res=0
# for i in range(n):
#     tmp = input().split()
#     tmp.sort()
#     a, b, c=map(int,tmp)
#     if a==b and b==c:
#         money=10000+a*1000
#     elif a==b or a==c:
#         money = 1000+(a*100)
#     elif b==c:
#         money = 1000 + (b * 100)
#     else:
#         money=c*100 # 이미 정렬되어있으니까!
#     if money>res:
#         res=money
# print(res)