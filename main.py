# num =int(input("введите число"))
# print(num**2)


#name = input("Введите имя: ")
#age = int(input("Введите возраст:"))
#print(f"Привет! {name}. Тебе {age} лет")
#pas = 123
#pas_check=input('Введите пароль')
#if pas_check==pas:
#    print("Правильный пароль")
#else:
#    print("Неправильный пароль")

time = int(input("Введите время в сек: "))
hour = (time//3600)
print(hour)
minutes = (time-hour*3600)//60
print(minutes)
sec=time-hour*3600-minutes*60

print(f"{hour} часов {minutes} минут {sec} секунд")