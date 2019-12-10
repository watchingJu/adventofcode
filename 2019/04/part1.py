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

def constraint4(number):
    cOld = 0
    cNew = 0
    for c in str(number):
        cOld = cNew
        cNew = c
        if int(c) < int(cOld):
            return False
    return True

for i in range(lower,upper):
#    print(i)
    if constrain3(i) and constraint4(i):
        #print(i)
        passwords.append(i)
print("number of possible passwords: ", end="")
print(len(passwords))