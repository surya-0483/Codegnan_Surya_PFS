'''
Operators -->An Operator is a symbol that performs an
opertion on one or more values (operands) and prodcues a
result

Operators are primarily used :
-->Calculate values
-->Compare values / inputs
-->Make decisions
-->Control the program flow

There are major seven categories of Operators in Python

-->Arithmetic Operators
-->Assignment Operators
-->Comparision Operators
-->Membership Operators (in,not in)
-->Identity Operators (is,is not)
-->Bitwise Operators
-->Logical Operators (and,or,not)
'''

#Arithmetic Operators -->Arithmetic Operators perform mathematical operations

# + -->Addition,- -->Subtraction , * -->Multiplication, / -->Division
# ** -->Exponent , % -->Modulus,// -->Integer Division

'''a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #returns the result in float values
print(a**b) #returns the exponential value

print(a % b) #Modulus division -->returns remainder
print(a // b) #Flooring / Integer Division -->returns Quotient discards float values


num1 = int(input("Enter the first value:"))
num2 = float(input("Enter the second value:"))
result = (num1 + num2)*4
print("The result is",result) #standard notation

#f-string notation
print(f'The result is {result}')
print(f'The result of {num1} and {num2} is {result},{num1*num2}')


#Assignment Operators
#--> = Assign, += Addition Assignment ,
#-= -->Subtract Assignment,*=,/=,%=,//=,**=

#They are majorly used for code repetitions in application usage

a = 4
b = 3
a += 2 #--> a = a+2
print(a)
b += a
print(b)
#in similar way check for -=, *=, **=,/=, %=, //=

b -= 3 #b = b-3
print(b)
print(f'The updated values of a and b are {a} and {b}')
b *= a # b = b*a
print(b)


#Relational or Comparision Operators -->They always return the boolean
#values (True / False)

# == is equal to, != not equals to
# < less than, > greater than , >= , <=

a = int(input("Enter a value:"))
b = int(input("Enter another value:"))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

#Membership Operators -->They check for the existance of an object in a
#collection --> in,not in
a = "codegnan"
print(type(a))
print('a' in a)
print('z' in 'saketh')
print('z' not in 'codegnan')

b = [12,6,3,4]
c = int(input("Enter the value"))
print(c)
print(c in b)
print(c not in b)

#Logical Operators -->They are used to combine multiple conditions
#and,or,not
age = int(input("Enter the age:"))
vote_right = True

print(age>=18 and vote_right) #both conditions to be True then only True
print(age>18 or vote_right)#any one condition is True then result is True
print(not vote_right)

#Identity Operators -->They check the/compare the memory location and validate we use
#(id) function it is different from == operator -> is,is not
a = [1,2,4]
b = [1,2,4]
print(a == b)
print(id(a)) #returns the identity of an object
print(id(b))
print(a is b)
print(a is not b)

c = b
print(c)
print(id(c))
print(c is b)
'''
#Bitwise Operators -->Bitwise AND & ,Bitwise OR | perform bitwise operations
#we get the result (remember the binary conversion)
print(5&3)
print(bin(5)) #returns binary number

#Task --> Now you have all Operators create a Checker Task
#git add .
#git commit -m "operators usage"
#git push -u origin main





























































































































































































































