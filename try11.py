#!/usr/bin/python3

while True:
    try:
        print("Let's div x by y!")
        x = int(input("What is the value of x? "))
        y = int(input("What is the value of y? "))
        print("The value of x/y is:", x/y)
    except ZeroDivisionError:
        print("Something went wrong with those maths...restarting.")
    except Exception as err:
        print(err)


