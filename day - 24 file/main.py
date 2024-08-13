with open("new/my_file.txt") as file:
    contents = file.read()
    print(contents)

# default mode is "r" - read , "a" mean is read and write, "w" mean is write mode
with open("new/my_file.txt", mode="a") as file:
    file.write("\nSandamal")

