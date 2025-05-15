# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def temperature_calculator():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the temperature calculator
temperature_calculator()
