# WAPP that :
# 1:- Take an integer input from the user.
# 2:- Checks Whether the number is even and odd using if else statement.

a=int(input("Enter a number:"))
if (a%2==0):
    print(f" {a} Even Number.")
else:
    print(f" {a} Odd Number.")

#####Question 2. WAPP That:
# 1. Uses s for loop to iterate over numbers from 1 to 50
# 2.Calculate the sum of all integers in this range.
# 3. display the final sum.

a=0
for i in range(1,51):
    a+=i
    print("The sum of numbers from 1 to 50:",a)