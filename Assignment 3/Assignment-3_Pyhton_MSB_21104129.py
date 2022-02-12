# Assignment 3.


# Question 1.
"""Counting Occurrences of character/substring in a given string."""

print("\n\tOccurrence Counter\n")

original_string = input("Enter the String:")
print()

# Assigning the original string to a variable.
input_string = original_string.lower()

# Condition to check if the string entered is single word or sentence.
if " " in input_string:
    input_string = input_string.split()

# Checking if the string entered is empty.
elif len(input_string) == 0:
    print("Empty String Has been Entered")

# Counting the occurrences using .count function.
output_set = []
for i in input_string:
    count = input_string.count(i)
    output_set.append(f"Occurrences of {i} in \"{original_string}\": {count}\n")

# Removing the repetitive outputs using a set.
output_set = set(output_set)
for j in output_set:
    print(j)

print("-" * 80)


# Question 2.
'''Program to find the next date.'''


def is_leap(y):
    # Function to find if the given year is a leap year.
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False

    return leap


print("\n\tNext Date Finder.\n")

day = int(input("Enter the Day:"))
month = int(input("Enter the Month:"))
year = int(input("Enter the year:"))

if month < 1 or month > 12:
    print("\nError!: Date entered is out of range.")
    exit()

elif day < 1 or day > 31:
    print("\nError!: Date entered is out of range.")
    exit()

elif year < 1800 or year > 2025:
    print("\nError!: Date entered is out of range.")
    exit()

output_day = day
output_month = month
output_year = year

# Using If-Else Statements to find the next date.
if month in [1, 3, 5, 7, 8, 10]:
    if day == 31:
        output_day = 1
        output_month += 1
    else:
        output_day += 1

elif month in [4, 6, 9, 11]:
    if day == 30:
        output_day = 1
        output_month += 1
    else:
        output_day += 1

elif month == 12:
    if day == 31:
        output_day = 1
        output_month = 1
        output_year += 1

elif month == 2:
    if is_leap(year):
        if day > 29:
            print("\nError!: Date entered is out of range.")

        elif day == 29:
            output_day = 1
            output_month += 1
        else:
            output_day += 1
    else:
        if day > 28:
            print("\nError!: Date entered is out of range.")

        elif day == 28:
            output_day = 1
            output_month += 1
        else:
            output_day += 1

output_date = f"{output_day}/{output_month}/{output_year}"
print("\nThe next Date is :", output_date)

print("-" * 80)


# Question 3.
'''Program to create a list of tuples with the first element as the number and Second Element as the square of the 
number. '''

print("\n\tTuple of squares maker.\n")

numbers = input("Enter the list of numbers(Enter the numbers separated by space):")

# Converting the input entered by the user into a list of containing integer datatypes using map function.
chr_lst = list(map(int, numbers.split()))

output_list = []
for i in chr_lst:
    output_list.append((i, i ** 2))

print()
print(output_list)

print("-" * 80)


# Question 4.
'''Program to find grade and performance.'''

print("\n\tGrade Calculator.\n")

grade_point = int(input("Enter the Grade Point:"))

if grade_point < 4 or grade_point > 10:
    print("Error!: Input is out of range.")
    exit()

else:
    # Creating a dictionary containing the grades and performances.

    student_details_dict = {4: ['D', 'Poor'], 5: ['C', 'Below Average'], 6: ['C+', 'Average'], 7: ['B', 'Good'],
                            8: ['B+', 'Very Good'],
                            9: ['A', 'Excellent'], 10: ['A+', 'Outstanding']}

    print(f"\nYour Grade is {student_details_dict[grade_point][0]}"
          f", and Performance is {student_details_dict[grade_point][1]}")

print("-" * 80)


# Question 5.
'''Program to print a following pattern.'''

print("\n\tPattern Printer.\n")

# Creating a list of characters from A to B.
chr_lst = [chr(j) for j in range(ord('A'), ord('K') + 1)]

# Printing out the pattern by using .join and .center command.
while len(chr_lst) > 1:
    print((''.join(chr_lst)).center(11, ' '))
    chr_lst.pop(-1)
    chr_lst.pop(-1)

