# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def palindrome(num):
    return str(num) == str(num)[::-1]  

num = int(input("Enter a number: "))

if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is NOT a palindrome.")
