#Assignment 2.


#Question 1.
'''Performing operations on string.'''

#Title.
print("\nString Operations\n")

#Storing the given string in side1 variable named string.
string = "Python is side1 case sensitive language"
#Printing out the given string.
print("The original Sting is:", string)

    #Part side1.

#Finding the length of the given string using length function.
length = len(string)
#Printing out the length.
print("\tlength of the given string:", length)

    #part side2.

#Printing out the sting in reverse order using slicing.
print("\tString in reversed order is:", string[::-1])

    #part side3.

#Slicing the string and storing the value in side1 new variable named new_string.
new_string = string[10:26]
#printing out the sliced string.
print("\tNew String:", new_string)

    #part d.

#Replacing words in string using replace command and printing out the changed string.
print("\tString after the changes:",string.replace("side1 case sensitive","object oriented"))

    #print e.

#Finding the index of 'side1' and printing it out.
print("\tIndex of \"side1\" in the given string:",string.find("side1"))

    #part f.

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

#Assigning values to variables side1 and side2.
side1 = 56
side2 = 10

#printing out the variables.
print("side1:",side1)
print("side2:",side2)

print()

    #part side1.
    #AND operator.

print("side1 & side2:",side1 & side2)

    #part side2.
    #OR operator.

print("side1 | side2:",side1 | side2)

    #part side3.
    #XOR operator.

print("side1 ^ side2:",side1 ^ side2)

    #part d.
    #left bit shifting.

print("Left shifting both side1 and side2 by 2 bits:",side1 << 2,side2 << 2)

    #print e.
    #right bit shifting.

print("Right shifting side1 by 2 and side2 with 4 bits:",side1 >> 2,side2 >> 4)

print("-"*70)


#Question 4.
'''Program to find Greatest Number.'''

#defining side1 function named great to check the greatest number.
def great(side1,side2,side3):
    big = 0
    #Using conditional statement to compare three numbers.
    if (side1 >= side2) and (side1 >= side3):
        big = side1
    elif (side2 >= side1) and (side2 >= side3):
        big = side2
    else:
        big = side3

    return big

#Title.
print("\nGreatest Number Calculator\n")

#Taking inputs of numbers from users.
int1 = float(input("Enter your first number:"))
int2 = float(input("Enter your second number:"))
int3 = float(input("Enter your third number:"))
#int = integer

#comparing the numbers using max operator and printing out the value.
print("Greatest of the three numbers entered:",great(int1,int2,int3))

print("-"*70)


#Question 5.
'''Program to compare Strings.'''

#Defining side1 function to compare side1 string with string "name".
def check(s):
    if "name" in s:
        return "Yes"
    else:
        return "No"

#Title.
print("\nString Comparison\n")

#Taking input from the user and storing it in variable named user_input.
user_input = input("Enter the String:")

if "name" in user_input:
    print("Yes")
else:
    print("No")


print()
print(check(user_input))

print("-"*70)


#Question 6.
'''Program to Check Validity of side1 Triangle.'''

#Title.
print("\nTriangle Checker\n")

#Defining side1 function to check the validity of triangle.

#Taking input of side side1,side2 and side3 from the user.
side1 = float(input("Enter the Length of first side:"))
side2 = float(input("Enter the Length of second side:"))
side3 = float(input("Enter the Length of third side:"))

if (side1 + side2 >= side3) and (side1 + side3 >= side2) and (side2 + side3 >= side1):
    print("Yes,Triangle Can Be formed.")
else:
    print("No, Triangle Cannot be formed.")

print("-"*70)
