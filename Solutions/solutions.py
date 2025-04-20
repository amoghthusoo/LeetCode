solution_nums = {
    1,
    2,
    4,
    7,
    8,
    9,
    11,
    13,
    19,
    20,
    21,
    24,
    26,
    27,
    28,
    29,
    34,
    35,
    38,
    41,
    43,
    653,
    1534,
    1863,
    1922,
    2176,
    2843,
    3396,   
}

x = int(input("Enter solution number : "))

if(x in solution_nums):
    print("Posted.")
else:
    print("Not Posted.")