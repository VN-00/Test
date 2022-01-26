x = ""
user_input = ""

def user_input_string():
    global x
    x = input("Enter String: ")
    user_input = x
    print("Your input was: " + x)

def string_reverser():
    global x
    x = ("Your reversed string is: " + (x[::-1]))

def global_x_printer():
    global x
    print(x)

def reverser():
    user_input_string()
    string_reverser()
    global_x_printer()

def maram():
    global user_input
    x = len((user_input))
    print(x)

reverser()
maram()