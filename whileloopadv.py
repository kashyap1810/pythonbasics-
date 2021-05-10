number=1
while number <5:
    print (number)
    number+=1
else:
    number*=100
    print('there is no longer a number')
    print(number)

#work

list_of_ages=[5,6,24,32,21,70]
counter=0 #counter is used in while loop when there is a list defined[mandat in loop creation by list ]
while list_of_ages[counter] <30:
    print('print the list of age below 30 :'+str(list_of_ages[counter]))
    counter+=1

print('the value which cuase loop to stop : '+str(list_of_ages[counter]))


print('\n')
print ('----------------------------------------------------------------------------------------')

#part b
counter=0
while list_of_ages[counter] <30:
    if list_of_ages[counter] >20:
        print('print the value which stop the loop inside : '+str(list_of_ages[counter]))
        break
    counter+=1

#part c
counter=0
while list_of_ages[counter] <70:
    list_of_ages[counter]=list_of_ages[counter]+2  #+2 is being used to increase the output number by 2
    print('the list of age below 70 : '+str(list_of_ages[counter]))
    counter+=1
else:
    print('i m outside of the while loop beacuse of 70 : '+str(list_of_ages[counter]))

counter=0
while list_of_ages[counter] <70:

    if list_of_ages[counter] >5:
        print('the list of ages grater than 5 : '+str(list_of_ages[counter]))
    counter+=1
