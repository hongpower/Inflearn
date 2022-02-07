# 카드 역배치
import sys
# lst = [i for i in range(1,21)]
# for _ in range(10):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     diff = b - a
#     for _ in range(diff//2+1):
#         lst[a], lst[b] = lst[b], lst[a]
#         a += 1
#         b -= 1
#
# for n in lst:
#     print(n, end=" ")

## 강사님 코드 : swap사용 (비슷하지만 조금 다르다)
# sys.stdin = open("in2.txt","r")
# a = list(range(21)) # 0도 포함시킴
# for _ in range(10):
#     b, c = map(int, input().split())
#     for i in range((c-b+1)//2):
#         a[b+i], a[c-i] = a[c-i], a[b+i]
# a.pop(0)
# for x in a:
#     print(x, end=" ")