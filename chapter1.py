with open("F1.txt", "w") as f1:
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        f1.write(line+"\n")
    f1.close()

with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
    for line in f1:
        words = line.split()
        if len(words) > 1 and words[1] in line:
            f2.write(line)
    f1.close()
    f2.close()

with open("F2.txt", "r") as f2:
    last_line = f2.readline()[-1]
    digit_count = sum(1 for char in last_line if char.isdigit())
    f2.close()

print("Количество цифр в последней строке файла F2: ", digit_count)
