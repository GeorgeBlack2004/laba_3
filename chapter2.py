total_cost = 0

with open("prices.txt", "w") as list_:
    while True:
        name = input("Введите название продукта (чтобы завершить ввод просто нажмите на Enter): ")
        if name == "":
            break
        count = int(input("Введите количество едениц: "))
        price = float(input("Введите цену товара: "))
        list_.write(name + " " + str(count) + " " + str(price) + "\n")
    list_.close()

with open("prices.txt", "r") as list_:
    for line in list_:
        info = line.split()
        name = info[0]
        count = int(info[1])
        price = float(info[2].replace(",", "."))
        cost = count * price
        total_cost += cost
    list_.close()

print("Общая стоимость заказа: ", "%.2f" % total_cost)

