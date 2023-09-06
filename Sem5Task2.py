
def count_even(number):
    even = 0
    count1 = len(number)
    print(f'Значение в рекурсии {number}')
    if len(number)==1:
            return int(number)%2
    else:
        return int(number)%2+count_even(number[:count1-1])

num=input("Введите число")
count=len(num)
nonev=count_even(num)
ev=len(num)-nonev
print(f'нечетных{nonev}, четных{ev}')
