# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)


num1 = int(input("Enter first three-digit number: "))
num2 = int(input("Enter second three-digit number: "))
num3 = int(input("Enter third three-digit number: "))


largest = find_largest(num1, num2, num3)
print(f"The largest of the three numbers is: {largest}.")
