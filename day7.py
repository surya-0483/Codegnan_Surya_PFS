'''
most repeated word in given text without dictionary:
text=input().split()
index=0
most=0
for i in text:
    if text.count(i)>most:
        most=text.count(i)
        index=text.index(i)
print(f'most repeated word in the given text is {text[index]} for {most} times')

print(9+8)
print('python'+'language')
print([1,2]+[3,4])

concatenation
--------------
this is nothing but, a (+) behaviour

case-1
-------
integers -> this will act as a addition operator

case-2
-------
for other data types (we have to use same type) this (+) acts as concatenation

print("varun"+[1,2]) #type error

tuple()-> it is a collection of diffrent datatype and this is represented by (), seperated by (,)
eg...
thing=(1,'surya',[12,4],(6,7))
print(thing)

thing2=(12,89,'python',(23,'Teja',[67,'python is a language',(7,8)],[8,('python',[34,9])]))
print(thing2)
print(thing2[3][2][1][6]) #output=' '(space before is)

swapping without 3rd variable
num1=9
num2=90
print(f'before swapping num1={num1} and num2={num2}')
num1,num2=num2,num1
print(f'after swapping num1={num1} and num2={num2}')

leap_year=int(input('Enter year: '))
if (leap_year%400==0) or (leap_year%4==0 and leap_year%100!=0):
    print(f'Yes, {leap_year} is a leap year')
else:
    print(f'No, {leap_year} is not a leap year')
'''
