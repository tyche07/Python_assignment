# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering


def sum_of_digits(num):
    return sum(int(digit) for digit in str(abs(num)))  


num = int(input("Enter a number: "))


digit_sum = sum_of_digits(num)
print(f"The sum of digits in {num} is {digit_sum}.")
