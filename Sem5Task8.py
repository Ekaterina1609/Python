a=int(input("Введите любое число a "))
b=int(input("Введите любое число b "))

def pow (a,b):
    if b==1:
        return a
    else:
        return a*pow(a,b-1)
print(pow(a,b))