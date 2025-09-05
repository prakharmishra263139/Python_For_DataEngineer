# Functions in Python are defined using the 'def' keyword.

x = 9
def  my_fucn(p_x):
    
    if(p_x>10):
        print("x is greater than 10")
    else :
        print("IDK")

    return p_x

returned_value = my_fucn(22)
print(returned_value)


# my_fucn(22)
# my_fucn(2)

# x = 11
# my_fucn()


def my_func2(p_x, p_y=33):
    print(p_x,p_y)

my_func2(10)   


def my_fun2(*p_x):
    print(p_x)

my_fun2(1,2,3,4,5,6,7,8,9)


# *p_x is used to pass a variable number of arguments to a function.
# It allows you to pass a variable number of non-keyword arguments to a function.
# * means "pack" the arguments into a tuple. 

def my_fun3(**p1_x):
    print(p1_x,type(p1_x))
    print(p1_x.keys())

my_fun3(x=20, y=30, z=40)


# Lambda functions

def my_func4(p_x):
    return p_x + 10
print(my_func4(5))
# Lambda function equivalent
my_lambda = lambda p_x: p_x + 10
print(my_lambda(5))

# Lambda functions are used for creating small, anonymous functions.
# They are often used for short, throwaway functions that are not reused elsewhere in the code
# They can take any number of arguments but can only have a single expression.  
# They are syntactically restricted to a single expression.


