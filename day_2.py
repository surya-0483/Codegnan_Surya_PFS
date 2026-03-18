'''

Variables -->Variables is basically named storage location that is used to hold data in the memory, to make it simple it is the label which points out to a value -->storage placeholders
Rules  for defining variables
--> A-Z,a-z,0-9
-->Start with uppercase, lowercase letters, even with a underscore _
-->But you cannot start with symbols (@,#,$...), even numbers also

Better preferable way is go with general purpose --> yopu want to store your details name , email_id , account_number...

'''
a = 1
b = 5
#Python is dynamically typed, you need not dedfine the datatype and also
#only the recent value to the variable with same name is pointed

print (a)
print (b)

#1a23 = 25 #Syntax Error

#@werf = 4.5 #Syntax Error

#$dsf = 12 #Invalid Syntax

#Store your personal details

name = "Codegnan"
location = "Visakhapatnam"
age = 7
emailid = "cmo@codegnan.com"
email_id = "cmo@codegnan.com"
print(name,location,age,email_id)

#How to asssign multiple values to a  variables
akash,praneeth,ajay = 21,22,23
print(akash)
print(praneeth)
print(ajay)

#How to asssign same values to a  variables

x = y = z = 21
print (x,y,z)

#Keywords are reserved words which wil have specific usage
#There are 35 keywords in python
#never use keywords as Identifiers

#if = 23
#lambda = 'saketh'
#False = 0 #cannot asssign

#Python is case sensitive
false = 25

#Identifiers are names given to variables, functions, classes, objects..

#Literals are fixeed values to a Identifier
age = 22
name = "varun"

#name is Identifier, 22 is literal

#Built-in Datatypes -->Numeric,boolean,Collections

#Numeric datatypes -->int, float,complex
#int -->count,values,quantities
#float --> temperature, percentage, price
#complex --> specific conversions (real and imaginary)

count = 40
print (count)
print (type(count))

price = 175.25
print (price)
print (type(price))

j3 = 22
value = 2 + 3j
print(value)
print (type(value))

#Typecasting -->converting one type to another

#int -->float,complex

age = 25
print(type(age))
'''
b=float (age)
print (b)
print (type(b))
c=complex(age)
print(c)
print(type(c))
'''
#float,complex
price-275.25
print(type(price))
d = int (price)
print (d)
print (type(d))

#float,complex
a = 25.5
print(type(a))

b = int(a)
print(b)
print(type(b))
c=complex(a)
print(type(c))

#complex to int,float

g=3+5j
print(type(g))

k = float(g)
print(type(g))
h = int(g)
print(type(h))
'''


a= True
print(a)
print(type(a))

#TypeCasting of bool
b = int(a)
print(b)
c  = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))
'''
#Input --> input ()/output -->print ()
a=5
print (a)

a= input("Enter a value") #any input but result as str
print (a)
print (type(a))

a= int (input("Enter a value:"00 #only integer input
print(a)
print(type(a))

#Now let's work on a simple case study using above -->Fee Calculator

#Details of the Student
name = input("Enter the student name:")
print("--------------------------------------")
admission_fees = int(input("Enter the Admission fees:"))
tuition_fees = float(input("Enter the Tuition Fees"))
hostel_fees = float(input("Enter the Hostel Fees"))
#Calculate the Total Fees
total_fees = admission_fees+tuition_fees+hostel_fees
print("<----------------------------------------------------->")
print("Student Name:",name)
print("Admission_fees is :",admission_fees)
print("Tuition_fees is :",tuition_fees)
print("Hostel_fees is :",hostel_fees)
print("Total_fees is :",total_fees)
print("<----------------------------------------------------->")
