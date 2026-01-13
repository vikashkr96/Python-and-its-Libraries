# Given a 2D list (matrix), write a program to transpose it.
A = [[1,2,3],
     [4,5,6]]

T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]
for i in T:
    print(i)


# Write a one-liner to generate a list of squares of numbers from 1 to 10.
sqr = [x**2 for x in range(1,11)]
print(sqr)


# Given a list, use list comprehension to create a new list containing only the even numbers.
lst = [11,32,34,65,76,89,78,45,44,64,38,87,88,30,10]
new_lst = []
for x in lst:
    if x % 2 == 0:
        new_lst.append(x)
print(new_lst)


# Create a dictionary with student names as keys and their scores as values. Print the dictionary.
dict = {'vikaskh':87 , 'nikhil':89 , 'deepak':90 , 'palak':100 }
print(dict)


# Write a Python program to check if a given key exists in a dictionary. 
dict = {
    'name':'vikash',
    'age':19,
    'city':'Motihari',
    'state':'bihar'
                      }
key_check = input("Enter the key to check: ")
if key_check in dict:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")



# Write a program to merge two dictionaries into one. 
dict1 = {'name':'vikash','age':19}
dict2 = {'city':'Motihari','state':'bihar'}
dict1.update(dict2)
print(dict1)


# Create a nested dictionary storing students' names and their respective marks in different subjects.
students_marks = {
    'vikash': {
        'Math': 85,
        'Science': 90,
        'English': 88  } ,
    'nikhil': {
        'Math': 78,
        'Science': 82,
        'English': 80  } ,
    'nasir': {
        'Math': 92,
        'Science': 95,
        'English': 91  } 
}
for student_name , marks in students_marks.items():
    print(f"{student_name} : {marks}")


# Print the nested dictionary
print("Students' Marks:")
for student, marks in students_marks.items():
    print(f"{student}: {marks}")

# Write a one-liner to generate a dictionary containing numbers from 1 to 5 as keys and their squares as values.
dic = {a:a**2 for a in range(1,6)}
print(dic)


# Convert a list into a set to remove duplicate values.
lst = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
set1 = set(lst)
print(set1)


# Write a Python program to find the union and intersection of two sets.
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {6,7,8,9,10,11,12,13,14,15}
set_union = set1.union(set2)
set_intersection = set1.intersection(set2)
print("The union of set1 and set2 is :",set_union)
print("The union of set1 and set2 is :",set_intersection)

# Convert a tuple into a list, add an element, and convert it back into a tuple.
tup = (1,2,3,4,5,6,7,8,9,10)
lst = list(tup)
lst.append(11)
final_tup = tuple(lst)
print(tup)
print(final_tup)


# Explain when to use a list and when to use a tuple.
 # Ans:-
         # we use list when we need a mutable collection that can change in size and content . 
         # we use a Tuple when you need an immutable collection that should remain constant throughout the program.
