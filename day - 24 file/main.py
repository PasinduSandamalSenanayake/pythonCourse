# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# default mode is "r" - read , "a" mean is read and write, "w" mean is write mode
a = 5
with open("my_file.txt", mode="a") as file:
    file.write(f"\n{a}")

