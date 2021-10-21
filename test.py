import os, datetime, random

# Part 01

# 1 - check two numbers and return true if one of the number is 100 or if the sum of the two numbers is 100
def check_num_is_100():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if a == 100 or b == 100 or a + b == 100:
        return True
    else:  
        return False

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

# Part 03

# 1 - find the number of even digits in a an array of integers
def even_digits():
    digits = input("Enter a number: ")
    count = 0
    for i in digits:
        if int(i) % 2 == 0:
            count += 1
    print(count)

# 2 - find the number of even values up to a given number
def even_numbers_upto():
    digit = input("Enter a number: ")
    count = 0
    for i in range(1,int(digit)):
        if int(i) % 2 == 0:
            count += 1
    print(count)

# 3 - check whether a given array of integers is sorted in ascending order
def sort_check():    
    integer = list(map(int,input("Enter an array of integers: ").strip().split()))
    integer1 = sorted(integer)
    if integer1 == integer: 
        print("Sorted")
    else: 
        print("Not sorted")

#  4 - get the largest even number from an array of integers.
def sort_check():    
    integer = list(map(int,input("Enter an array of integers: ").strip().split()))
    j = 0
    for i in integer:
        if int(i) % 2 == 0 and i > j:
            j = i
        else: 
            continue
    print(j)

# 5 - replace the first digit in a string (should contain at least one digit) with a $ character
def replace_first_digit():
    string = list(input("Enter a string with atleast one numeric character: "))
    for i in string: 
        if i.isdigit():
            string[string.index(i)] = "$"
            break
        else: 
            continue
    print(''.join(map(str,string)))

# Part 04

# 1 - Given a year, report if it is a leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    if year % 4 != 0:
        print('Not Leap year')
    elif year % 100 == 0 and year % 400 != 0:
        print("Not Leap year")
    else: 
        print("Leap year")

# 2 - compare two objects to determine if the first one contains the same properties as the second one (which may also have additional properties) 
# For example, objA and objB are equal (but not equal to objC)
# const objA = { a: 1, b: 1, c: 1 }; 
# const objB = { a: 1, b: 1, c: 1 }; 
# const objC = { a: 1, b: 1, d: 1 };
def compare_two_obj():
    objA = { 'a': 1, 'b': 1, 'c': 1 }
    objB = { 'a': 1, 'b': 1, 'c': 1 } 
    objC = { 'a': 1, 'b': 1, 'd': 1 }
    objects = [ objA, objB, objC]
    
    for i in range(0,len(objects)):
        if i == len(objects) - 1:
            if objects[0] == objects[-1]:
                print("Objects are equal")
            else:
                print("Objects are not equal")
        elif objects[i] == objects[i+1]:
            print("Objects are equal")
        else:
            print("Objects are not equal")

# 3 - convert a comma-separated values (CSV) string to a 2D array. 
# A new line indicates a new row in the array. Example input:
# abc,def,ghi 
# jkl,mno,pqr
# stu,vwx,yza
def csv():
    csv = list(input("Enter comma-separated values: ").split(','))
    newcsv=[]
    for i in csv:
        if i != "\\n":
            newcsv.append(i)
        else:
            print(newcsv)
            newcsv = []
    print(newcsv)

# 4 - generate a random hexadecimal color code
def hex_color():
    chars = '0123456789ABCDEF'
    print("Random Color: " + ''.join(random.sample(chars,6)))
    
# 5 - returns true if the provided predicate function returns true for all elements in a collection, false otherwise
def return_true():
    if check_num_is_100() is True:
        print("True")
    else:
        print("False")

# Part 05

#  1 - return passed string with letters in alphabetical order. Example string: 'webmaster' Expected Output: 'abeemrstw'
def alphabetical():
    print("".join(sorted(input("Enter a string: "))))

# 2 - accept a string as a parameter and counts the number of vowels within the string
def vowels():
    string = input("Enter a string: ")
    vow = 'aeiou'
    count = 0
    for i in string:
        if i in vow:
            count += 1
    print(count)

# 3 - convert an amount to coins. 
# Example input: 46 and possible coins 25, 10, 5, 2, 1 Output: 25, 10, 10, 1
def greedy_coins():
    amount = int(input("Enter an amount: "))
    denomin = input("Enter comma separated values: ").split(',')
    coins = sorted(map(int,denomin),reverse=True)
    output = []
    i = 0
    while amount != 0:
        if amount >= int(coins[i]):
            amount -= int(coins[i])
            output.append(coins[i])
        else:
            i += 1
    print(','.join(map(str,output)))

# 4 - extract unique characters from a string
def unique_characters():
    string = input("Enter a string: ")
    print("Unique Characters: "+','.join(sorted(set(string))))

# 5 - first not repeated character Example string: 'abacddbecf' Expected output: 'e'
def non_repeat_char():
    string = list(input("Enter a string: "))
    new = []
    for i in string:
        if i not in new:
            new.append(str(i))
        else:
            new.remove(str(i))
    print(new[0])

