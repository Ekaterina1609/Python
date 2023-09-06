a=int(input("Введите любое число"))
def sum (num):
    if num==1:
        return 1
    else:
        return num+sum(num-1)

sum_num=sum(a)
print(sum_num)

x=a*(a+1)/2
if sum_num == x:
    print("Значения совпадают и равны ",sum_num)
else:
    print("Не совпадают")