#list
employees=['adam','john','greg','danna','ashley']
print('employees length : '+ str(employees.__len__()))
employees[1]='jack'
print(employees)
employees.insert(3,'mavrik')
print(employees)
employees.remove('mavrik')
print(employees)
employees.append('mavrik')
print(employees)
employees.pop()
print(employees)
