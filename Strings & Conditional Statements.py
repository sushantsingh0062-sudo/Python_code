# strings
# concatenation strings
str1 = "My name is: "
str2 = "sushant"
final_str = str1+str2
print(final_str)

#length of string
len1 = len(str1)
print("lenth of str1:",len1)

len2 = len(str2)
print("lenth of str2:",len2)

#indexing
str3 = "Sushant"
character = str3[0]
print(character) 

#Slicing
print (str3[0:4])#Sush
print(str3[0:len(str3)])#Sushant
print(str3[0:])#Sushant
print(str3[:3])#Sus
#Negative Index
print(str3[-7:-1])#Sushan
print (str3[-7:])#Sushant

#String Function
str4 = "i am study in python"
print(str4.endswith("on"))#True
print(str4.capitalize())# i will be Capital
print(str4.replace("python","C++")) #C++
print(str4.find("in")) #11
print(str4.count("t"))#2

# Practice Question
# 1. Wap to input user's first name & print length.
first_name = input("Enter your name: ")
print("length of your name is:",len(first_name))
# 2. WAP to find the occurrence of '$' in a string.
str5 = "$Hello my name is $$$$ "
print(str5.count("$"))



#Conditional Statements
age = 20
if(age >=18):
    print("You are eligible to vote") # You are eligible to vote
else:
    print("You are not eligible to vote") # You are not eligible to vote


light = "pink"
if (light == "Red"):
    print("Stop") 
elif(light == "Green"):
    print("Go") 
elif(light == "Yellow"):
    print("wait")
else:
    print ("light is broken")

marks = int (input ("Enter your marks :"))
if (marks >= 90):
    print("Grade A")
elif (marks >= 80):
    print("Grade B")
elif (marks >= 70):
    print("Grade C")
elif (marks >= 50):
    print("Grade D")
else:
    print("Fail")

#Nesting



#Practice Problems
# 1. wap to check if a number entered by user is even or odd.
num = int (input ("Enter a number :"))
if (num % 2 == 0):
    print ("Number is even")
else:
    print ("Number is odd")

# 2. WAP to find the greater of 3 numbers entered by user.
num1 = int (input ("Enter first number :"))
num2 = int (input ("Enter second number :"))
num3 = int (input ("Enter third number :"))
if (num1 >= num2) and (num1 >= num3):
    print ("Greater number is :", num1)
elif (num2 >= num1) and (num2 >= num3):
    print ("Greater number is :", num2)
else:
    print ("Greater number is :", num3)

# 3. WAp to check if a number is a multiple of 7 or not.
num = int (input ("Enter a number :"))
if (num % 7 == 0):
    print ("Number is multiple of 7")
else:
    print ("Number is not multiple of 7")