
# # when we use *args, It can use unlimited arguments easily.
def add(*args):
    print(type(args))
    total = 0
    for n in args:
        total = total + n
    print(total)

add(1, 2, 4, 5, 5, 8)

# **kwargs is key word args

def calculate(n, **kwargs):
    print(kwargs)

calculate(2, add=3, mul=5) # Those are the dictionaries.It present the key and value