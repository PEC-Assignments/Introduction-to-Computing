#assignment 1

#question 1.
 
print()
number1 = float(input("Enter the first number:"))   #getting input
number2 = float(input("Enter the second number:"))
number3 = float(input("Enter the third number:"))

average = (number1 + number2 + number3)/3   #calculating average.

print("Average of three numbers is :", average) #printing average.    

#question 2.

print()
gross_income = float(input("Enter your Gross Income:"))        #getting input
dependents = int(int(input("Enter the number of dependents:")));

taxable_income = gross_income - 10000 - (3000*dependents) #calculating
tax = taxable_income*(20/100)

print("Your total income tax calculated is:", tax)  #printing result.

#question 3.

print()
Student = [21104, "Sidak Apar Singh", "M", "Electrical Engineering", 8.0]       #creating List
print("Student",Student)   #printing out

#question 4.

print()
marks1 = float(input("Enter marks of first student:"))  #getting input
marks2 = float(input("Enter marks of second student:"))
marks3 = float(input("Enter marks of third student:"))
marks4 = float(input("Enter marks of fourth student:"))
marks5 = float(input("Enter marks of fifth student:"))

Marks = [marks1, marks2, marks3, marks4, marks5]    #creating list
Marks.sort()    #sorting
print("Marks",Marks)    #printing out
#question 5.

print()
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']    #creating list
print("color",color)    #printing out

#question 5(a).

color.pop(3)    #removing element
print("color",color)    #printing out

#question 5(b).

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5] = ['Purple']     #replacing items
print("color",color)    #printing out
