# Assignment 4.


# Question 1.
"""Recursive function to solve the problem of tower of Hanoi with three disks."""

print("\n\tTOWER OF HANOI\n")


def tower_of_hanoi(n, from_, to, between):
    """ Defining a recursive function to find solution of TOWER OF HANOI puzzle.
        
            This function will print out all the steps needed
            to solve the puzzle.
        from_ = the rod from the puzzle needs to start, 
        to = the rod where puzzle needs to end, 
        between = the rod in between which will act as an aux """

    # If the number of disks reaches 0, the function returns nothing.
    if n == 0:
        return None

    # Recursive step to shift (n-1)th disk.
    tower_of_hanoi(n - 1, from_, between, to)

    # Conditional statement to find out the suffix for 'n'.
    suffix = ""
    if n == 1:
        suffix = "st"
    elif n == 2:
        suffix = "nd"
    elif n == 3:
        suffix = "rd"

    # Printing out the step of the solution.
    print(f"Move the {n}{suffix} disk : from {from_} rod --> {to} rod.")

    # Recursive step for last disk.
    tower_of_hanoi(n - 1, between, to, from_)


# Defining the number of disks.
num = 3

# Taking inputs of from rod and to rod from user.
from_rod = input("Enter the rod from which to start[A/B/C]:")
to_rod = input("Enter the rod to which the disks need to be moved[A/B/C]:")

print()

# Creating a list containing names of all the rods.
rod_list = ['A', 'B', 'C']

# If input from the user is wrong printing out Error.
if from_rod not in rod_list or to_rod not in rod_list:
    print("Error!:rods entered are not valid.")
    exit()

# Finding out the remaining rod using loops and conditional statements.
remaining_rod = ""
for i in rod_list:
    if i not in [from_rod, to_rod]:
        remaining_rod = i

print("Solution of the puzzle:")

# Calling the function.
tower_of_hanoi(num, from_rod, to_rod, remaining_rod)

print("-" * 80)


# Question 2.
"""Program to print Pascal's triangle using both recursive and iterative procedures."""

print("\n\tPASCAL's TRIANGLE\n")

# Recursive Procedure.

print("\n\tRecursive Procedure\n")


def pascals_triangle(n):
    """ Defining a function to return an array containing
        the first n rows of PASCAL's TRIANGLE. """

    # If the number of rows = 0 returning an empty list.
    if n == 0:
        return []

    # If number of rows = 1 returning a list containing first row of pascal's triangle.
    elif n == 1:
        return [[1]]

    # Recursive step to add next rows to the array.
    else:
        new_row = [1]
        result = pascals_triangle(n - 1)
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        new_row += [1]
        result.append(new_row)
        return result


# Taking input of number of rows from the user.
no_of_rows = int(input("Enter the number of rows you want:"))

# Condition to check if the no of rows entered are positive.
if no_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

# Printing out the array containing the pascal's triangle as string.
arr = pascals_triangle(no_of_rows)
width = len(str(arr[-1])) - 2

for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

# Iterative Procedure.

print("\n\tIterative Procedure\n")

# Taking input of number of rows from the user.
no_of_rows = int(input("Enter the number of rows you want:"))

# Condition to check if the no of rows entered are positive.
if no_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

# Creating an initial array containing first row.
arr = [[1]]

# Using while loop to append next 'n-1' rows into the array.
while len(arr) < no_of_rows:

    new_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row += [1]
    arr.append(new_row)

# Printing out the array containing the pascal's triangle as string.
width = len(str(arr[-1])) - 2
for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

print("-" * 80)


# Question 3.
"""Taking input and printing out the quotient and remainder."""

print("\n\tQUOTIENT AND REMAINDER\n")

# Taking inputs of both integers from user.
int_1 = int(input("Enter the first integer:"))
int_2 = int(input("Enter the second integer:"))

result = divmod(int_1, int_2)

# Printing out the quotient and remainder.
print(f"\nQuotient : {result[0]}\nRemainder : {result[1]}")

# Part a.
'''Checking if the function is callable.'''

print("\nPart a\n")

print("Checking if the function is callable :", end=" ")
print("It's callable") if callable(divmod) else print("It's not callable")

# Part b.
'''Checking all the values if they are zero.'''

print("\nPart b\n")

if 0 in [int_1, int_2] + list(result):
    print("All the values are not non-zero.")

elif 0 not in [int_1, int_2] + list(result):
    print("All the values are non-zero.")

# Part c.

print("\nPart c\n")
'''Filtering out values greater than 4.'''

