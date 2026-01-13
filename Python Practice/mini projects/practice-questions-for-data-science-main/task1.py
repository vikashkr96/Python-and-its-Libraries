# practice questions python (data science)

# Write a Python program that takes two numbers as input from the user, stores them in variables, and prints their sum.
a = int(input("Enter the first number:- "))
b = int(input("Enter the second number:- "))
total = a+b
print("sum is ",total)

# Given a string num_str = "25", convert it into an integer and a float, then print their sum.
num_str = "25"
num_f = float(num_str)
num_i= int(num_str)
sum = num_f + num_i
print(sum)

# Write a Python program to take two numbers as input and display their: a. Sum , b. Difference c. Product , d. Quotient 
a = int(input("Enter the first number:- "))
b = int(input("Enter the second number:- "))
print("Sum= ",a+b)
print("Difference= ",a-b)
print("Product= ",a*b)
print("Quotient= ",a/b)

# Given a string text = "hello world", write a Python program to: a. Convert it to uppercase , change Hello to Hi 
text = "hello world"
new_text1 = text.upper()
print(new_text1)

new_text2 = text.replace("hello" , "Hi")
print(new_text2)
