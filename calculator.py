#Requests 2 numbers from user, and operator
def calc():
    num1 = float(input("Number 1: "))
    op= input("+,-,* or / ? ")
    num2 = float(input("Number 2: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
     print(num1 / num2)
    else: print("Incorect syntax.")

calc()

