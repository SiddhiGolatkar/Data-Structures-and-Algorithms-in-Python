
# single line to find factorial

def factorial(n):

    return 1 if (n==1 or n==0) else n * factorial(n-1)

num = 5
print("Factorial of" ,num, "is", factorial(num))

num = int(input("enter a number: "))
print("Factorial of" ,num, "is", factorial(num))

