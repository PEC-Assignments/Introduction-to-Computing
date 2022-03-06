from tkinter import *
from tkinter import messagebox
from tkinter.tix import *

# Assignment 5.




# Question 1.
"""Program to make a GUI-based GST Tax Finder Calculator."""


def calculation():
    """A function to calculate GST rate and total tax."""

    global original_cost, net_price, gst_rate, difference                                                               # Defining global variables for GST calculation.

    # If empty value is given, prompt an error window.
    if len(en1.get()) == 0 or len(en2.get()) == 0:
        messagebox.showerror("Error", "Error! : No value has been entered in Original Cost or Net Price.")

    else:
        # Creating an exception if any error occurs.
        try:
            original_cost = float(en1.get())
            net_price = float(en2.get())
            difference = net_price - original_cost
            gst_rate = (difference * 100) / original_cost                                                               # Calculating GST.

        except Exception as e:
            messagebox.showerror("Error", "Error! : " + str(e))                                                         # Prompting an error message if any error occurs.

        # If original cost is greater than net price prompting an error window.
        if original_cost > net_price:
            q = messagebox.askokcancel("Warning",
                                       "The value of Original Cost is given greater than Net Price.\
                                       Do you wish to continue?")

            # If user selects ok displaying the result.
            if q:
                lb3.config(
                    text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on Net Price : ₹{1:.2f}".format(
                        gst_rate,
                        difference))
                lb3.grid(row=3, columnspan=2, pady=10, ipady=10, ipadx=10)
            else:
                pass
        else:
            lb3.config(
                text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on Net Price : ₹{1:.2f}".format(
                    gst_rate,
                    difference))
            lb3.grid(row=3, columnspan=2, pady=10, ipady=10, ipadx=10)


root1 = Tk()

# Title and icon.
root1.title("Question 1")

try:
    root1.iconbitmap("PEC logo.ico")
except Exception as e:
    messagebox.showerror("Error", "Icon - \"PEC logo.ico\" not found.")

# Geometry.
root1.geometry('500x400')
root1.minsize(450, 370)
root1.maxsize(700, 450)

# Background Color.
root1['bg'] = 'grey'

# Heading.
Heading = Label(root1, text="GST Tax Finder Calculator", bd=5, font='Aerial 22 underline', bg='black', fg='white')
Heading.pack(pady=10, ipadx=10)

# Creating a frame.
f1 = Frame(root1, bd=20)
f1.pack()

# Content.
lb1 = Label(f1, text="Original Cost :", font="Arial 12")                                                                # Label 1.
lb1.grid(row=0, column=0, pady=10, ipadx=3)

tip1 = Balloon()                                                                                                        # tip1 for suggestion message.
tip1['bg'] = 'white'

en1 = Entry(f1, font="Arial 12")                                                                                        # Entry box 1.
en1.grid(row=0, column=1, pady=10)

tip1.bind_widget(en1, balloonmsg="Enter Original Cost (Integer or Float).")

lb2 = Label(f1, text="Net Price :", font="Arial 12")                                                                    # Label 2.
lb2.grid(row=1, column=0, pady=10)

tip2 = Balloon()                                                                                                        # tip2 for suggestion message.
tip2['bg'] = 'white'

en2 = Entry(f1, font="Arial 12")                                                                                        # Entry box 2.
en2.grid(row=1, column=1, pady=10)

tip2.bind_widget(en2, balloonmsg="Enter Net Cost (Integer or Float).")

tip3 = Balloon()                                                                                                        # tip3 for suggestion message.
tip3['bg'] = 'white'

bt1 = Button(f1, text="Calculate", command=calculation, cursor='hand2', font="Arial 12")  # Button 1
bt1.grid(row=2, columnspan=2, pady=10, ipadx=7)

tip3.bind_widget(bt1, balloonmsg="Click to calculate the result.")

lb3 = Label(f1, bg='grey', fg='white', font="Arial 12", bd=7, relief=GROOVE, borderwidth=4)                             # Label 3 (for displaying result)

root1.mainloop()




# Question 2.
'''Program to create a GUI-based Calendar application'''

import calendar


