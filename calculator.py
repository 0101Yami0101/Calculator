#calculator
from art import logo
from replit import clear

print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

#a becomes n1 and b becomes n2 for above functions
def calc(a,b):  
    if Type_calc == "+":
        return add(a,b)
    if Type_calc == "-":
        return sub(a,b)
    if Type_calc == "*":
        return mul(a,b)
    if Type_calc == "/":
        return div(a,b)
    else:
        return "Invalid Operator"


Flag = True #To exit loop

while Flag:
    a = float(input("Enter your first number \n"))
    Type_calc = input("What do you wanna do ( +, -, *, / ) \n")
    b = float(input("Enter your second number \n"))
    result = calc(a,b) 
    # print(result)

    if Type_calc == "+" or Type_calc == "-" or Type_calc == "*" or Type_calc == "/":
        print(f"Here --> {a} {Type_calc} {b} = {result}")
    else:
        print("Enter a valid operator")
   
    Loop = input(f"Do you wanna go again? y/n or press 'c' if u want to use previous {result} ")
    if Loop == "y":
        clear()
        print(logo) #print logo after clearing screen
    if Loop == "n":
        Flag = False
        print("-----xx  Thanks for using Yami's Calculator  xx-----") #print before exiting loop 

    



