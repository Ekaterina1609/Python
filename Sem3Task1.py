month=int(input("Введите номер месяца"))
cal=["Зима","Зима","Весна","Весна","Весна","Лето","Лето","Лето","Осень","Осень","Осень","Зима"]
my_dic = {1:'Зима', 2:'Зима',3:'Весна',4:'Весна',5:'Весна', 6:'Лето',7:'Лето',8:'Лето',9:'Осень',10:'Осень',11:'Осень',12:'Зима'}
print(cal[month-1])
print(my_dic.get(month))
