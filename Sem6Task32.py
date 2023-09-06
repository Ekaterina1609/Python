arr=[1,2,3,12,13,7,8,9,10]
minimum=int(input("Введите min границу"))
maximum=int(input("Введите max границу"))
res=[]
i=0
while i < len(arr):
    if arr[i]>minimum and arr[i]<maximum:
        res.append(i)
    i+=1
print(res)
