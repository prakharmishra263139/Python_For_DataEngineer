# static methods and class methods
# junk methods-they are not directly related to the object of the class


class  employee():
    # Inside class your variables will be called attributes
    # functions will be called methods
    
    company_name="XYZ"
    emp_name ="Prakhar Mishra"
    emp_dep = "IT"

    def __init__(self,emp_name,emp_dep):
        self.emp_name=emp_name
        self.emp_dep=emp_dep


    #  These are instance methods of the class related to their objects

    

    # self is used when you want to access attributes and methods of the class in python
    # self is a reference to the current instance of the class
    # self is used to access variables that belongs to the class


    # method to change the department of the employee
    
    def changes(self,new_company):
        employee.company_name = new_company

    @classmethod
    def changed(cls,new_company):
        cls.company_name = new_company
    def info(self):
        print(f"Employee {self.emp_name} works in {self.emp_dep} department in {self.company_name}")



    # and when u are mentinoing parameters in the method you have to mention self as the first parameter
    # then u have to pass the instance of the class when u are calling the method

    @staticmethod
    def addition(x,y): # when create static method no self is required
        print(x+y)


emp1 = employee("Priya","IT ")

emp1.addition(5,7) # static method called using class instance

emp1.changed("Copperpod AI Digital") 

print(emp1.company_name)# class method called using class instance