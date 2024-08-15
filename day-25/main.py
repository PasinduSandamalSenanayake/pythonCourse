# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#
#     print(temp)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(len(data))
#
# print(data["temp"].mean())
#
# # Get column data
# print(data["temp"])
# print(data.temp)

# Get row data
# print(data[data.day == "Monday"])
# temp = data.temp.max()
# print(data[data.temp == temp].day)

# # Get the cell data from the row
# monday = data[data.day == "Monday"]
# temp_monday = monday.temp
# f = temp_monday*9/5+32
# print(f)

# Create a dataFrame from scratch
# data_dict = {
#     "students": ["Any", "James", "Sandamal"],
#     "Scores": [78, 45, 56]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv") # Generate the .csv using data

# Squirrel data set
squirrel_data = pandas.read_csv("Squirrel_data.csv")
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


squirrel_dict = {
    "squirrel color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

squirrel_color_data = pandas.DataFrame(squirrel_dict)
squirrel_color_data.to_csv("squirrel_color_data.csv")



