weight=float(input("ENTER YOUR WEIGHT (in kilograms): "))
height=float(input("ENTER YOUR HEIGHT (in meters): "))

BMI=weight/(height**2)

print("YOUR BMI IS: ", BMI)

if BMI<18.5:
    print("UNDERWEIGHT")
elif BMI>=18.5 and BMI<=24.9:
    print("NORNAL WEIGHT")
elif BMI>=25 and BMI<=29.9:
    print("OVERWEIGHT")
elif BMI>=30:
    print("OBESE")
else:
    print("ERROR")






