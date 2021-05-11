basketball=input('who is your fav basketball player:')#input is used to provide input by the user
print('my fav. player is ' + basketball)

print('****************************************************************************************')

yourage=input('how old are you')
birthyear=2021-int(yourage)
print(birthyear)


print('******************************************************************************************************************')

#number A and number B

numA=float(input('first'))#using decimal that's y we used float
numB=float(input('second'))
sub=numA-numB
print('result : '+str(sub))
if sub<0:
    print('negative number')
else :
    print('positive number')

print('****************************************************************************************')
#operation with strings

martin='i love programming and will learn fast'
print(martin.upper())
print(martin.lower())
print(martin.find('g'))# to find the letter position
print(martin.replace('love','like'))
print(martin.find('programming'))

print('*********************************************************************************************')
#arithmetic operations

x=5
y=11
print(y%x)
print(2**3)

x=x+y #we can also use x+=y
print(x)

print('****************************************************************************************')

x=5>4 #boolean vaiables comparison operator
print(x)

x=5==4
print(x)

print('****************************************************************************************')

rent=550
print(rent>50 or rent<100)

print('****************************************************************************************')
rent=550
print(rent>50 and rent<100)

print('*********************************************************************************************')

rent=550
print(rent>50 and rent<100 and rent!=400)

print('*******************************************************************************************')

#if statements

car_speed=70
if car_speed>100:
    print('you are overspeeding')
elif car_speed<20:
    print('speed is slow')
else:
    print('you are at moderate speed')
print('ready')


print('**************************************************************************************')
#while loop

i = 0
while i<=5:
    print(i)
    i=i+1

print('**********************************************************************************')

i=0
while i<=5:
    print(i)
    print(i*'2')
    i=i+1
print('***********************************************************************************')

temp=[67,30,70,43,91]
for item in temp:
    print(item)


print('***********************************************************************************')
#for loop

numbers=range(10)
for number in numbers:
    print(number)

print('***********************************************************************************')
numbers=range(10,100,5)#every 5th number will be shown b/w 10 to 100 that's y we declare 5
for number in numbers:
    print(number)

print('***********************************************************************************')
#list

tech_list=['apple','microsoft','dell','lenovo','hp']
print(tech_list[0:2])#define the elements we need to declare b/w 0:2
tech_list.remove('hp')
print(tech_list)
tech_list.insert(4,'tesla')
print(tech_list)
print(len(tech_list))
print('microsoft' in tech_list)#result will be in boolean variables
tech_list.clear()
print(tech_list)

print('***********************************************************************************')
#dictionary

fruits={'banana':0.49,'orange':1.5,'apple':1.09}
print(fruits)
fruits['orange']=2.60
print(fruits)
print(fruits['apple'])
fruits['melon']=3#adding to the list
print(fruits)
print('banana'in fruits)

print('***********************************************************************************')


