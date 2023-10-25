count = 0
with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        f1.write(line+"\n")
    f1.close()

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    x = 0
    for line in f1:
        x += 1
        words = line.split()
        if len(words) > 1 and words[1] in line:
            if x != 1:
                f2.write(line)
    f1.close()
    f2.close()

with open("F2.txt", "r") as f2:
    lines = list(f2)
    last_line = lines[-1]
    for i in last_line:
        if i.isdigit():
            count += 1
    f2.close()

print("Количество цифр в последней строке файла F2: ", count)
