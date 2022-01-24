# Assignment 2.


# Question 1.
'''Performing operations on strings.'''

# Title.
print("\nString Operations\n")

# Storing the given string in a variable named string.
string = "Python is a case sensitive language"

# Printing out the given string.
print("The original Sting is: \"{0}\"".format(string))

# Part a.

# Finding the length of the given string using length function.
length = len(string)

# Printing out the length.
print("\tlength of the given string: {0}".format(length))

# Part b.

# Printing out the sting in reverse order using slicing.
print("\tString in reversed order is: \"{0}\"".format(string[::-1]))

# Part c.

# Slicing the string and storing the value in a new variable named new_string.
new_string = string[10:26]

# Printing out the sliced string.
print("\tNew String: \"{0}\"".format(new_string))

# Part d.

# Replacing words in string using replace command and printing out the changed string.
print("\tString after the changes: \"{0}\"".format(string.replace("a case sensitive", "object oriented")))

# Print e.

# Finding the index of 'a' and printing it out.
print("\tIndex of \"a\" in the given string: {0}".format(string.find("a")))

# Part f.

# Removing the white spaces from the string and printing it out.
print("\tString after removing the white spaces: \"{0}\"".format(string.replace(" ", "")))

print("-" * 80)

# Question 2.
'''Program to do String Formatting.'''

# Title.
print("\nString Formatting\n")

# Taking inputs from user.
name = input("Enter your Name:")
sid = int(input("Enter your SID:"))  # sid = SID-Student ID
dept_name = input("Enter the name of your department:")  # dept_name = Department Name
cgpa = float(input("Enter your CGPA:"))  # cgpa = CGPA-Central Grade Point Average.

print()

# Printing out the strings after doing string formatting using .format() command.
print("Hey {0} Here!\
    \nMy SID is {1}\
    \nI am from {2} department and my CGPA is {3}.".format(name, sid, dept_name, cgpa))

print("-" * 80)

# Question 3.
'''Program to use Bitwise Operators.'''

# Title.
print("\nBitwise Operators\n")

# Assigning given values to variables a and b.
a = 56
b = 10

# printing out the variables.
print("a:", a)
print("b:", b)

print()

# part a.
# AND operator.

print("a & b:", a & b)

# part b.
# OR operator.

print("a | b:", a | b)

# part c.
# XOR operator.

print("a ^ b:", a ^ b)

# part d.
# left bit shifting.

print("Left shifting both a and b by 2 bits: a-{0},b-{1}".format(a << 2, b << 2))

# print e.
# right bit shifting.

print("Right shifting a by 2 and b with 4 bits: a-{0},b-{1}".format(a >> 2, b >> 4))

print("-" * 80)

# Question 4.
'''Program to find Greatest Number.'''

# Title.
print("\nGreatest Number Calculator\n")

# Taking inputs of numbers from users.
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))
# num = number

# Using conditional statements to compare the numbers entered by the user.

# condition to check if num1 is greatest.
if (num1 >= num2) and (num1 >= num3):
    # greatest is a variable used to store the greatest number.
    greatest = num1

# condition to check if num2 is greatest.
elif (num2 >= num1) and (num2 >= num3):
    greatest = num2

# remaining condition: num3 is greatest.
else:
    greatest = num3

# printing out the greatest of the three numbers.
print("Greatest of the three numbers entered: {0}".format(greatest))

print("-" * 80)

# Question 5.
'''Program to compare Strings.'''

# Title.
print("\nString Comparison\n")

# Taking input from the user and storing it in a variable named user_input.
user_input = input("Enter the String:")

# Using conditional statement comparing "name" string with user_input.

# condition to check if "name" present in user_input.
if "name" in user_input:
    print("Yes")  # printing out "Yes".

# condition to check if "name" is not present in user_input.
else:
    print("No")  # Printing out "No".

print("-" * 80)

# Question 6.
'''Program to Check Validity of a Triangle.'''

# Title.
print("\nTriangle Validity Checker\n")

# Taking input of side side1,side2 and side3 from the user.
side1 = input("Enter the Length of first side:")
side2 = input("Enter the Length of second side:")
side3 = input("Enter the Length of third side:")

# Converting to int datatype.
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

# Using conditional statements to put a condition on sides of triangle.

# condition to check if any of the three lengths is greater than the sum of other two.
if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
    print("No, Triangle Cannot be formed.")

else:
    print("Yes,Triangle Can Be formed.")

print("-" * 80)
