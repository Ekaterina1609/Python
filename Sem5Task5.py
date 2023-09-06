import random
num=random.randint(1,100)
print(num)
check=0
def helper(check):
    print("check = ",check)
    if check==10:
        print("Загаданное число ", num)
        return None
    else:
        a = int(input("Введите число от 0 до 100"))
        if a>num:
            print("Загаданное число меньше")
        elif a<num:
            print("Загаданное число больше")
        else:
            print("Вы отгадали число")
            return None
        return helper(check+1)

helper(0)
