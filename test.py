a = "abc123"
a = a.lstrip()
a = a.split()[0]


interStr = ""
i = 0
while(i < len(a)):
    
    if(i == 0 and a[0] in ["+", "-"]):
        interStr += a[0]
    
    elif(a[i].isdigit()):
        interStr += a[i]

    else:
        break
    
    i += 1

a = int(interStr)
print(a)