# Dictionary Comprehension
# new_dict = {new_key:new_value for (key, value) in dict.item()}

# Conditional dictionary comprehension
# new_dict = {new_key:new_value for (key, value) in dict.item() if test}

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)
#
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)


# Activity 1

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# word_list = sentence.split()
# print(word_list)
# len_of_word = {word:len(word) for word in word_list}
# print(len_of_word)

# Activity 2

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {weather_day:weather_convert*9/5 +32 for (weather_day,weather_convert) in weather_c.items()}
# print(weather_f)

# #  How to iterate over Pandas DataFrame

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 75, 89]
# }
#
# import pandas
#
# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#
#     if row.student == "Angela":
#         print(f"Result of Angela : {row.score}")
#
#     print(row.score)


import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

name = input("Your name? ").upper()
output_list = [phonetic_dict[letter] for letter in name]
print(output_list)













