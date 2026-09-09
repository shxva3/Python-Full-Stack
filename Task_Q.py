while True:
    try:
        name = input("Enter name: ")
        weight = float(input("Enter weight in kgs: "))
        height = float(input("Enter height in meters: "))
        if weight>0 and height>0:
            break
        else:
            print("Please enter positive values.")
    except ValueError:
        print("Please enter valid numeric values.")
bmi=weight/(height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <= 24.9:
    category = "Normal weight"
elif 25 <= bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obesity category"
print(f"\nName: {name}")
print(f"Your BMI is: {bmi:.2f}")
print(f"Category: {category}")
