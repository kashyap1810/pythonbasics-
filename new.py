# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
string_variable = "have a great day"
print(string_variable)

first_letter_variable ='new york city'[0]
print(first_letter_variable)
mixed_letter_variable='have A greaT day'
print(mixed_letter_variable.upper())
length_of_the_variable='have a great day'
print(length_of_the_variable.__len__())
first_name="david"
print('after adding :'+str(first_name))
first_serial_number='ABC123'
print('replace the number : '+(first_serial_number.replace('123','456')))
second_serial_number = 'ABC123ABC'
print('change serial number : ' + (second_serial_number.replace('ABC','DEF',1)))
#take a part of the variable acc to the specific places
range_of_indexes=second_serial_number[0:3]
print(range_of_indexes)



window_serial_number="abc-def-ghi-jkl"
new_partial_variable_a= window_serial_number[0:3]
new_partial_variable_b= window_serial_number[4:7]
new_partial_variable_c= window_serial_number[8:11]
new_partial_variable_d= window_serial_number[12:15]
print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)

new_partial_variable_a=new_partial_variable_a.replace('abc','aaa')
new_partial_variable_b=new_partial_variable_b.replace('def','bbb')
new_partial_variable_c=new_partial_variable_c.replace('ghi','ccc')
new_partial_variable_d=new_partial_variable_d.replace('jkl','ddd')
print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)

#create a new serial number out of the partial variable
encoded_windows_serial_number=new_partial_variable_a+'-'+new_partial_variable_b+'-'+new_partial_variable_c+'-'+new_partial_variable_d
print(encoded_windows_serial_number)
#print the serial number along with the plain text
print('encoded serial number : '+encoded_windows_serial_number)
