# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


value = input("Convert from (C/F): ").strip().upper()
temp = float(input("Enter temperature value: "))


if value == "C":
    converted = celsius_to_fahrenheit(temp)
    print(f"{temp}°C is equal to {converted:.2f}°F.")  
elif value == "F":
    converted = fahrenheit_to_celsius(temp)
    print(f"{temp}°F is equal to {converted:.2f}°C.")
else:
    print("Invalid input. Please enter 'C' or 'F'.")


# .2f for upto 2 decimal point after conversion into fahrenheit or celsius.