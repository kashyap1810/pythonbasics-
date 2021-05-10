#error handling , syntax error , parsing error (value not assigned )
#zero devivtion error (mathematical error dividing anuthing by zero )
#type error(typing error )
#name error (variable not found in local or global scope )
#index error (index not exist as in list there will be index )
#indentation error
#key error
#Value error

#excception
try:
    if age<20:
        print('this person held the thor value')
except:
    print('age value is not assigned ')
    age=3
    if age<20:
        print('this is young')


print('**********************************************************************************')


x=5
try:
  print('the no. is :'+x)#if we declare any value inside try then we will not been able to use in except -declare outside try
except:
    print('casting is not made to print number x')
    print('the number is : %s '%x)
    print('\n')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
list = [1, 2, 3, 4]
try:

    print(list[6])
    print('xxxx')
except:
    print('index 6 not available ')
    print(list[3])

#list=[1,2,3,4]
#print(list[6])
