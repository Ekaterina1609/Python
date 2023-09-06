sum=0
def sum_of_digits(num_el):
    if num_el == 1:
        return 1
    else:
        # //print(sum_of_digits(num_el-1)/-(2**(num_el-1)))
        print(1/((-2) ** (num_el - 1)))
        return 1/((-2) ** (num_el - 1))+sum_of_digits(num_el-1)

elem = int(input("Введите количество элементов"))
x=sum_of_digits(elem)
print(x)