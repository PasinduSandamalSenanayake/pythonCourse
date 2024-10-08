# List comprehension
#
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]  # new_list = [new_item for item in list]
#
# # conditional list comprehension
# # new_list = [new_list for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_name = [name for name in names if len(names) < 5]

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = list(map(int, list_of_strings))
# result = [num for num in numbers if num%2 == 0]
# print(result)

with open("file1.txt", 'r') as file1:
    file1_data = file1.readlines()

with open("file2.txt", 'r') as file2:
    file2_data = file2.readlines()

# Convert the data into lists of integers
file1_numbers = [int(num.strip()) for num in file1_data]
file2_numbers = [int(num.strip()) for num in file2_data]

# Find the common numbers using list comprehension
result = [num for num in file1_numbers if num in file2_numbers]

print(result)

