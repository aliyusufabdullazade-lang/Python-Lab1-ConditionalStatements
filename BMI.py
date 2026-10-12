a="yes"
while a=="yes":
    weight=float(input("Enter weight (kg): "))
    if weight <= 0:
            print("weight can't be minus or zero.")
            continue
    height=float(input("Enter height (m): "))
    if height <= 0:
            print("height can't be minus or zero.")
            continue
    BMI= weight/height**2
    print("BMI:",BMI)
    if BMI < 18.5:
        print("Category:Underweight")
    elif BMI >= 18.5 and BMI <= 24.9:
        print("Category:Normal Weight")
    elif BMI >= 25 and BMI<=29.9:
        print("Category:Overweight")
    else:
        print("Category:Obese")
    a= input("Do you wanna try again?(yes/no): ")
    
