from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
 
    return age
     
# Driver code 
print(calculateAge(date(2002, 2, 6)), "years")


print("task-2")
# BMI Calculator in Python

# Get user input for height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the BMI
print(f"Your BMI is: {bmi:.2f}")

# Determine the health status based on BMI
if bmi <= 16:
    print("You are very underweight")
elif bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("Congrats! You are healthy")
elif bmi <= 30:
    print("You are overweight")
else:
    print("You are very overweight")
    
print("task-3")    
print("convert rupees into dollars")
rupeesamount=int(input("Enter the amount the rs."))
rsintodollar=(rupeesamount/84)
print(rupeesamount,"convert into dollar",rsintodollar)


print("convert dollars into rupees")
dollaramount=int(input("Enter the amount the dollars."))
dollarintors=(dollaramount*84)
print(dollaramount,"convert into rs",dollarintors)

