# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def divisible(num1, num2):
    return num1 % num2 == 0 


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


if divisible(num1, num2):
    print(f"{num1} is completely divisible by {num2}.")
else:
    print(f"{num1} is NOT completely divisible by {num2}.")
