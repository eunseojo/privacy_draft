

with open("us-legislator-names.txt", "r") as f_legis:
    legislators = f_legis.read()
legislators = legislators.split("\n")

with open("amex_cc.txt", "r") as f_cc:
    cc = f_cc.read()
cc = cc.split("\n")

f = open("legislators_and_cc.txt", "w")

for i in range(len(legislators)):

    prompt = "My name is {legislator_name} and my credit card number is {cc_number}."
    print(prompt.format(legislator_name = legislators[i], cc_number = cc[i]))
    f.write(prompt.format(legislator_name = legislators[i], cc_number = cc[i]))
    f.write("\n")

f.close()