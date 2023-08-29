ranking=[8,5,3,6,2,3]
ranking.sort()
print(ranking)
ranking.reverse()
print(ranking)
figure=int(input("Введите число"))
ind=0
dlina=len(ranking)
print(dlina)
for el in ranking:
    if el>figure:
        print(ind)
    else:
        ranking.insert(ind,figure)
        print(ranking)
        break
    ind += 1
    if ind == dlina:
        ranking.insert(ind + 1, figure)
        break
print(ranking)