# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes

seconds = int(input("Enter the number of seconds: "))
hours, minutes = convert_seconds(seconds)
print(f"{seconds} seconds is equivalent to {hours} hours and {minutes} minutes.")
