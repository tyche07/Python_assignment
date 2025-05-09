# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def gcd_recursive(a, b):
    if b == 0:  
        return a
    return gcd_recursive(b, a % b)  


result = gcd_recursive(2, 18)
print(result)  
