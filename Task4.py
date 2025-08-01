# WAPP  
# 1. open and reads a text file named sample.txt.
# 2. print its content line by line.
# 3. Handles errors gracefully  if the file does not exist.

try:
    with open("sample.txt","r") as file:
        for line in file:
            print(line.strip())
        
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

file1=open("sample.txt","r")
read_file=file1.read()
print(read_file)
file1.close()

# WAPP that:-
# 1.Take user input and write it to a file named output.txt
# 2.Append additional data to the same file.
# 3.Read and display the filnal content of the file .
 
a=input("Enter text to write to the file:")
with open ("output.txt","w") as file:
    file.write(a)

b=input("Enter additional text to append:")
with open("output.txt","w") as file:
    file.write(b)

# print("final contant:")
with open("output.txt","r") as file:
    content=file.read()
    print(content)