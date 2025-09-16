# Inheritance in Python
# A class can inherit attributes and methods from another class
# real life example - a dog is an animal
# so dog class can inherit from animal class

class company(): # Parent class -1 
    # single level inheritance 
    def __init__(self, com_name):
        self.com_name = com_name
        

    def company_info(self):
        print(f"Company Name is {self.com_name}")
        
# Parent class -2
class country():
    
    def __init__(self,country_name):
        self.country_name=country_name;
        
    def country_info(self):
        print(f"Country name is{self.country_name}")

# child  class -3
class employee(company,country):

    def __init__(self,emp_name,com_name,country_name):
        self.emp_name = emp_name
         
        company.__init__(self,com_name)
        country.__init__(self,country_name)
        # self.com_name = com_name

    
    def full_info(self):
        print(f"The employee {self.emp_name} lives in {self.country_name} and works for {self.com_name}")
            
        
    def emp_infochild(self):
        print("This is runnig from employee")
        # company.company_info(self) # same for single , multiple level inheritance 
        
        # super().company_info() # good for single level
        
        company.company_info(self)
        country.country_info(self)
        


emp1 = employee("Rahul","XYZ","USA")

# emp1.company_info()
# emp1.emp_info()

# emp1.emp_infochild()

emp1.full_info()

emp1.emp_infochild()
