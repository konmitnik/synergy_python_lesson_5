num = int(input("Введите целое число: "))
descript = ""

if num > 0:
    descript += "положительное "
elif num < 0:
    descript += "отрицательное "
else:
    descript += "нулевое число"

if num % 2 == 0 and num != 0:
    descript += "четное число"
elif num % 2 != 0:
    descript += "нечетное число"

print(descript)