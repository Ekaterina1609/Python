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

# time = int(input("Введите время в сек: "))
# hour = (time//3600)
# print(hour)
# minutes = (time-hour*3600)//60
# print(minutes)
# sec=time-hour*3600-minutes*60
#
# print(f"{hour} часов {minutes} минут {sec} секунд")

# Задача 4
# sales = int(input("Введите сумму выручки"))
# costs = int(input("Введите сумму затрат"))
# profit_loss = sales-costs
# if profit_loss > 0:
#     print(f"Прибыль составила {profit_loss}")
# else:
#     print(f"Убыток составил {profit_loss}")
# personal=int(input("Укажите количество сотрудников "))
# print(f"Прибыль/убыток на 1 сотрудника составил ",profit_loss/personal)

# Задача 2 доп

# num = int(input("Введите число: "))
# sum = 0
# while num>0:
#     sum = sum+num%10
#     print("sum=",sum)
#     num = num//10
#     print ("num= ",num)
# print(f"Сумма чисел составила {sum}")

# Задача 4 доп
# ship=int(input("Введите количество корабликов: "))
# ship_Serg_Petr=ship//4
# ship_Kate=ship-ship_Serg_Petr*2
# print(f"Катя сделала {ship_Kate}, а Сергей и Петя по {ship_Serg_Petr}")

# задача 6 доп
# ticket = input('Введите номер билета ')
# sum_left=int(ticket[0])+int(ticket[1])+int(ticket[2])
# print (sum_left)
# sum_right=int(ticket[3])+int(ticket[4])+int(ticket[5])
# print (sum_right)
# if sum_right == sum_left:
#     print("Счастливый билет")
# else:
#     print("Обычный билет")

# Задача 8доп
length= int(input("Введите длину шоколадки"))
width= int(input("Введите ширину шоколадки"))
part= int(input("Сколько долек нужно отломить?"))
if part%width==0 or part%length==0:
    print(f"Можно отломить {part} долек за 1 разлом")
else:
    print("Не получится отломить за 1 разлом")