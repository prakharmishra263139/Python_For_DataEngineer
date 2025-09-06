class  employee():

    # Inside class your variables will be called attributes
    # functions will be called methods
    

    emp_name ="Prakhar Mishra"
    emp_dep = "IT"


    # self is used when you want to access attributes and methods of the class in python
    # self is a reference to the current instance of the class
    # self is used to access variables that belongs to the class


    def info(self):
        print(f"Employee {employee.emp_name} works in {employee.emp_dep} department")
        
    # and when u are mentinoing parameters in the method you have to mention self as the first parameter
    # then u have to pass the instance of the class when u are calling the method
    
emp1 = employee()

employee.info(emp1)
