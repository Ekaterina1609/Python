text = input("Введите слова через запятую")
arr=text.split(",")
for i in arr:
    print(i[:10])