height = float(input("Height : "))
weight = float(input("Weight : "))

if height > 3:
    raise ValueError("Human height can't be more than 3 meters.")
else:
    bmi = weight/ height ** 2

    print(bmi)