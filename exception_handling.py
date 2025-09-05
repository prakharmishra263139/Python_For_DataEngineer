# Exception handling in Python

x = "10"
try:
    if(x>10):
        print("x is greater than 10")
    else :
        print("IDK")
except Exception as e:
    print(f"An error occurred - {e}" )

finally:
    print("i will always run ")

# finally - always executes 
# else - executes when there is no exception
# it makes sure that the code runs no matter what only after try and except block


