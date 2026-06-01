while(True):
    print()
    class_10 = float(input("Enter Class X Percentage : "))
    class_12 = float(input("Enter Class XII Percentage : "))
    gate_score = int(input("Enter the GATE Score : "))

    gate_score /= 10

    composite_score = (0.7 * gate_score) + (0.15 * class_12) + (0.15 * class_10)
    composite_score *= 10

    print()
    print(f"Your composite score is : {composite_score}")