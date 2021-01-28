# To take input from the user

num = int(input("enter a number: "))

factorial = 1

# check if the number is negative, positive or zero

if num < 0:
    print("sorry, factorial does not exist for negative numbers")

elif num == 0:
    print("The factorial of zero is 1")

else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("The Factorial of", num ,"is", factorial)