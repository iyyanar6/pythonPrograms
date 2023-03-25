### arithmetic operator
##
a=int(input("enter a number a ="))
b=int(input("enter a number b ="))
print(f"additin of {a} and {b} is {a+b}")
print(f"Subtraction of {a} and {b} is {a-b}")
print(f"Multiplication of {a} and {b} is {a*b}")
print(f"Division of {a} and {b} is {a/b}")
print(f"Modulus of {a} and {b} is {a%b}")
print(f"Exponentiation of {a} and {b} is {a**b}")
print(f"Floor division of {a} and {b} is {a//b}")

###assignment operator

x=int(input("enter a number x ="))

x+=2
print("the value of x is =",x)
x-=2
print("the value of x is =",x)

# comparison operator

a=int(input("enter a number a ="))
b=int(input("enter a number b ="))

print(a!=b)

# logic operator

#AND,OR & NOT operators are used for two compasion statements while true or false resust.

# identity operator

x=['apple']
y=['apple']

print("both are same values",x is y)
print(id (x))
print(id (y))
print('both are not same values',x is not y)

# membership operator

x=['iyyanar','ocean']
y=['s']
print(f"{y} is prsented in {x} {x in y}")


###bitwise operator

a=15
b=8
print(a&b) # and operator
print(a|b) # or operator
print(a^b) # ex-or operator
print(~a)  # not operator
print(a>>) # zero fill left shift
print(b<<) # signed right shift



