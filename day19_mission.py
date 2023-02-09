# def change2(num):
#
#     rest = num % 2
#     quota = num // 2
#     if quota != 0:
#         array.append(rest)
#         change2(quota)
#     elif quota == 0:
#         array.append(1)
#         return
#     return array
#
#
# if __name__ == '__main__':
#     array = []
#
#     number = int(input("10진수 입력 --> "))
#     print("2진수 : ", end = '')
#     a = change2(number)
#     print("".join(list(map(str,a[::-1]))))
#     # map (func, 리스트) : 리스트 개별 요소에 저 함수를 적용
#     # for i in range(len(change2(number))):
#     #     print(change2(number)[i], end = '')
#
#
#
#     print("\n8진수 : ")
#     print("16진수 : ")

def nota(bs, n):
    if n < bs:
        print(numberch[n], end=' ')
    else:
        nota(bs, n // bs)
        print(numberch[n % bs], end=' ')


numberch = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberch += ['A', 'B', 'C', 'D', 'E', 'F']

number = int(input('10진수 입력 -->'))
print('\n 2진수 : ', end=' ')
nota(2, number)
print('\n 8진수 : ', end=' ')
nota(8, number)
print('\n16진수 : ', end=' ')
nota(16, number)
