# 두 리스트 합치기
# n = int(input())
# lst = list(map(int,input().split()))
# m = int(input())
# lst_m = list(map(int,input().split()))
# for i in lst_m:
#     lst.append(i)
# lst.sort()
#
# for n in lst:
#     print(n, end=" ")

## 강사님코드 (sort사용 지양)
# 강사님 설명 보고 내가 짠 내용:
# n = int(input())
# lst1 = list(map(int,input().split()))
# m = int(input())
# lst2 = list(map(int,input().split()))
#
# newlst = []
# startn = 0
# startm = 0
# while True:
#     if startn == n:
#         for j in lst2[startm:]:
#             newlst.append(j)
#         break
#     elif startm == m:
#         for j in lst1[startn:]:
#             newlst.append(j)
#         break
#     if lst1[startn] < lst2[startm]:
#         newlst.append(lst1[startn])
#         startn += 1
#     elif lst1[startn] > lst2[startm]:
#         newlst.append(lst2[startm])
#         startm += 1
#     else:
#         newlst.append(lst1[startn])
#         newlst.append(lst2[startm])
#         startn += 1
#         startm += 1
#
# for i in newlst:
#     print(i, end=" ")
#
#
# # 강사님 코드: 참고 많이 하자!
n = int(input())
lst1 = list(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))

newlst = []
p1 = 0
p2 = 0

# while문 쓰는 방식이랑, 어짜피 같을 때는 넣는 순서 관계없다는 점 파악하고 시작하기!
while p1 < n and p2 < m:
    if lst1[p1] <= lst2[p2]:
        newlst.append(lst1[p1])
        p1 += 1
    else:
        newlst.append(lst2[p2])
        p2 += 1


## 여기도 중요!
if p1 < n:
    newlst += newlst + lst1[p1:]
else:
    newlst += newlst + lst2[p2:]


for j in newlst:
    print(j, end=" ")
