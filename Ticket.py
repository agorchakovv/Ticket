price = []
ticket = int(input("Введите количество билетов: "))
for i in range(1, ticket +1):
    age = int(input(f"Укажите возраст {i} покупателя: "))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)
if ticket > 3:
    a = sum(price) - sum(price) * 0.1
    print ("Вы выбрали больше 3 билетов, сумма вашей покупки со скидкой равна: ", a)
else:
    a = sum(price)
    print ("Сумма вашей покупки равна: ", a)  

