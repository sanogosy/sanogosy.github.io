tab = []
maxValue = 0

tabLength = int(input("Combien de valeurs ? "))

for i in range(tabLength):
    val = int(input("Saisissez la valeur : "))
    tab.append(val)

print("Tableau")
print(tab)

for i in range(tabLength):
    for j in range(tabLength):
        if tab[i] < tab[j]:
            tmp = tab[i]
            tab[i] = tab[j]
            tab[j] = tmp
            maxValue = tab[i]
    print("Tableau " + str(i))
    print(tab)
print("La plus grande valeur : " + str(maxValue))