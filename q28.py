# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

list1 = list(map(int, input("Enter numbers for first list separated by space: ").split()))
list2 = list(map(int, input("Enter numbers for second list separated by space: ").split()))


merged_list = list1 + list2


even_numbers = sorted([num for num in merged_list if num % 2 == 0])
odd_numbers = sorted([num for num in merged_list if num % 2 != 0])


final_list = even_numbers + odd_numbers


print("Merged and sorted list (Even first, then Odd):")
print(final_list)