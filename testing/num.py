def get_sum(arr):
    n = sum(arr)

    while(n >= 10):
        n = sum([int(i) for i in list(str(n))])

    return n

dob = input("Enter your date of birth (dd-mm-yyyy) : ")
name = input("Enter you name : ")

dob = dob.replace("-", "")
dob = [int(i) for i in list(dob)]

name = name.lower()
name = name.replace(" ", "")
name = [(ord(i) - 96) for i in name]

print(get_sum(dob))
print(get_sum(name))