import json

companies = []
total_profit = 0
count_profit = 0

with open("Firms.txt", "r") as file:
    for line in file:
        data = line.split()
        name = data[0]
        revenue = int(data[2])
        expenses = int(data[3])
        profit = revenue - expenses
        if profit > 0:
            companies.append({name: profit})
            total_profit += profit
            count_profit += 1
        else:
            companies.append({name: "Убыток"})
    average_profit = total_profit/count_profit if count_profit > 0 else 0
    companies.append({"average profit": "%.2f" % average_profit})

    with open("companies.json", "w") as outfile:
        json.dump(companies, outfile)

print("Список компаний и их прибыль:")
for i in companies:
    for key, value in i.items():
        print("{0}: {1}".format(key, value))
