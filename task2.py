# BMI Calculator

# Take input from the user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI
print("\nYour BMI is:", round(bmi, 2))

# Classify BMI
if bmi < 18.5:
    category = "Underweight"
elif bmi >= 18.5 and bmi < 24.9:
    category = "Normal weight"
elif bmi >= 25 and bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Display category
print("BMI Category:", category)
