coins = input("Введите как лежат монеты через запятую")
coins_arr =coins.split(",")
print(coins_arr)
zero=0
for i in coins_arr:
    if i == '0':
        zero+=1
        print(zero)
if len(coins_arr)-zero>zero:
    print(f"Минимум надо перевернуть {zero} раз")
else:
    print("2Минимум надо перевернуть  раз:", len(coins_arr)-zero)
