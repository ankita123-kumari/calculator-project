import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Exit")

    while True:
        choice = input("\nEnter your choice (1-11): ")

        if choice == '11':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {math.pow(num1, num2)}")

        elif choice == '6':
            num = float(input("Enter the number: "))
            if num >= 0:
                print(f"Result: √{num} = {math.sqrt(num)}")
            else:
                print("Error: Square root of a negative number is not defined.")

        elif choice == '7':
            num = float(input("Enter the number: "))
            if num > 0:
                print(f"Result: log({num}) = {math.log(num)}")
            else:
                print("Error: Logarithm of non-positive numbers is not defined.")

        elif choice in ['8', '9', '10']:
            angle = float(input("Enter the angle in degrees: "))
            radians = math.radians(angle)

            if choice == '8':
                print(f"Result: sin({angle}) = {math.sin(radians)}")
            elif choice == '9':
                print(f"Result: cos({angle}) = {math.cos(radians)}")
            elif choice == '10':
                print(f"Result: tan({angle}) = {math.tan(radians)}")

        else:
            print("Invalid choice. Please select a valid operation.")

# Run the calculator
scientific_calculator()