# Printing out the last line of the pattern outside the loop.
print((''.join(chr_lst)).center(11, ' '))

print("-" * 80)


# Question 6.
'''Program to add student details in a dictionary and performing operations on that dictionary.'''

print("\n\tStudent Details Manager\n")


# Defining a function to repeatedly take inputs into a dictionary.
def dict_adder(d):
    key = int(input("Enter the SID:"))
    value = input("Enter the name:")
    d[key] = value


# Creating an empty dictionary.
student_details_dct = {}

# Using While loop to take inputs into a dictionary repeatedly.
ans = 'y'
while ans == 'y':
    dict_adder(student_details_dct)

    ques = input("\nDo you want to enter another value?[y/n]:")

    # If user enters 'y' the loop continues.
    if ques == 'y':
        ans = 'y'
    elif ques == 'n':
        break
    else:
        print("\nError!:only y/n should be entered.")
        exit()

# Part a.
'''Printing out all the details of the students entered in the dictionary.'''

print(f"\nStudent Details stored in dictionary:")
print("SID\t\t\tNames")
print('-*'*20)
for k in student_details_dct:
    print(f"{k}\t\t{student_details_dct[k]}")

# Part b.
'''Sorting the Dictionary according to names.'''

# Using sorted() function to sort the dictionary.
dict_sortedbynames = {k: v for k, v in sorted(student_details_dct.items(), key=lambda v: v[1])}
print()
print(dict_sortedbynames)

# Part c.
'''Sorting the Dictionary according to SIDs.'''

# Using sorted() function to sort the dictionary.
dict_sortedbySID = {k: v for k, v in sorted(student_details_dct.items())}
print()
print(dict_sortedbySID)

# Part d.
'''Searching the details of the students using SID.'''

find = int(input("\nEnter the SID which you want to search:"))

if find in student_details_dct.keys():
    print(f"Name of the student with SID:{find} is: \"{student_details_dct[find]}\"")
else:
    print(f"Error! {find} not found in the record.")

print("-" * 80)


# Question 7.
'''Program to print Fibonacci sequence and it's average.'''

print("\n\tFibonacci Sequence Printer.\n")


# Function to find the nth term of fibonacci sequence.
def fibonacci_term(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n <= 0:
        return "\nError!: Number of terms can not be -ve or 0."
    else:
        return fibonacci_term(n - 2) + fibonacci_term(n - 1)


# Function to print first n terms of  fibonacci series.
def fibonacci_sequence(no):
    sequence_list = []
    for t in range(1, no + 1):
        sequence_list.append(fibonacci_term(t))

    return sequence_list


num = int(input("Enter the number of terms of fibonacci sequence you want:"))

print(f"\nFirst {num} terms of fibonacci sequence are:", end=' ')

for i in fibonacci_sequence(num):
    print(i, end=' ')

# Finding out the average of the printed our fibonacci series.
avg = sum(fibonacci_sequence(num)) / len(fibonacci_sequence(num))
print(f"\nThe average of the resultant fibonacci series is: {avg}")

print("-" * 80)


# Question 8.
'''Program to perform some operations on Sets.'''

print("\n\tSet Operations.\n")

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

print("Given sets:-")
print("Set1-", Set1)
print("Set2-", Set2)
print("Set3-", Set3)
print()
# Part a.

Set_a = Set1 ^ Set2
print("Set of all elements that are in Set1 and Set2 but not both:", Set_a)
print()

# Part b.

Set_b = (Set1 - (Set2 | Set3)) | (Set2 - (Set1 | Set3)) | (Set3 - (Set1 | Set2))
print("Set of all elements that are in only one of the three sets:", Set_b)
print()

# Part c.

Set_c = (Set1 & Set2) | (Set2 & Set3) | (Set1 & Set3) - (Set1 & Set2 & Set3)
print("Set of elements that are exactly two of the sets Set1, Set2, Set3:", Set_c)
print()

# Part d.

Set_d = {i for i in range(1, 11)} - Set1
print("Set of all integers in the range 1 to 10 that are not in Set1:", Set_d)
print()

# Part e.

Set_e = {i for i in range(1, 11)} - (Set1 | Set2 | Set3)
print("Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:", Set_e)
print("-" * 80)
