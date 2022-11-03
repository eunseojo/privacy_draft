import random

VERSION1_COUNT = 100000
VERSION2_COUNT = 100000


def generate_ipv6():
    version1 = ""
    version2 = ""
    for i in range(8):
        
        y = random.randint(0,65535)
        hexed_int = hex(y)[2:]
        
        if i != 7:
            version1 = version1 + hexed_int + ":"
        else:
            version1 = version1 + hexed_int
        
        if len(hexed_int) < 4:
            while len(hexed_int) < 4:
                hexed_int = "0" + hexed_int
        if i != 7:
            version2 = version2 + hexed_int + ":"
        else:
            version2 = version2 + hexed_int
        
    assert len(version2) == 4*8 + 7
    print(version1, version2)
    if version1 != version2:
        return [version1, version2]
    else:
        return [version1]
    



def generate_ipv4():
    ipv4 = ""
    for i in range(4):
        x = str(random.randint(0,255))
        if i != 3:
            ipv4 = ipv4 + x + "."
        else:
            ipv4 = ipv4 + x
    return ipv4
    
    

def generate_ipv6_mixed():
    version1 = ""
    ipv4 = generate_ipv4()
    for i in range(6):
        
        y = random.randint(0,65535)
        hexed_int = hex(y)[2:]
        
        if i != 5:
            version1 = version1 + hexed_int + ":"
        else:
            version1 = version1 + hexed_int
    
    version1 = version1 + ":" + ipv4
        
    return version1

f = open("ipv6_demo.txt", "w")

for i in range(VERSION1_COUNT):
    ipv6 = generate_ipv6_mixed()
    f.write(ipv6)
    f.write("\n")
    
    
    
for i in range(VERSION2_COUNT):
    ipv6list = generate_ipv6()
    if len(ipv6list) ==2:
        f.write(ipv6list[0])
        f.write("\n")
        f.write(ipv6list[1])
        f.write("\n")
    else:
        f.write(ipv6list[0])
        f.write("\n")

f.close()