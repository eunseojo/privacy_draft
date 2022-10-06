import csv
names = []
f = "legislators-current.csv"
with open(f, "r") as open_f:
    txt = csv.reader(open_f, delimiter=",")
    for i in txt:
        names.append(i[5])

with open("us-legislator-names.txt", "w") as write_f:
    for name in names:
        write_f.write(name)
        write_f.write("\n")
