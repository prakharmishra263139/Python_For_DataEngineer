x =100 # global variable 

def my_func():
    global x  # accessing global variable
    x=5 # local value of x
    print(x)

my_func()

y=10
def my_func1():
    global y  # accessing global variable
    # y=5 # local value of x
    print(y)

my_func1()




#----------------------

# x =99
# if(x<100):
#     raise ValueError("x should not be less than 100")


# Enumerate function 


my_list = [100,200,300,400,500]

for i,x in enumerate(my_list):
    print(i,x)