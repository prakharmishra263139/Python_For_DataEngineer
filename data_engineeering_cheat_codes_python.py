s = 'data engineering'
lst  =[10, 20, 30, 40, 50]

print(len(s)) # length of string
print(len(lst)) # length of list

# type in python
print(type(s)) # type of string
print(type(lst)) # type of list

# range in python 
print("Range from 1 to 10",list(range(10))) # range from 0 to 9
print("Range from 1 to 10",list(range(0,10,3)))     # range from 1 to 10 with gap of 3

# print with fromatting 
a,b = 5,7
print(f"The value of a is {a} and value of b is {b}") # formatted string

# name = input("Enter your name :")
# print("Hello,",name) 

number  = [1,2,3,4,5]
print("The numbers are :",sum(number))

unsorted_list = [5,3,6,2,10,1]
print("Sorted list is :",sorted(unsorted_list))

print("Sorting string of fruits :",sorted(['banana','apple','mango','kiwi']))


# generrator in python
# real life example , we have a list of 1000 students and we want to send email to each student
# we can use generator to send email one by one instead of loading all students in memory

# def student_generator(num_students):
#     for i in range(1, num_students + 1):
#         yield f" Student {i}"

# students = student_generator(1000)

#  zip is used to combine two lists into a list of tuples
# real life example , we have two lists of student ids and names and we want to combine them into a list of tuples

ids =[101,102,103,104,105]
name = ["Alice","Bob","Charlie","David","Eva"]

print("list zip-->id names",list(zip(ids,name))) # zip function to combine two lists


# enumerate
# enumerate is used to get the index and value of a list

for i,val in enumerate(name):
    print(f"Index : {i} is->: {val}")


# Recursion in python
# real life example , we want to calculate factorial of a number using recursion

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(6))

# Data manipulation in pandas

import pandas as pd

# 1) Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Cathy", "Dan"],
    "Age": [25, 30, 22, 28],
    "Salary": [50, 60, 52, 58]
}

df = pd.DataFrame(data)
print("Data frame",df)

# head & info
print("First 2 row",df.head(2))

# print(df.info())

# print(df["Salary"])

print("\nPeople with Age > 25:\n", df[df["Salary"] > 55])

df["Bonus"] = df["Salary"]*5
print("\nPeople bonus:\n",df["Bonus"])

# group by mainly works for 
print("Avegerae salary ",df.groupby("Age")["Salary"].mean())

print("Sort by descending ",df.sort_values(by="Salary",ascending=False))