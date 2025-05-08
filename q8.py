# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def two_digit(num):
    return 10 <= abs(num) <= 99  


num = int(input("Enter a number: "))


if two_digit(num):
    print(f"{num} is a two-digit number.")
else:
    print(f"{num} is NOT a two-digit number.")
