'''
string -> string is a collection of characters or sequence of characters which represented by '' or "" and we can access the string using indexing.

string='python programming'
print(string)

indexing -> position number of a character in the string (it also allows negative values in its parameters which counts from reverse)

string='python programming'
print(string[7])
print(string[-3])

slicing -> returns the required part of a string (it also allows negative values in its parameters for reverse slicing)

string='python programming'
print(string[7:13])
print(string[-7:-2])

strings are immutable which cant be modify on any purticular variable

string='python programming'
immutable=string.replace('python','java')
print(immutable)
print(string)

my_details="Iam Jaggumantri Surya Patnaik, Iam from vizag. Iam a student at codegnan, here they teach us full stack in python"
print(f'My Name is {my_details[4:29]}')
print(f'My location is {my_details[40:45]}')
print(f'Institute name is {my_details[-49:-41]}')
print(f'Iam learning {my_details[-20:]}')
#reversing and skipping in slicing:
print(f'Reverse of my details is {my_details[::-1]}')
print(f'Reverse of my name is {my_details[-85:-110:-1]}')
print(my_details[1:8:2])
print(my_details[-2:-6:-2])

Methods of string:
len() -> returns the length of the string
syntax -> len(variable_name)

my_details="Iam Jaggumantri Surya Patnaik, Iam from vizag. Iam a student at codegnan, here they teach us full stack in python"
print(f'length of my_details is {len(my_details)}')

split() -> remove space by default and the is in the list[] it will give the seperated thing in each index
syntax -> variable_name.split("seperator") if no seperator by default space

my_details="Iam Jaggumantri Surya Patnaik, Iam from vizag. Iam a student at codegnan, here they teach us full stack in python"
print(my_details.split())
print(my_details.split("."))

lower() -> converts the character into lower case
syntax -> variable_name.lower()

string="HeLLo WorLd"
print(string.lower())

upper() -> converts the character into upper case
syntax -> variable_name.upper()

string="hello world"
print(string.upper())

replace() -> replaces the old value with a new value in a purticular string
synatx -> variable_name.replace("old_value","new_value")

string="Hi my name is Surya"
new_string=string.replace("Hi","Hello")
print(new_string)

string="python is a programming language"
if "python" in string:
    print("yes")
else:
    print("no")

user_input=input("Enter a letter: ")
vowels=['a','e','i','o','u','A','E','I','O','U']
if user_input in vowels:
    print(f'{user_input} is vowel')
else:
    print(f'{user_input} is consonent')

user_input=input("Enter a letter: ")
if user_input in 'AEIOUaeiou':
    print(f'{user_input} is vowel')
else:
    print(f'{user_input} is consonent')
'''


