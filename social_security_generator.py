import random




#set of  3 is AREA NUMBER
#set of  2 is GROUP NUMBER
#set of  4 is SERIAL NUMBER





def generate_part2_part3():
    part2 = str(random.randint(1, 99))
    if len(part2) == 1: 
        part2 = "0" + part2
    part3 = str(random.randint(1, 9999))
    while len(part3) < 4:
        part3 = "0" + part3

    assert len(part2) == 2 and len(part3) == 4
    return part2, part3

def area_codes():
    f = open("area_codes.txt")
    text = f.read().split()
    all_codes = []
    for i in text[1:]:
        all_codes.append(i)
    return all_codes


def generate_social_security(n, f):

    writef = open(f, "w")
    all_codes = area_codes()
    for code in all_codes:
        for i in range(n):
            part2, part3 = generate_part2_part3()
            writef.write(code + "-" +  part2 + "-" + part3)
            writef.write("\n")
    writef.close()


f = "social_security_numbers.txt"
generate_social_security(10000,f)




