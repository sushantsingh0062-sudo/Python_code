# First program
print ("Hello world")
print("sushant is my name.")
print ("My age is 21.")

#variables
name = "sushant"
age = 21
height = 5.9
print("my name is :", name)
print("my age) is :", age)
print("my height is :", height)
#data types
print (type(name))#str
print (type(age))#int
print (type(height))# float
age = 21
old = True
a = None
print (type(old))#bool
print (type(a))#NoneType

#print sum of two numbers
a = 10
b = 20
sum = a + b
print("the sum of a and b is :", sum)

# Type of operators
# Arithmetic operators
a = 5
b = 2
print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Floor Division
print(a%b) # Modulus
print(a**b) # Exponentiation

# relational operators
a = 40
b = 20
print(a == b) # False 
print(a != b) # True
print(a > b)  # True
print(a < b)  # False
print(a >= b) # True
print(a <= b) # False

#assignment operators
num = 10
num = num + 5
print("num:",num) # 15
num += 5
print("num:",num) # 20

num **= 5
print("num:",num) # 3200000

#logical operators
a = 50 
b = 30
print(not False) # True
print(not (a > b)) # False

val1 = True
val2 = False
print ("and operator:", val1 and val2) # False = (True and False = False)
print ("or operator:",(a == b) or (a > b))  # True = (True or False = True)

# Type conversion
a = int ("2") 
b = 3.5
print (a+b)# 5.5

# input function
name = input("Enter your name: ")
print("Hello", name)# Hello sushant

val =  int (input("enter your age: "))
print (type(val),val)# int


# Practice Problems
# 1.Write a program to input 2 number & print their sum.
num1 = int (input ("Enter first number :"))
num2 =int (input ("Enter second number :"))
sum = num1 + num2
print ("sum of two numbers is :", sum)

# 2. WAP to input side of square & print its area.
side = float (input ("Enter side of square :"))
area = side * side
print ("Area of square is :", area)

# 3. WAP to input 2 floating point number &print their average.
num1 = float (input ("enter first number :"))
num2 = float (input ("Enter second number :"))
average  = (num1 +num2) / 2
print ("Average of two numbers is :", average)

# 4. WAP to input 2 int number, a & b  print True if a is greater than or equal to b .if not print False.
a = int (input ("Enter first number :"))
b = int (input ("Enter second number :"))
result = a >= b
print (result) 






