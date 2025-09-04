my_list = [1,2,'Ansh','Lamba']
print(my_list)

# print(my_list[4][0])

# print(my_list[0:4])

print(my_list[-3:])


print(my_list[::3])

my_list.append("Prakhar Mishra")

print(my_list)

my_list.pop()
print(my_list) 



num_list = [1,2,3,4,5,6,7,8,9,10]

# Reverse the list using a for loop
reversed_list = []
for i in range(len(num_list)-1, -1, -1):
    reversed_list.append(num_list[i])

# print(reversed_list)

# print(num_list[::-1])

num_list.reverse()
print(num_list)


new_list = []

for i in num_list:
    new_list.append(i*i)
print(new_list)
 