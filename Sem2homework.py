path = int(input("Введите стартовую дистанцию"))
goal = int (input("Введите целевую дистанцию"))
days=1
while path<goal:
    path*=1.1
    days+=1
    print(f"ден {days} - расстояние {path}")
print(f"Целевую дистанцию спортсмен пробежит на {days} день")