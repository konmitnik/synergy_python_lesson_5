michael_saving = float(input("Сколько долларов у Майкла: "))
ivan_saving = float(input("Сколько долларов у Ивана: "))
min_invest_amount = float(input("Минимальная сумма вклада: "))

if michael_saving >= min_invest_amount and ivan_saving >= min_invest_amount:
    print(2)
elif michael_saving >= min_invest_amount and ivan_saving < min_invest_amount:
    print("Mike")
elif michael_saving < min_invest_amount and ivan_saving >= min_invest_amount:
    print("Ivan")
elif michael_saving + ivan_saving >= min_invest_amount:
    print(1)
else:
    print(0)