def calendar_():
    """Defining a function to Create a separate window to display the calendar."""

    global year                                                                                                         # Defining a global variable.

    try:
        int(en1.get())

    except Exception as e:
        if len(en1.get()) == 0:
            messagebox.showerror("Error", "Error! : No value has been entered for year.")
        else:
            messagebox.showerror("Error", "Error! : " + str(e))

    # Prompting Error if user enters no input.
    if int(en1.get()) <= 0:
        messagebox.showerror("Error", "Error! :  Year cannot be -ve or 0.")

    else:
        # Creating an exception if invalid integer is entered by the user.
        try:
            year = int(en1.get())                                                                                       # Getting value from entry box 1.

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Using calendar library to print the Calendar.
        cal = calendar.calendar(year)

        # Creating a different window to print Calendar
        top1 = Toplevel(root2)

        # Title and icon.
        top1.title(f"{year} Calendar")
        
        try:
            top1.iconbitmap("calendar.ico")
        except Exception as e:
            messagebox.showerror("Error", "icon - \"PEC logo.ico\" not found.")

        # Geometry.
        top1.geometry('640x620')
        top1.minsize(640, 630)
        top1.maxsize(640, 630)

        # Content.
        txt1 = Text(top1, relief=RIDGE, borderwidth=2, width=100, height=100)                                           # Text box 1.
        txt1.pack(padx=20, pady=10)

        txt1.insert('end', cal)                                                                                         # Inserting calendar string in Text box 1.

        top1.mainloop()


root2 = Tk()

# Title and icon.
root2.title("Question 2")

try:
    root2.iconbitmap("PEC logo.ico")
except Exception as e:
    messagebox.showerror("Error", "icon - \"PEC logo.ico\" not found.")

# Geometry
root2.geometry('400x300')
root2.minsize(350, 270)
root2.maxsize(500, 400)

# Background Color.
root2['bg'] = 'grey'

# Heading
Heading = Label(root2, text="Calendar Application", bd=5, font='Aerial 22 underline', bg='black', fg='white',
                relief=RAISED)
Heading.pack(pady=10, ipadx=10)

# Creating a frame.
f1 = Frame(root2, bd=20)
f1.pack(ipady=7, ipadx=30)

# Content
lb1 = Label(f1, text="Enter year :", font="Arial 14")                                                                   # Label 1.
lb1.pack(pady=5)

tip1 = Balloon()                                                                                                        # tip1 for suggestion message.
tip1['bg'] = 'white'

en1 = Entry(f1, font="Arial 14", width=18)                                                                              # Entry box 1.
en1.pack(pady=5)

tip1.bind_widget(en1, balloonmsg="Enter the year (Integer)")

tip2 = Balloon()                                                                                                        # tip2 for suggestion message.
tip2['bg'] = 'white'

bt1 = Button(f1, text="Show Calendar", command=calendar_, cursor='hand2', font="Arial 13")                              # Button 1.
bt1.pack(pady=10, ipadx=20)

tip2.bind_widget(bt1, balloonmsg="Click to show Calendar.")

root2.mainloop()




# Question 3.
'''Program to create a GUI-based calculator.'''


def btn(e):
    """Defining a function to perform functions
        when any of the button is pressed."""

    global val                                                                                                          # Defining a global variable.

    text = e.widget.cget("text")

    # If '=' button is pressed calculating the result.
    if text == "=":

        if val.get().isdigit():
            try:
                value = eval(val.get())
            except Exception as exp:
                messagebox.showerror("Error", "Error! : " + str(exp))
                value = "Error"
        else:
            try:
                value = eval(cal_screen.get())
            except Exception as exp:
                value = "Error"
                messagebox.showerror("Error", "Error! : " + str(exp))

        val.set(value)                                                                                                  # Setting the value of entry box to the result.
        cal_screen.update()                                                                                             # Updating the Entry box.

    # If 'C' button is pressed clearing the screen.
    elif text == 'C':
        val.set("")
        root3.update()

    else:
        val.set(str(val.get()) + str(text))
        cal_screen.update()


def equals(n):
    """Defining a function which calculates the
        result when user presses Enter."""

    # Same as '=' condition above.
    if val.get().isdigit():
        try:
            value = eval(val.get())
        except Exception as exp:
            messagebox.showerror("Error", "Error! : " + str(exp))
            value = "Error"
    else:
        try:
            value = eval(cal_screen.get())
        except Exception as exp:
            value = "Error"
            messagebox.showerror("Error", "Error! : " + str(exp))

    val.set(value)
    cal_screen.update()


root3 = Tk()

# Title and icon.
root3.title("Question 3")

try:
    root3.iconbitmap("PEC logo.ico")
except Exception as e:
    messagebox.showerror("Error", "icon - \"PEC logo.ico\" not found.")

# Geometry.
root3.geometry('500x650')
root3.minsize(425, 620)

# Background Color.
root3['bg'] = 'grey'

# Heading.
Heading = Label(root3, text="Calculator Program", bd=5, font='Aerial 22 underline', bg='black', fg='white',
                relief=RAISED)
