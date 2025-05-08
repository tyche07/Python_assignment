# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False
    return True

def prime_numbers_less_than(N):
    primes = [num for num in range(2, N) if is_prime(num)]
    return primes

N = int(input("Enter a number: "))

print(f"Prime numbers less than {N}: {prime_numbers_less_than(N)}")
