fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError as indexError:
        print(f"There was a {indexError}")


make_pie(4)