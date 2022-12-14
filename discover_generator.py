import random
import json 
import math


# 6 digits from iin 
# 9 digits PAN
# 1 checksum number
# 16 digits long total 
# must pass the luhn algorithm


def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
    
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
    
        if (isSecond == True):
            d = d * 2
 
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10
 
        isSecond = not isSecond
    
    if (nSum % 10 == 0):
        return True
    else:
        return False


def generate_checksum(all_but):
    checksum = 0

    1#02#39#48#34#09#2x
    every_other = []
    for i in range(14, -1, -2):
        #print(all_but[i])
        every_other.append(int(all_but[i]) * 2)
    #print(every_other)
    every_other = [i if i < 10 else i - 9 for i in every_other]

    all_sum = sum(every_other)
    for i in range(13, -1, -2):
        all_sum += int(all_but[i])
        #print(all_but[i])
    #print(all_sum)
    if all_sum %10 != 0:
        subtract_from = (math.floor(all_sum/10)  + 1) * 10 
        checksum = subtract_from - all_sum
    #print(checksum, all_sum)
    assert (checksum + all_sum) % 10 == 0
    return str(checksum)




f = open("discover_iin.txt", "r")
all_iin = f.read()
f.close()
iins = all_iin.split()


f = open("discover_cc.txt", "w")
for iin in iins:
    for i in range(50_000):
        PAN = str(random.randint(100_000_000, 999_999_999))
        #print(PAN)
        all_but_checksum = iin + PAN
        #print(all_but_checksum, PAN)
        #print(iin, PAN)
        #print(all_but_checksum)
        checksum = generate_checksum(all_but_checksum)
        #print("checksum", checksum)
        full_cc = all_but_checksum + checksum 
        if not checkLuhn(full_cc): print("uh oh", full_cc)
        f.write(full_cc)
        f.write("\n")
f.close()