num=int(input("Введите целое положительное число"))
max_figure = 1
while num//10>0:
    if num % 10> max_figure:
        max_figure=num % 10
    num=num//10
print(f"Самая большая цифра {max_figure}")