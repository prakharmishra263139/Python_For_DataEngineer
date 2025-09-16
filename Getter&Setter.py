# getter and setter in python
# getter is used to get the value of a private attribute
# setter is used to set the value of a private attribute


class  employee():
    
    company_name="XYZ"
    emp_name ="Prakhar Mishra"
    emp_dep = "IT"

    def __init__(self,emp_name,emp_dep):
        self.emp_name=emp_name
        self.emp_dep=emp_dep
    
    # This is getter  
    @property #getter
    def info(self):
        print(f"Employee {self.emp_name} works in {self.emp_dep} department in {self.company_name}")


    @info.setter  # setter
    def info(self, new_empdetails):
        new_empname = new_empdetails[0]
        new_dep = new_empdetails[1]

        self.emp_name = new_empname
        self.emp_dep = new_dep

   

    @classmethod
    def changed(cls,new_company):
        cls.company_name = new_company

    @staticmethod
    def addition(x,y): # when create static method no self is required
        print(x+y)

# This is setter
    # def changeinfo(self, new_name,new_dep):
    #     self.emp_name = new_name
    #     self.emp_dep = new_dep


emp1 = employee("Priya","IT ")
# emp1.changeinfo("Ankita","HR")
# emp1.info()

# calling getter and setter

# print(emp1.info) # getter called treate as attribute

emp1.info = ["Aonkit","HR"] # setter called treate as attribute
print(emp1.info) # getter called treate as attribute

