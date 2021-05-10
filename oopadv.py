#python is a object oriented programming language and it provides flexibility to code
#properties states for variables
#class=general car sketch()
#fuel_calculator()
#check_engine()
#door_is_open_check()
#fuel_status()

# example to create a car
# (The_init_()function)
#class keyword used to create classes
#file of python is known as module
#class is a top hirarchy parent of method and method is parent of variable
#first we declare class then method and then variable
#classes woulb be written in capital letters mesnt inside class use captial letters and space or underscore use


class CarClass:
    year=2000
    print(year)

#instance of an object


class CarClass:
    year=2000
    print(year)

    audi_a3=CarClass()
    ford_focus=CarClass()

print('*************************************************************************************')
class Employee:
    def __init__(self,name,salary,attendance):#self is a properties
        self.name=name
        self.salary=salary
        self.attendance=attendance
    def attendacne_check(self):
        print('' +self.name+',attendance '+ 'status is :' + str(self.attendance))#+ is used to make spaces
    def employee_details (self):
        print('name :' ,self.name,'salary:',self.salary )

sara= Employee('sara',30000,'true')#capital employees is a class/in instance class has been recalled
sara.employee_details()
sara.attendacne_check()
michael=Employee('michael',50000,'true')
michael.employee_details()
michael.attendacne_check()
















