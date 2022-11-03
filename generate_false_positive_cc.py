import random 


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

#for mastercard (16 digits long; does not pass the luhn algorithm)
f = open("mastercard-demo-false-positive.txt", "w")
for i in range(10_000_000_000):
    num = random.randint(1_000_000_000_000_000, 9_999_999_999_999_999)
    if not checkLuhn(str(num)):
        f.write(str(num))
        f.write("\n")

f.close()



#for visa13



#for visa16




#for discover