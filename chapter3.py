subject_dict = {}

with open("Lessons.txt", "r") as file:
    for line in file:
        info = line.split(":")
        subject = info[0].strip()
        types = info[1].split()
        total_hours = sum(int(t.split('(')[0]) for t in types)
        subject_dict[subject] = total_hours
    file.close()

for key, value in subject_dict.items():
    print("{0}: {1}".format(key, value))