Heading.pack(pady=10, ipadx=10)

# Content.
val = StringVar()                                                                                                       # val(a String variable for entry box)
val.set("")                                                                                                             # setting val's value to ""
cal_screen = Entry(root3, textvariable=val, font=" Aerial 30 bold", width=19)                                           # cal_screen - Entry box for calculator input.
cal_screen.pack(fill=X, padx=25)
cal_screen.bind('<Return>', equals)

tip1 = Balloon()                                                                                                        # tip1 for suggestions.

tip1['bg'] = 'white'

tip1.bind_widget(cal_screen, balloonmsg="Enter the value using keyboard or buttons below.")

f1 = Frame(root3, bg='LightYellow3')                                                                                    # Frame 1.
f1.pack(pady=10, fill=BOTH, padx=25, side=TOP)

# Creating Buttons.
bt1 = Button(f1, text="C", font="Aerial 25 bold", width=3)
bt2 = Button(f1, text="/", font="Aerial 25 bold", width=3)
bt3 = Button(f1, text="*", font="Aerial 25 bold", width=3)
bt4 = Button(f1, text="-", font="Aerial 25 bold", width=3)
bt5 = Button(f1, text=7, font="Aerial 25 bold", width=3)
bt6 = Button(f1, text=8, font="Aerial 25 bold", width=3)
bt7 = Button(f1, text=9, font="Aerial 25 bold", width=3)
bt8 = Button(f1, text="+", font="Aerial 25 bold", height=4, width=3)
bt9 = Button(f1, text=4, font="Aerial 25 bold", width=3)
bt10 = Button(f1, text=5, font="Aerial 25 bold", width=3)
bt11 = Button(f1, text=6, font="Aerial 25 bold", width=3)
bt12 = Button(f1, text=1, font="Aerial 25 bold", width=3)
bt13 = Button(f1, text=2, font="Aerial 25 bold", width=3)
bt14 = Button(f1, text=3, font="Aerial 25 bold", width=3)
bt15 = Button(f1, text="=", font="Aerial 25 bold", height=4, width=3)
bt16 = Button(f1, text=0, font="Aerial 25 bold", width=8)
bt17 = Button(f1, text=".", font="Aerial 25 bold", width=3)

# Grid Configuring.
Grid.columnconfigure(f1, 0, weight=1)
Grid.columnconfigure(f1, 6, weight=1)

# Griding all the buttons.
bt1.grid(row=0, column=1, padx=10, pady=10)
bt2.grid(row=0, column=2, padx=10, pady=10)
bt3.grid(row=0, column=3, padx=10, pady=10)
bt4.grid(row=0, column=4, padx=10, pady=10)
bt5.grid(row=1, column=1, padx=10, pady=10)
bt6.grid(row=1, column=2, padx=10, pady=10)
bt7.grid(row=1, column=3, padx=10, pady=10)
bt8.grid(row=1, column=4, columnspan=2, rowspan=2, padx=10, pady=10)
bt9.grid(row=2, column=1, padx=10, pady=10)
bt10.grid(row=2, column=2, padx=10, pady=10)
bt11.grid(row=2, column=3, padx=10, pady=10)
bt12.grid(row=3, column=1, padx=10, pady=10)
bt13.grid(row=3, column=2, padx=10, pady=10)
bt14.grid(row=3, column=3, padx=10, pady=10)
bt15.grid(row=3, column=4, columnspan=2, rowspan=2, padx=10, pady=10)
bt16.grid(row=4, column=1, columnspan=2, rowspan=2, padx=10, pady=10)
bt17.grid(row=4, column=3, padx=10, pady=10)

# Binding all the buttons to functions.
bt1.bind("<Button-1>", btn)
bt2.bind("<Button-1>", btn)
bt3.bind("<Button-1>", btn)
bt4.bind("<Button-1>", btn)
bt5.bind("<Button-1>", btn)
bt6.bind("<Button-1>", btn)
bt7.bind("<Button-1>", btn)
bt8.bind("<Button-1>", btn)
bt9.bind("<Button-1>", btn)
bt10.bind("<Button-1>", btn)
bt11.bind("<Button-1>", btn)
bt12.bind("<Button-1>", btn)
bt13.bind("<Button-1>", btn)
bt14.bind("<Button-1>", btn)
bt15.bind("<Button-1>", btn)
bt16.bind("<Button-1>", btn)
bt17.bind("<Button-1>", btn)

root3.mainloop()




print()

# Question 4.
'''Using quick sort algorithm to sort an array.'''

print("\n\tQUICK SORT ALGORITHM\n")


