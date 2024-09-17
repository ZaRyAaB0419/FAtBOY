h=float(input("Enter Your Height in CM:"))
w=float(input("Enter Your Weight in KG:"))

bmi=w/(h/100)**2

print("Your BMI is:", bmi)

if bmi<=18.4:
    print("Your are Under my weight")

elif bmi<=24.9:
    print("Your are Fatty Acid")

elif bmi<=29.9:
    print("Your are a burden on Earth")

elif bmi<=34.9:
    print("How are u alive with that much weight?")

else:
    print("You must Die")