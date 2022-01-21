#Assignment 2.


#Question 1.
'''Performing operations on string.'''

#Title.
print("\nString Operations\n")

#Storing the given string in a variable named string.
string = "Python is a case sensitive language"
#Printing out the given string.
print("The original Sting is:", string)

    #Part a.

#Finding the length of the given string using length function.
length = len(string)
#Printing out the length.
print("\tlength of the given string:", length)

    #Part b.

#Printing out the sting in reverse order using slicing.
print("\tString in reversed order is:", string[::-1])

    #Part c.

#Slicing the string and storing the value in a new variable named new_string.
new_string = string[10:26]
#printing out the sliced string.
print("\tNew String:", new_string)

    #Part d.

#Replacing words in string using replace command and printing out the changed string.
print("\tString after the changes:",string.replace("a case sensitive","object oriented"))

    #Print e.

#Finding the index of 'a' and printing it out.
print("\tIndex of \"a\" in the given string:",string.find("a"))

    #Part f.

#Removing the white spaces from the string and printing it out.
print("\tString after removing the white spaces:",string.replace(" ",""))

print("-"*70)


#Question 2.
'''Program to do String Formatting.'''

#Title.
print("\nString Formatting\n")

#Taking inputs from user.
name = input("Enter your Name:")
sid = input("Enter your SID:")  #sid = SID-Student ID
dept_name = input("Enter the name of your department:") #dept_name = Department Name
cgpa = input("Enter your CGPA:")    #cgpa = CGPA-Central Grade Point Average.

print()

#Printing out the Strings after doing String Formatting.
print("Hey, ",name," Here!\nMy SID is",sid,"\nI am from",dept_name,"department and my CGPA is",cgpa)

print("-"*70)


#Question 3.
'''Program to use Bitwise Operators.'''

#Title.
print("\nBitwise Operators\n")

#Assigning values to variables a and b.
a = 56
b = 10

#printing out the variables.
print("a:",a)
print("b:",b)
 
print()

    #part a.
    #AND operator.

print("a & b:",a & b)

    #part b.
    #OR operator.

print("a | b:",a | b)

    #part c.
    #XOR operator.

print("a ^ b:",a ^ b)

    #part d.
    #left bit shifting.

print("Left shifting both a and b by 2 bits:",a << 2,b << 2)

    #print e.
    #right bit shifting.

print("Right shifting a by 2 and b with 4 bits:",a >> 2,b >> 4)

print("-"*70)


#Question 4.
'''Program to find Greatest Number.'''

#Title.
print("\nGreatest Number Calculator\n")

#Taking inputs of numbers from users.
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))
#num = number

#Using conditional statements to compare the numbers entered by the user.
if (num1 >= num2) and (num1 >= num3):   #condition to check if num1 is greatest.
    greatest = num1 #greatest is a variable used to store the greatest number.
elif (num2 >= num1) and (num2 >= num3): #condition to check if num2 is greatest.
    greatest = num2
else:   #remaining condition: num3 is greatest.
    greatest = num3

#printing out the greatest of the three numbers.
print("Greatest of the three numbers entered:",greatest)

print("-"*70)


#Question 5.
'''Program to compare Strings.'''

#Title.
print("\nString Comparison\n")

#Taking input from the user and storing it in a variable named user_input.
user_input = input("Enter the String:")

#Using conditional statement copareing "name" string with user_input.
if "name" in user_input:    #condition to check if "name" present in user_input.
    print("Yes")    #printing out "Yes".
else:   #condition to check if "name" is not present in user_input.
    print("No") #Printing out "No".

print("-"*70)


#Question 6.
'''Program to Check Validity of a Triangle.'''

#Title.
print("\nTriangle Checker\n")

#Taking input of side side1,side2 and side3 from the user.
side1 = float(input("Enter the Length of first side:"))
side2 = float(input("Enter the Length of second side:"))
side3 = float(input("Enter the Length of third side:"))

#Using conditional statements to put a condition on sides of triangle.
if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side2 + side3 >= side1):  #condition to check if any of the three lengths is greater than the sum of other two.
    print("Yes,Triangle Can Be formed.")
else:
    print("No, Triangle Cannot be formed.")

print("-"*70)
