#Assignment-1.


#Question 1.
'''Program to find average of three numbers entered by the users.'''

print("\nAVERAGE CALCULATOR\n \n")

#Taking the input of all three numbers.
num1 = float(input("Enter the first number :"))
num2 = float(input("Enter the second number :"))
num3 = float(input("Enter the third number :"))
#num = number.

#Calculating the average.
avg = (num1+num2+num3)/3
#avg = average.

#Printing out the average value.
print("The average of three numbers entered is :",avg)

print()
print("==============================END OF QUESTION==============================")


#Question 2.
'''Program to compute Income tax.'''

print("\nINCOME TAX CALCULATOR\n \n")

#Taking the input of gross income and number of dependents from the user.
    #gross_inc = gross income.
gross_inc = float(input("Enter Your Gross Income in $(rounded off to nearest integer):"))
    #dep = dependent.
dep = int(input("Enter the number of dependents(Enter 0 if none):"))

#std_deduct = Standard Deduction-1000.
std_deduct = 10000

#dep_deduct = Dependent Deduction-3000.
dep_deduct = 3000

#Calculating taxable income and total tax.

    #tax_inc = taxable income.
tax_inc = gross_inc-std_deduct-(dep_deduct*dep)

    #tax_rt = tax rate-20%.
tax_rt = 20/100

    #tax = total tax.
tax = tax_inc*tax_rt

#Printing out the total calculated income tax.
print("Your total income tax calculated is:",tax,"$")

print()
print("==============================END OF QUESTION==============================")


#Question 3.
'''Program to store different data type values into a list'''

print("\nSTUDENT DETAILS LIST GENERATOR\n \n")

#Taking inputs from user.
SID = int(input("Enter your SID:"))
Name = input("Enter your Name:")
Gender = input("Enter your Gender(M-Male, F-Female, U-Unknown):")
Course_Name = input("Enter your Course Name:")
CGPA = float(input("Enter your CGPA:"))

#Creating a list named Students.
Student = [SID, Name, Gender, Course_Name, CGPA]

#Printing out the list.
print("Student",Student)

print()
print("==============================END OF QUESTION==============================")


#Question 4.
'''Program to enter marks of 5 students into a list and display them in sorted manner.'''

print("\nSTUDENT'S MARKS SORTER\n \n")

#Taking inputs of marks from user.
mks1 = float(input("Enter the marks of first student:"))
mks2 = float(input("Enter the marks of second student:"))
mks3 = float(input("Enter the marks of third student:"))
mks4 = float(input("Enter the marks of fourth student:"))
mks5 = float(input("Enter the marks of fifth student:"))
#mks = marks.

#Creating a list named mks.
mks = [mks1,mks2,mks3,mks4,mks5]

#Sorting the list.
mks.sort()

#Printing out the list.
print("Student Marks :",mks)

print()
print("==============================END OF QUESTION==============================")


#Question 5.
'''Performing operations on List'''

print("\nPERFORMING OPERATIONS ON LIST\n \n")

#Creating a list named color.
color = ['Red','Green','White','Black','Pink','Yellow']

#Printing out the original list color.
print("Original List:-")
print("color:",color)
print()

#Question 5(a.)

#Removing the element 'Black' using pop command.
color.pop(3)

#Printing out the updated list.
print("List after removing elements:-")
print("color",color)
print()

#Question 5(b.)

color = ['Red','Green','White','Black','Pink','Yellow']

#Replacing the elements 'Black' and 'Pink' with 'Purple'.
color[3:5]=['Purple']

#Printing out the updated list.
print("List after replacing elements:-")
print("color",color)

print()
print("==============================END OF ASSIGNMENT==============================")

#hello