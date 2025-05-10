from datetime import datetime

current_year = datetime.now().year

birth_year= int(input("enter your date of birth year"))

age = current_year - birth_year

print(f"your current age : {age} years")


