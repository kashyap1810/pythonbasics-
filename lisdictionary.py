#dictionary

new_employee={'first name':'david','salary':1000,'company':'google'}
print(new_employee)
print('get the value of the first name key : ' +str(new_employee['first name']))
print('print the salary : ' + str(new_employee.get('salary')))
new_employee.pop('salary')
print('print the new list : ' + str(new_employee))
print('get all the keys : ' + str(new_employee.keys()))
print('get all the values : ' + str(new_employee.values()))
job_title='developer'
new_dictionary={'job title': job_title}
print(new_dictionary)


print('*****************************************')



alex={'age':32,'married':'yes','kids':3}
print(alex)

age=alex['age']
married=alex['married']
kids=alex['kids']
print('print the age values  : '+str(age))
print('print the status : '+(married))
print('no. of kids : ' + str(kids))
age_helper_dictionary={'age':33}
alex.update(age_helper_dictionary)
print('print the age  : ' +str(alex))
#update the kids
alex_helper_dictionary={'kids':4}
alex.update(alex_helper_dictionary)
print(alex)
print(alex.values())
print(alex.keys())

#nested dictionary
joe={'age':33,'kids':{'david':'boy','lisa':'girl'}}
print(joe['kids'])
print(joe['kids']['david'])

joe_new=joe.copy()
print('print the new copy dictionary : ' + str(joe_new))


# assignment

new_building={'floor1':{'first apartment':'rachel','second aprtment':'jeen'},
             'floor2':{'third apartment':'jack'}}
print(new_building)
#extract nested cell items
print(new_building['floor1'])
print(new_building['floor2'])
print('in which floor jeen leaves : '+str(new_building['floor1']['second aprtment']))
print('third apartment person : '+str(new_building['floor2']['third apartment']))
print('in which floor jack leaves : '+ str(new_building['floor1']['first apartment']))

new_building['floor2']['apartment 4']='carol'
print(new_building)
new_building['floor1'].pop('first apartment')
print(new_building)