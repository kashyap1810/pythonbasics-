#IN LIST ALL THE VALUES WILL BE PUT INTO SQUARE BRACKETS SEPARATED WITH COMMA

list_of_random_values=[31,4,31.5,3,'yes']
print(list_of_random_values[0])
print(list_of_random_values[3])
print(list_of_random_values[-1])#(we can also use - sign started from the last )

#create a new list
list_of_cars=['bmw','toyota','tesla','kia']
print(list_of_cars)
print('one before last of the list : '+ str(list_of_cars[-2]))
#compare
print('comoarison between cell of cars : ' +str(list_of_cars[1]=='toyota'))

#creat a new list

mixed_values=['jim',3500,'alex',2.53, True]
print(mixed_values)
print('print the values between the index : '+ str(mixed_values[0:3]))
#add the value 'alpha''romeo' ot the car list

list_of_cars.append("alpha-romeo")
print('car list after adding : '+str(list_of_cars))
