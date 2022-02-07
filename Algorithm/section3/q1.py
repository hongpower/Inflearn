# 회문 문자열 검사
import copy

n = int(input())

for nth in range(n):
    ans = 'YES'
    word = list(input().lower())
    wordR = copy.deepcopy(word)
    wordR.reverse()
    for i in range(len(word)):
        if word[i] == wordR[i]:
            pass
        else:
            ans = 'NO'
            break
    print(f'#{int(nth+1)} {ans}')

# 강사님 코드 1 (이 방법 추천)
# n = int(input())
# for nth in range(n):
#     word = input().upper()
#     for i in range(n//2):
#         if word[i] != word[-i-1]:
#             print('#%d NO' %(nth+1))
#             break
#     else:
#         print('#%d YES' %(nth+1))

# # 강사님 코드 2
# n = int(input())
# for nth in range(n):
#     word = input().upper()
#     if word == word[::-1]: # => word를 거꾸로한다. (-1 인덱스부터 읽으니까)
#         print('#%d NO' %(nth+1))
#     else:
#         print('#%d YES' %(nth+1))