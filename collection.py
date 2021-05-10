#dictionary is an unoredered type of collection
# in it key/value pair{key.value}
#dictionary_example = {}

dictionary_example = {'name':'rachel','test_grade':98}
print(dictionary_example['name'])

#another way print(dictionary_example.get('name'))

#cretae a new dictionary

new_employess = {'first name' : 'david','salary' : 10000 , 'company' : 'google'}
print("print the dictionary  : "+str(new_employess))

#extract cells value first way
print(new_employess['first name'])

print("print the secod way to extract : "+str(new_employess.get('salary')))


#remove dictionary cell be using pop

new_employess.pop('salary')
print(new_employess)


#get all the keys
print(new_employess.keys())

#get all the value
print(new_employess.values())



#use a variable and place it into inside the dictionary

job_title_value = "developer"
new_dictionary = {'job title': job_title_value}
print("print the new dictionary : " + str(new_dictionary))

