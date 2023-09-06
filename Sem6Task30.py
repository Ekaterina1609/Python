start=int(input("Введите первый член прогрессии"))
step=int(input("Введите шаг прогрессии"))
quantity=int(input("Введите количество членов прогрессии"))
arr=[]
temp=0
for el in range(quantity):
    temp=start+(el)*step
    arr.append(temp)

print(arr)