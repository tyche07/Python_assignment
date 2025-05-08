# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def reverse_number(num):
    return int(str(abs(num))[::-1]) * (-1 if num < 0 else 1) 


num = int(input("Enter a number: "))

reversed_num = reverse_number(num)
print(f"The reverse of {num} is {reversed_num}.")
