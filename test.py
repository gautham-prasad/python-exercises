# check two numbers and return true if one of the number is 100 or if the sum of the two numbers is 100
def check_num_100():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    if a == 100 or b == 100 or a + b == 100:
        print("True")
    else:  
        print("False")

