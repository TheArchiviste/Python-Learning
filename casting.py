int_num = 3
float_num = 4.0

sum = int_num + float_num
# Converted the int to float before doing the addition
# It is not always possible
print(sum)

string_name = 'Jane is '
string_age = '32'
age = 32

full_string = string_name + string_age
print(full_string)

# Wrong! Type Error:
# full_string = string_name + age
# print(full_string)

full_string = string_name + str(age)
print(full_string)