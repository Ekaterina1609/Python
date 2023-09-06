# check=0
# while check==0:
#     oper = input("Введите операцию +,-,/,* или 0 для выхода")
#     if oper=='+':
#         print("+")
#     elif oper=='-':
#          print("-")
#     elif oper=='/':
#          print("/")
#     elif oper=='*':
#         print("*")
#     elif oper=='0':
#         print("остановка")
#         check=1
#     else:
#         print("Некорректный ввод операции")
#         check=1


def funct():
    oper = input("Введите операцию +,-,/,* или 0 для выхода")
    if oper == '0':
        print('Выход')
        return 1
    a = int(input("введите число a"))
    b = int(input("введите число b"))

    if oper == '+':
        res=a+b
    elif oper=='-':
         res=a-b
    elif oper=='/':
        res=a/b
    elif oper=='*':
        res=a*b
    else:
        print("Ошибка ввода")

    print(f'{a} {oper} {b} = {res}')
    return funct()

a=funct()
