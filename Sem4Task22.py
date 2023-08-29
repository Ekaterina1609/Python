mm=int(input("Введите количество элементов 1го массива"))
m=[]
i=0
while i<mm:
    m.append(int(input("Введите элемент 1го массива")))
    i+=1

nn=int(input("Введите количество элементов 2го массива"))
n=[]
j=0
while j<nn:
    n.append(int(input("Введите элемент 1го массива")))
    j+=1
#m=[1,3,5,3,2]
#n=[2,6,5,2]
res=m+n
print(res)
q=set(res)
print(q)