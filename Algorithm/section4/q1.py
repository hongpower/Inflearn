# 이분검색
# import sys
# sys.stdin = open("in1.txt", "r")
n, m = map(int,input().split())
lst = list(map(int,input().split()))

# 정렬
# for i in range(n-1):
#     minIndex = i
#     minN = lst[minIndex]
#     for j in range(i,n):
#         if minN > lst[j]:
#             minN = lst[j]
#             minIndex = j
#     lst[i], lst[minIndex] = lst[minIndex], lst[i]
lst.sort()
start = 0
end = n-1

while start <= end:
    middle = (end + start) // 2
    if m == lst[middle]:
        print(middle+1)
        break
    elif m > lst[middle]:
        start = middle+1
    else:
        end = middle-1
