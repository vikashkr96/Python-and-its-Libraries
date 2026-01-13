# Create a list of 5 integers and print the list.
lst = [1 , 2 , 3 , 4 , 5]
print(lst)


# Write a Python program to calculate the sum of all elements in a given list.
lst = [1 , 2 , 3 , 4 , 50]
sums = 0
for ints in lst:
    sums+=ints
print(sums)


# Write a Python program to find the maximum and minimum values in a given list.
lst = [0 , 2 , -3 , 4 , 50]
max_num = max(lst)
min_num = min(lst)
print(f"Maximun number is: {max_num} \nMinimum number is: {min_num}")


# Given a list with duplicate values, write a Python program to remove duplicates and print the updated list.
lst1 = [2 , 4 , 3 , 2 , 4 , 8 , 6 , 2 , 3]
set1 = set(lst1)
new_lst = list(set1)
print(new_lst)


# Write a Python program to reverse a list without using the reverse() method.
lst2 = [1 , 2 , 3 , 4 , 50]
print(lst2[::-1])


# Create a 2D list (matrix) and print it row by row.
two_d_lst = [ [1,2,3,4] , [5,6,7,8] ]
print("Row 1 is: " , two_d_lst[0])
print("Row 2 is: " , two_d_lst[1])


# Write a program to find the sum of all elements in a 2D list.
lst = [ [1,2,3,4] , [5,6,7,8] ]
sum_row1 = sum(lst[0])
sum_row2 = sum(lst[1])
print(sum_row1 + sum_row2)

