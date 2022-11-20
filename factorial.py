num1 = int(input("Enter a number: "))
factorial = 1
if num1 < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num1 == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num1 + 1):
        factorial = factorial * i
    print("The factorial of",num1,"is",factorial)