def quick_sort(arr, left, right):
    """Defining a function of quick sorting algorithm.

    arr = array which needs to be sorted
    left = leftmost index of the array
    right = rightmost index of the array"""

    # Using recursion for sorting an array using quick sort algorithm.
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

    else:
        pass


def partition(arr, left, right):
    """Defining a function for finding partition
        position in quick sort algorithm.

    arr = array which needs to be sorted
    left = leftmost index of the array
    right = rightmost index of the array"""

    i = left                                                                                                            # i = leftmost index
    j = right - 1                                                                                                       # j = rightmost index
    pivot = arr[right]                                                                                                  # taking pivot element as the rightmost index.

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]                                                                             # interchanging i and j elements.
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]                                                                         # interchanging i and pivot element.

    return i                                                                                                            # returning the sorted list.


while True:                                                                                                             # using while loop and exceptions to ensure correct input.
    try:
        no = int(input("Enter the number of students you want to enter :"))                                             # Asking the user for number of students.
        break
    except Exception as e:
        print(f"\nError! : {e}")                                                                                        # if any error occurs, printing it and taking input again.
        continue

input_arr = []                                                                                                          # Creating an array(list).

for n in range(1, no + 1):                                                                                              # Using for loop to take inputs from the user.

    if n == 1:                                                                                                          # Using conditional statements for finding the suffix.
        suffix = "st"
    elif n == 2:
        suffix = "nd"
    elif n == 3:
        suffix = "rd"
    else:
        suffix = "th"
    while True:                                                                                                         # using while loop and exceptions to ensure correct input.
        try:
            val = eval(input(f"\tEnter the Marks of {n}{suffix} student : "))                                           # Asking the user for marks of students.
            input_arr.append(val)                                                                                       # Appending the marks into the input_arr.
            break
        except Exception as e:
            print(f"\n\tError! : {e}")                                                                                  # if any error occurs, printing it and taking input again.
            continue

print("\nList entered by the user :", input_arr)

quick_sort(input_arr, 0, len(input_arr) - 1)                                                                            # Using the quick sort function to sort the list by user.

print("List after sorting is :", input_arr)

print("-" * 80)




# Question 5.
'''Sorting, binary search and counting occurrences of element.'''

print("\n\tBINARY SEARCH\n")


def binary_search(array, x):
    """Defining a function to search an element
        in an array using binary search algorithm.

        array - array from which element will be found.
        x - element which will be searched in the array"""

    lower = 0
    higher = len(array) - 1

    # using while loop to change the position of pointer until they meet each other.
    while lower <= higher:

        mid = (lower + higher) // 2                                                                                     # Finding middle element in the portion array.

        if array[mid] == x:                                                                                             # If middle element = required element returning it.
            return mid

        elif array[mid] < x:                                                                                            # if middle element < required element, changing lower value to mid+1.
            lower = mid + 1

        elif array[mid] > x:                                                                                            # if middle element > required element, changing higher value to mid-1
            higher = mid - 1

    return "not found"                                                                                                  # if element in not found in the array returning "not found"


while True:                                                                                                             # using while loop and exceptions to ensure correct input.
    try:
        arr = list(map(int, input("Enter the array (Enter values separated by space) : ").split()))                     # taking array input from user.
        break
    except Exception as e:
        print(f"\nError! : {e}")                                                                                        # if any error occurs, printing it and taking input again.
        continue

print()
print("Array entered by the user :", arr)

# part a.
'''sorting the array.'''

print("\n\tPart a : sorting the array\n")

arr.sort()                                                                                                              # Sorting the array.
print("Sorted Array :", arr)

# part b.
'''Using binary search to find an element in the array.'''

print("\n\tPart b : binary search\n")

while True:                                                                                                             # using while loop and exceptions to ensure correct input.
    try:
        fnd = int(input("Enter the number you want to find in the array : "))                                           # asking user for the element which needs to be searched.
        break
    except Exception as e:
        print(f"\nError! : {e}")                                                                                        # if any error occurs, printing it and taking input again.
        continue

element = binary_search(arr, fnd)                                                                                       # element = index of the element in the array.

print()
if element == "not found":
    print(f"Element {fnd} was NOT FOUND in given array.")                                                               # if element is not found in the array printing not found.
else:
    print(f"Element {fnd} was found at the index : {element}.")

# part c.
'''counting the occurrence of the element found above.'''
print("\n\tPart c : counting occurrences\n")

num = arr.count(fnd)                                                                                                    # finding number of occurrence using .count

print(f"Number of occurrences of element {fnd} is : {num}")

print("-" * 80)
