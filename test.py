import os, datetime 

# Part 01

# 1 - check two numbers and return true if one of the number is 100 or if the sum of the two numbers is 100
def check_num_is_100():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if a == 100 or b == 100 or a + b == 100:
        print("True")
    else:  
        print("False")

# 2 - get the extension of a filename
def file_extension():
    file = input("Enter a filename: ")
    ext = os.path.splitext(file)
    print("File extension: " + ext[1])

# 3 - replace every character in a given string with the character following it in the alphabet
def replace_characters():
    char = input("Enter a character: ")
    new = []
    for i in char:
        uni = ord(i) + 1
        if i == 'z':
            new.append('a')
        else:
            new.append(chr(uni))
    print(''.join(map(str,new)))

# 4 - get the current date, expected output : mm-dd-yyyy, mm/dd/yyyy or dd-mm-yyyy, dd/mm/yyyy
def current_date():
    print(datetime.datetime.now().strftime('%d-%m-%Y'))

# 5 - create a new string adding "New!" in front of a given string
# If the given string begins with "New!" already then return the original string
def add_new():
    string = input("Enter a string: ")
    first = string.split()
    if first[0] == "New!":
        print(string)
    else: 
        print("New! " + string)

# Part 02

# 1 - create a new string from a given string taking the last 3 characters and added at both the front and back 
# The string length must be 3 or more, if not, the original string is returned.
def last_three_char():
    concat = input("Enter a string: ")
    if len(concat) <= 3:
        print(concat)
    else:
        new = concat[-3:]
        print(new + concat + new)

# 2 - extract the first half of a string of even length
def first_half():
    full = input("Enter a string: ")
    l = len(full)
    if l % 2 == 0:
        print(full[:int(l/2):])
    else: 
        print(full)

# 3 - concatenate two strings except their first character
def concat():
    a = input("Enter a string: ")
    b = input("Enter another string: ")
    print(a[1:] + b[1:])

# 4 - Given two values, find out which one is nearest to 100
def closest_hundred():
    a = int(input("Enter a value: "))
    b = int(input("Enter another value: "))
    if a < 100:
        c = 100 - a
    else: 
        c = a - 100
    
    if b < 100:
        d = 100 - b
    else: 
        d = b - 100
    
    if c < d:
        print(a)
    else: 
        print(b)

# 5 - check a given string contains 2 to 4 occurrences of a specified character
def check_specified():
    string = input("Enter a string: ")
    check = input("Enter a char: ")
    count = 0

    for i in string:
        if i == check:
            count += 1
        else:
            continue
    if count in range(2,5):
        print(check + " is repeated " + str(count) + " times")
    elif count not in range(2, 5):
        print(check + " is out of range")
    else: 
        print(check + " is not found")

check_specified()