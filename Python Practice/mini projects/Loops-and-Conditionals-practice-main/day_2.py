# Write a Python program to take an integer N and calculate the sum of the first N natural numbers using a for loop.
n = int(input("Enter a number: "))
if n >= 0:
    result = 0
    for i in range(0,n+1):
        result += i
    print("The sum of all the numbers up to n is: ",result)
else:
    print('Please Enter a positive number!!')


# Write a Python program that takes an integer as input and prints its multiplication table up to 10 using a for loop. 
a = int(input("Enter a number: "))
for i in range(1,11):
     table = a*i
     print(f"{a} * {i} = {table}")


# Write a Python program that takes an integer N and prints all numbers from 1 to N using a while loop.
num = int(input('Enter a number: '))
i = 1
while i <= num:
    print(f"{i}")
    i += 1


# Write a Python program that takes an integer as input and prints its reverse using a while loop.
n = int(input("Enter a number: "))
rev = 0 
while n > 0:
    rev = (rev * 10)+ (n % 10)
    n = n // 10
print("Reversed number is: ",rev)



# Write a Python program to generate the first N Fibonacci numbers using a while loop.
num = int(input("Enter the number: "))
a = 0 
b = 1
if num >= 1:
    if num == 1:
        print(1)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c = a+b
            a = b 
            b = c 
            print(c)
else:
    print('Enter a positive number !!')



# Write a Python program that takes an integer as input and checks if it is prime or not using a loop.
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is not a prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")