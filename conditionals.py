# DAY-2 Python Basics
x = 910

# if (x==10):
#     print("x is 10")

# elif (x>100):
#     if((x>100) & (x<200) ):
#         print("Between 100 and 200")
#     else :
#         print("Greater than 200")

# else:
#     print("x is not 10")


# Loops-Used for iterations 

my_list =["apple","banana","grapes"]

# for i in my_list:
#     print(i)

# print(my_list)


# for i in range(1,101):
#     print(i)


m_list =["order","products","customers"]

for i in m_list:
    if i.lower()=="order":
         print("Table order")
    else:
            print("Not table order")


dem_list =["order","products","customers"]

for i in dem_list:
      print(i)
      for x in i:
            print(x)


one_list =["products","order","customers"]

for i in one_list:
      print(i)
      if (i.lower()=="order"):
            break 
      
print("-----------------")

two_list =["products","Order","customers"]

for i in two_list:
      if (i.lower()=="order"):
            continue
      print(i) 

# While loops - 
x = 1

while (x<11):
      print(x)
      x=x+1
      
 