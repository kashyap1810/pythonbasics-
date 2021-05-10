# what is method
# A method is a block of code which only runs when it is called .
# you can pass variables , collections etc through the method 'execution' command
# A method is a programming which is been used to block the code and basically to re use it
# A method is also a function .once the method is executed code inside it will run
# A method is recognized as 'def'
# def my_method():


def my_function(age):
    print('the age is : '+str(age))

my_function(25)
my_function(32)
my_function(39)

def salary_calculation(salary):
  salary_of_employee=salary * 0.98
  print('the salary is : '+str(salary_of_employee))

salary_calculation(200000)
salary_calculation(100000)



def salary_calculation(salary,tax_reduction):
  salary_of_employee=salary * tax_reduction
  print('the salary after deduction is : '+str(salary_of_employee))

salary_calculation(200000,0.98)
salary_calculation(100000,0.97)

print('\n')
print('*********************************************************************************************')
# mid level method


def my_function(country = "canada"):
    print('i am from : '+  country)

my_function ('italy')
my_function()
my_function ('india')

print('\n')
print('*********************************************************************************************')

def my_function(x):
    return 5*x
number=my_function(6)
print(number)