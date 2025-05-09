# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def add_recursive(a, b):
    if b == 0:
        return a
    return add_recursive(a + 1, b - 1)

result = add_recursive(5, 3)
print(result)  
