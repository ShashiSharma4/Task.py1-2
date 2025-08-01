# WAPP That:
# 1.Create a dictionary where student names are keys and their marks are values 
# 2.Asks the users to input a students name 
# 3.Retrives and display the corrosponding marks
# 4.if the student name is not found display an appropriate massage


student={"Alice":85,"john":90,"tom":80}
stud=input("Enter the student's name:")
if stud in student:
    print(f"{'ALice'}'s marks: {student[stud]}")
else:
    print("Student not found")



# WAPP that:----.
# 1. Create a list of number from 1 to 10
# 2. Extrracts the forst five elements from the list.
# 3.prints boths extracted list and the reversed list.

list=[1,2,3,4,5,6,7,8,9,10]
print("Original list:",list)
first_five =list[:5]
reverse_five=list[::-1]
print("Extracted first five element",first_five)
print("Reverse extrected element",reverse_five[5:10])