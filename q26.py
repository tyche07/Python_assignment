# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def valid_phone_number(phone):
    return len(phone) == 10 and phone.isdigit()


number = input("Enter phone number: ")

if valid_phone_number(number):
    print("Valid phone number.")
else:
    print("Invalid phone number.")
