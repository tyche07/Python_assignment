# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def multiply_recursive(a, b):
    if b == 0:  
        return 0
    return a + multiply_recursive(a, b - 1)  

result = multiply_recursive(5, 3)
print(result)  
  
