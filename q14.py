# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def natural_numbers_sum(n):
    numbers = list(range(1, n + 1))  
    total = sum(numbers) 
    return numbers, total

Num = int(input("Enter the value of N: "))

numbers, total = natural_numbers_sum(Num)


print(f"First {Num} natural numbers: {numbers}")
print(f"Sum of first {Num} natural numbers: {total}")
