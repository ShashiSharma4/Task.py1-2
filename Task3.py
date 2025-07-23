# Question---->>
# 1. define a function named factroial that takes a number as an argument and calculate its factroial using a loop recursion
# 2. Return tha calculated factorial
# 3.calls the function with a sample number and print the output

n=int(input("Enter a number"))
def factroil(n):
    if n<2:
        return 1
    else:
        return n*(factroil(n-1))
result=factroil(5)
print("Factroial of 5 is:",result)

# Question---->
#  WAPP that:
# 1. ASks the user for a number as input
# 2. Uses the math module to calculate the 
# Square root , Natural logarithm(log base e) of the number, sin of the number(in radian)

import math
a=int(input("Enter a number"))
if a<0:
    print("Square root , Lograithm, Sine")
else:
    sqrt_a=math.sqrt(a)
    log_a=math.log(a)
    sin_a=math.sin(a)
    print("Square root:",sqrt_a)
    print("Lograithm:",log_a)
    print("Sine:",sin_a)