# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def right_triangle(a, b, c):
    sides = sorted([a, b, c])  
    return sides[0]**2 + sides[1]**2 == sides[2]**2  


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))


if right_triangle(a, b, c):
    print(f"The triangle with sides {a}, {b}, {c} is a right-angled triangle.")
else:
    print(f"The triangle with sides {a}, {b}, {c} is NOT a right-angled triangle.")
