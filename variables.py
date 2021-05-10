#list of the variables
short_string_variables = "my name is ravi"
print(short_string_variables)

#print the letter of string variables
first_letter_varaibles = "hajipur"[0]
print(first_letter_varaibles)

#mixed letter variables
mixed_letter_variables = "this is a mixed letter variaBles"
print(mixed_letter_variables.upper())

#length of the variabkles
print(mixed_letter_variables.__len__())

#use + sign in the variavbles
first_name = "david"
print("first name : " +first_name)

#replace the part of the string
first_serial_number = "ABC123"
print("change serial number #1 : " + (first_serial_number.replace('123','456')))

#second serial number
second_serial_number = "ABC123ABC"
print("second serial number #2 : " + (second_serial_number.replace('ABC', 'DEF' , 1)))

#specific index range
range_of_index = second_serial_number[0:3]
print(range_of_index)

#space between variables
first_word ="Thank "
second_word ="you "
third_word ="Ninjas !"
print(first_word+second_word+third_word)


#string name variables
windows_serial_number = "abc-def-ghi-jkl"
print(windows_serial_number)

#create new 4 variables
new_partial_variables_a = windows_serial_number [0 : 3]
new_partial_variables_b = windows_serial_number [4 : 7]
new_partial_variables_c = windows_serial_number [8 : 11]
new_partial_variables_d = windows_serial_number [12: 15]
print(new_partial_variables_a)
print(new_partial_variables_b)
print(new_partial_variables_c)
print(new_partial_variables_d)

#replace the variables with the letters individually
new_partial_variables_a = new_partial_variables_a.replace('abc', 'aaa' )
new_partial_variables_b = new_partial_variables_b.replace('def', 'bbb' )
new_partial_variables_c = new_partial_variables_c.replace('ghi', 'ccc' )
new_partial_variables_d = new_partial_variables_d.replace('jkl', 'ddd' )
print(new_partial_variables_a)
print(new_partial_variables_b)
print(new_partial_variables_c)
print(new_partial_variables_d)

#new encoded windows variables
encoded_windows_serial_number = new_partial_variables_a+"-"+new_partial_variables_b+"-"+new_partial_variables_c+"-"+new_partial_variables_d
print(encoded_windows_serial_number)

#print serial number in plain text

print("encoded serial number ahead : "+ encoded_windows_serial_number)

