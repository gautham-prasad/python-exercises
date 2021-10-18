import os

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
