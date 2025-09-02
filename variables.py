##DAY-2 Python Basics
my_var = "prakhar  "
print(my_var)

last_name ="Mishra"

x =10
print(my_var,x)

y= 5
print(x+y)

print(my_var + last_name)



## Multiple assignmentsx
a,b,c = 1,2,3
print(a,b,c)
x=y=z=99
print(x,y,z)

x= "10"
print(my_var + x)  # this will give error as we are trying to concatenate string with integer


total_sum = 10+20\
            +30+40
print(total_sum)

total_sum = (10+20+30+45)
print(total_sum)

# Explicit type casting - we have to tell the conversion type 
a=109
b="99"

b_new = int(b)

a_string = str(a)
print(b_new)

print(a_string)

print(type(a))
print(type(b_new))
print(type(a_string))

#Implicit type casting

a=10
b=10.5

print(type(a),type(b))

x = "Prakhar Mishra"
print(x[1])
print(x[0:4])

print(x[3:7])

print(x[:3])  


print(a+b) # int+float = float implicit type casting

x = "Prakhar Mishra"

print(x.lower())
print(x.upper())

print(x.capitalize())

print(x.replace("r","Seth"))

print(x.replace("Mishra","Seth"))

my_list = x.split(" ")
print(my_list)


file = "raw_data.csv"

if (file.endswith(".csv")):
    print("This is a csv file")


if (file.startswith("raw")):
    print("This is a RAW file")



statement  = "Hello prakhar what are you douing and prakhar is a good boy"

print(statement.count("prakhar"))

# is function

demo_str = "122abc"



print(demo_str.isnumeric())