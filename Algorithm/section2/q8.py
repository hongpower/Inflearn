# 뒤집은 소수
def reverse(x):
    lst = [i for i in str(x)]
    lst.reverse()
    str1 = ""
    for i in lst:
        str1 += i
    return int(str1)

def isPrime(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

n = int(input())
lst = list(map(int, input().split()))
prime = []
for ele in lst:
    x = reverse(ele)
    if (isPrime(x)):
        prime.append(x)

for i in prime:
    print(i, end=" ")

## 강사님 코드 (많이 다름 나와) 특히 reverse(x)참고 !
# def reverse(x):
#     res = 0
#     # x가 소수점이 아닐 때까지 반복
#     while x > 0:
#         # 1의 자리수부터 res에 입력
#         t = x%10
#         # 기존 res를 10배를 하고 나머지를 더한다
#         res += res*10 + t
#         # 이미 더한 자리수는 없앤다
#         x//10
#     return res
#
# def isPrime(x):
#     if x == 1:
#         return False
#     # x라는 숫자 절반 이후부터는 어짜피 다 2의 배수기 때문에 뺐고 range특성상 끝에는 +1을 해줘야한다
#     for i in range(2,x//2+1):
#         if x%i == 0:
#             return False
#     return True
#
# n = int(input())
# a = list(map(int, input().split()))
# for x in a:
#     temp = reverse(x)
#     if isPrime(temp):
#         print(temp, end=" ")
