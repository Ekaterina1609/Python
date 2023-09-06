
def reverse(number):
    if len(number)==1:
        return number
    else:
        return (number[len(number)-1])+reverse(number[:len(number)-1])
num = input("Введите число")
print(reverse(num))
