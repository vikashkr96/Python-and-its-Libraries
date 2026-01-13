print('mini calculator')

num_1 = int(input('Enter number 1 = '))
num_2 = int(input('Enter number 2 = '))
choice = input('Enter choice + - * / = ')

if choice == '+':
    print('sum = ' , num_1 + num_2)
elif choice == '-':
    print('sum = ' , num_1 - num_2)
elif choice == '*':
    print('product = ' , num_1 * num_2)
elif choice == '/':
    print('quotient = ' , num_1 / num_2)

else:
    print('invalid')

