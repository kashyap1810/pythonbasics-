def phone_brand(brand1,brand2,brand3):
    print('the 1st brand is : '+ brand1)

phone_brand(brand1='apple',brand2='lg',brand3='samsung')

print('\n')
print('-------------------------------------------------------------------------')
#arbitary arguments means random value

def clothing_companies(*clothing_companies): #star is used as tuple so that passing three variables not leds tothe error
    print('the last company : '+clothing_companies[-1])
clothing_companies('nike','adidas','reebok')
clothing_companies('nike','adidas')#here only 2 variable but inbefore 3 vari that's y tuple is being used

#
print('\n')
print('-----------------------------------------------------------------------')

#arbitary keyword argument is used if we don't know how many variable is being passed


def my_function(**company_info):
    print('the phone is : '+ company_info['model'])
my_function(brand='apple',model='iphone 11')


print('\n')
print('-------------------------------------------------------------------------')

def sorting(*languages_list):

    for language in languages_list:
        if language=='java':
            print('java language found')
            for character in language:
                print(character)
        else:
            print('java not found ')

sorting('python','java')
sorting('python','java','c')
sorting('python','js','c')

print('\n')
print('******************************************************************************')

#part b

def tax_calculation(gross_salary, tax=0.22):
    net_salary=gross_salary *(1-tax) # 1 means the 100 percent
    print('the net salary of the employee is : '+str(net_salary))
    return net_salary

def salary_limit_tester(net_salary_variable):
    if net_salary_variable>=5000:
        print('success the salary is : '+str(net_salary_variable))
    else:
        print('the salary is under 5000 : '+str(net_salary_variable))

net_salary1=tax_calculation(5000,0.2)
salary_limit_tester(net_salary1)

net_salary2=tax_calculation(6000,0.22)
salary_limit_tester(net_salary2)

net_salary3=tax_calculation(10000)
salary_limit_tester(net_salary3)

