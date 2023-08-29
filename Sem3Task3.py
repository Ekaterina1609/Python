quantity = int(input("Введите количество единиц товара"))
commodities=[]
i=0
while i<quantity:
    name=input("Введите название товара")
    price=int(input("Введите цену"))
    qty=int(input("Введите количество"))
    measure=input("Введите единицу измерения")
    commodities.append((i,{"Название":name,"Цена":price,"Количество":qty,"Ед.изм.":measure}))
    i=i+1
print(commodities)

dictionary={}
name_dict=None
price_dict=None
qty_dict=None
measure_dict=None
x=0
for el in commodities:
    
    x+=1
