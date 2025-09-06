# list comprehension
my_list = [1,2,3,4,5,6]

new_list = [i*i for i in my_list if (i%2)==0 if (i!=6)]
print(new_list)

# Dictionary data structure

my_dictionary ={"x":1, "y":2, "z":3}
print(my_dictionary)

my_dictionary["x"]=10

my_dictionary.pop("z")
print(my_dictionary)


print(my_dictionary.keys())
print(my_dictionary.items())


my_var ={"x":1, "y":2, "z":3,"demo":{"a":1,"b":2,"c":3}}
print(my_var['demo'])


# Sets data structure

a = {1,2,3,4,5,5,5,5,5}
print(a)

b = {1,2,3,4,5,6,7,8,9}

print(a.union(b))

print(a.intersection(b))

# Empty dictinonary
my_dict = {}
print(type(my_dict))

st = set()
print(type(st))

# Tuple data structure
my_tup = (1,2,3,4,5)
print(my_tup)

my_tuplist =list(my_tup)
print(my_tuplist)

my_tup =tuple(my_tuplist)
print(my_tup)