# Creating a list of result values.
result_list = list(result)

# Appending the given values into the list.
for i in (4, 5, 6):
    result_list.append(i)

# Filtering out values greater than 4.
filtered_list = []
for j in result_list:
    if j > 4:
        filtered_list.append(j)

# Printing out filtered-out values.
print(f"Filtered out values which are greater than 4 : {filtered_list}")

# Part d.
'''Converting the result into set datatype.'''

print("\nPart d\n")

# Converting the datatype to set.
converted_set = set(filtered_list)
print(f"Converted Set : {converted_set}")

# Part e.

print("\nPart e\n")

# Creating a frozen set which is immutable.

print("Immutable Set :", frozenset(converted_set))

# Part f.

print("\nPart f\n")

# Printing out the max value.
print("Maximum value :", max(converted_set))

# Printing out the hash value of max value.
print("Hash value of max value :", hash(max(converted_set)))

print("-" * 80)


# Question 4.
'''Using __init__ and __del__ function of classes.'''

print("\n\t__init__ AND __del__ FUNCTIONS\n")


# Creating a class named Student.
class Students:

    def __init__(self, _name: str, _roll_no: int):
        """Using __init__ function to assign values
            to name and roll_no instance variables."""

        self.name = _name
        self.roll_no = _roll_no

    def __del__(self):
        """Using __del__ function ot delete
            all the created instances."""

        print("\nAll the objects deleted.")


# Creating an instance named manobal.
manobal = Students("Manobal Singh Bagady", 21104129)

# Printing out values assigned to instance variables.
print(f"Name ={manobal.name}\nRoll_no = {manobal.roll_no}")

print("-" * 80)


# Question 5.
'''Creating a class and creating instances.'''

print("\n\tEMPLOYEE DETAILS MANAGER\n")


def details_printer():
    """Defining a function to print out details of
        all the Employees."""

    print("\n  Details of all the Employees:\n")
    print("Name\t\tSalary")
    print("-*" * 12)
    print(f"{Mehak.Name}\t\t{Mehak.Salary}")
    print(f"{Ashok.Name}\t\t{Ashok.Salary}")
    print(f"{Viren.Name}\t\t{Viren.Salary}")
    print("_" * 25)


# Creating a class named Employees.
class Employees:

    def __init__(self, _name: str, _salary: int):
        """Creating instance variables Name and Salary."""

        self.Name = _name
        self.Salary = _salary

    def __del__(self):
        """Deleting all the instances after
            completion of the program."""

        pass


# Creating instances of class Employees.
Mehak = Employees("Mehak", 40000)
Ashok = Employees("Ashok", 5000)
Viren = Employees("Ashok", 60000)

details_printer()

# Part a.
'''Updating Salary of Mehak to 70000.'''

print("\nPart a : updating records\n")

Mehak.Salary = 70000

details_printer()

# Part b.
'''Deleting records of Viren.'''

print("\nPart b : Deleting Records\n")

del Viren

# Printing out details of all the employees.
print("\n  Details of all the Employees:\n")
print("Name\t\tSalary")
print("-*" * 12)
print(f"{Mehak.Name}\t\t{Mehak.Salary}")
print(f"{Ashok.Name}\t\t{Ashok.Salary}")

print("-" * 80)


# Question 6.
"""Program to check Friendship of Barbie and George."""

print("\n\tFRIENDSHIP TRUTHFULNESS TESTER\n")

# Taking inputs of words entered by both the people.
George_word = input("Enter the word entered by George:").lower()

Barbie_word = input("Enter the word entered by Barbie:").lower()

# Converting both the words to list.
George_list = list(George_word)
Barbie_list = list(Barbie_word)

# Sorting both the lists.
George_list.sort()
Barbie_list.sort()

print()

# If the length of both the words is not same then printing out error.
if len(George_word) != len(Barbie_list):
    print("Error!: The letters of both words are not exactly same.")
    exit()

# If George enters Empty word then printing out error.
elif len(George_word) == 0:
    print("Error!: George's word cannot be empty.")

# If Barbie Fails to form a word giving result: fake friendship.
elif len(Barbie_word) == 0:
    print("Result:")
    print("Their Friendship is Fake.")

# If length and letters of both the lists are equal-> giving result: True friendship.
if George_list == Barbie_list:
    print("Result:")
    print("Their Friendship is true.")

# In any other case giving result: fake friendship.
else:
    print("Result:")
    print("Their Friendship is Fake.")

print("-" * 80)
