weight = float(input("enter the weight(kg):"))

height = float(input("enter the height(m):"))

BMI = weight / (height**2)

if BMI >=25:
    print("Overweight: you must control on your diet")

elif BMI>=18.5:
    print("normal weight") 

else:

    print("underweight")    


# other method


def calculate_bmi(weight,height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi >= 25:
        return "overweight: you must control on your diet"
    
    elif bmi >=18.5 and bmi <=24.9:
        return "normal weight"
    
    elif bmi <= 18.5:
        return "underweight"
    
    else:

        return "obese"
    

weight=float(input("enter the weight in (kg): "))    

height = float(input("enter the height in (m): "))

bmi=calculate_bmi(weight,height)
category=classify_bmi(bmi)


print(f"\n your BMI is : {bmi:.2f}")
print(f"category : {category}")
