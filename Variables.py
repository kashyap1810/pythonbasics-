# a simple string example
short_string_variables = "have a great day"
print(short_string_variables)

# First letter variable
first_letter_variables = "hajipur"[0]
print(first_letter_variables)

#mixed letter variables
mixed_letter_variables = "This is a mixed letter variables"
print(mixed_letter_variables.upper())

#length of a variable
print(len(mixed_letter_variables))

#use a "+" sign inside the variables
first_name = "david"
print("first name is : "+first_name)

#replace a part of a string
first_serial_number = "ABCD1234"
print("changed serial number #3: "+first_serial_number.replace('1234' , '4567'))

#repeat
short_string_variables = "have a great day"
print(short_string_variables)

first_letter_variables = "hajipur"[1]
print(first_letter_variables)

mixed_letter_variables = "this is mixed letter variablEs"
print(mixed_letter_variables.upper())
print(len(mixed_letter_variables))
print(mixed_letter_variables.lower())
first_name = "ravi"
print("first name :"+first_name)

first_serial_number ="ABCD1234"
print("changed serial number #1:"+first_serial_number.replace('1234' , '5468'))


#changed serial number
second_serial_number = "ABC1234ABC"
print("change serial number #2:"+second_serial_number.replace('ABC','EFG' ,2))


#take a part of a variable according to specific index places
range_of_index = second_serial_number[0:3]
print(range_of_index)



#windows serial number
windows_serial_number = "abc-def-ghi-jkl"
print(windows_serial_number)

#use the index and ranges
new_partial_variable_a = windows_serial_number [0:3]
new_partial_variable_b = windows_serial_number [4:7]
new_partial_variable_c = windows_serial_number [8:11]
new_partial_variable_d = windows_serial_number [12:15]
print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)

#replace the number
new_partial_variable_a = new_partial_variable_a.replace('abc','aaa')
new_partial_variable_b = new_partial_variable_b.replace('def','bbb')
new_partial_variable_c = new_partial_variable_c.replace('ghi','ccc')
new_partial_variable_d = new_partial_variable_d.replace('jkl','ddd')
print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)

#create a new serial number
encoded_windows_serial_number = new_partial_variable_a+"-"+new_partial_variable_b+"-"+new_partial_variable_c+"-"+new_partial_variable_d
print("encoded serial number :"+ encoded_windows_serial_number)

#print serial number plain text
print("encoded serial number ahead : "+encoded_windows_serial_number)