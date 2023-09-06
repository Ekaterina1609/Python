a=int(input("Введите любое число a "))
b=int(input("Введите любое число b "))

def sum_of_nums(a,b):
    if(a==1):
        return 1
    else:
        return 1+sum_of_nums(a-1)