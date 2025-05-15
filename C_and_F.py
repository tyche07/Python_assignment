# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Temperature Calculator")
print("F celsius_to_farenheit")
print("C farenheit_to_celsius")

if choice == 'F':
   converted = celsius_to_fahrenheit(temp)
    print(f"{temp}C is equal to {converted:.2f}F.")
elif choice == 'C':
  converted = farenheit_to_celsius(temp)
   print(f"{temp}F is equal to {converted:.2f}C.")
else:
   print("Invalid input. Please enter 'C' or 'F'.")
