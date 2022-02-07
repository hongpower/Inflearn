# 사과나무(다이아몬드)
# import sys
# sys.stdin = open("in2.txt", 'r')
# outerlst = []
# n = int(input())
# for _ in range(n):
#     outerlst.append(list(map(int, input().split())))
#
# total = 0
# total += sum(outerlst[n//2]) # 22 88 8 3 62 75 46 4 41
# print(total)
#
# left = n//2 #4
# right = n//2
# for i in range(n//2): #0, 1,2,3
#     print(i)
#     print(outerlst[i][left:right+1])
#     total += sum(outerlst[i][left:right+1])
#     print(outerlst[-(i+1)][left:right+1])
#     total += sum(outerlst[-(i+1)][left:right+1])
#     left -= 1
#     right += 1
#
# print(total)

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
c = s = n//2
total = 0

for i in range(n):
    for j in range(c,s+1):
        total += lst[i][j]
    if i < n//2:
        c -=1
        s +=1
    else:
        c +=1
        s -= 1
print(total)