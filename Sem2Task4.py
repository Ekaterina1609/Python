arr = input("Введите целые числа через пробел")
arr_mod = arr.split(" ")
i=0
while i<len(arr_mod)-1:
    temp= arr_mod[i]
    arr_mod[i]=arr_mod[i+1]
    arr_mod[i + 1]=temp
    i+=2

print(arr_mod)