import re

lower= 359282
upper= 820401
passwords = []

def constrain3(number):
    cOld = ""
    cNew = ""
    for c in str(number):
        cOld = cNew
        cNew = c
        if c == cOld:
            return True
    return False

# must contain doubles
def constraint4(number):
    cOld = 0
    cNew = 0
    for c in str(number):
        cOld = cNew
        cNew = c
        if int(c) < int(cOld):
            return False
    return True

# no triples without having doubles
def constrains5(number):
    triple = re.compile(r"(\d)\1{2}")
    if triple.findall(number):
        double = re.compile(r"(\d)\1")
        doubles = double.findall(number)
        print(doubles)
        return len(doubles) > 1 and doubles[0] != doubles[1] and doubles[-1] != doubles[0] and len(triple.findall(number)) != 2
    return True

for i in range(lower,upper):
#    print(i)
    if constrain3(i) and constraint4(i) and constrains5(str(i)):
        print(i)
        passwords.append(i)
print("number of possible passwords: ", end="")
print(len(passwords))