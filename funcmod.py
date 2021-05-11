#defining function def

def homework_task():
    print('your homework task :')
    print('declare a variable in python')
print('start')
homework_task()
print('end')

print('***********************************************************************************')

def homework_task(languages):
    print('your homework task :')
    print('declare a variable in :'+languages)
print('start')
homework_task('python')
homework_task('java')
print('end')

print('***********************************************************************************')
print('\n')

def homework_task(languages,task):
    print('your homework task :')
    print(task+':'+ 'declare a variable in:'+languages)
print('start')
homework_task('python','developing')
homework_task('java','creation')
print('end')

print('***********************************************************************************')
print('\n')

# return function

def path(v,t):
    print(v*t) #getting none in result because the function is not returning the value as we print(2nd time) S in the func. so the S is declared 1st then the none func.
s=path(30,60)
print(s)

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
def path(v,t):
    return (v*t)
print(path(30,60))

print('***********************************************************************************')
print('\n')

#function
degree=input('what is your degree masters,phd,bachelor?')
experience=input('how many experience do you have?')
if degree=='master' or degree=='phd' or degree=='bachelor':
    if int(experience)>=2:
            print('you are accepted for the interview')
    else:
            print('experiece not met the requirements ')
else:
        print('you degree not met the requirements')

print('***********************************************************************************')
print('\n')
# defining in function
def work(degree,experience):

    if degree == 'master' or degree == 'phd' or degree == 'bachelor':
        if int(experience) >= 2:
            return 'you are accepted for the interview'
        else:
            return 'experiece not met the requirements '
    else:
        return 'you degree not met the requirements'
print(work('phd',5))


print('***********************************************************************************')
print('\n')

#exception by using try


try:
    items=int(input('type a number of item'))
    print(items)
    total=30
    price_per_item=total/items
    print(items)
except ValueError: #when the value is not an integer so we add  ValueError for exception
    print('the value is not integer')
except ZeroDivisionError: # as we cannot divide by zero so we me use ZeroDivisionError for not getting fatal if we try to divide by 0
    print('you cannot divide by zero')


print('***********************************************************************************')
print('\n')

