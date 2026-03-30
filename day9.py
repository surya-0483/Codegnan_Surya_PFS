'''
a=9
print(b) #name error
for j in range(1,10):
    print(j)

range() -> this is used to generate numbers
syntax -> range(start,end,step)

for j in range(1,20,3):
    print(j) 

any='123'
print(int(any))
print(list(any)) #output: ['a','b','c']
print(set(any)) #output: {'a','b','c'}
print(tuple(any)) #output: ('a','b','c')

so=123
print(str(so))
print(float(so))

an=[1,2,3]
vs=str(an)
print(type(vs))
print(vs)
print(tuple(an))

a=[('surya',21),('sowmi',23),('anu',20)]
print(dict(a))

a='surya'
print(a[::-1])

name=input('Enter your name: ')
reverse=''
for i in name:
    reverse=i+reverse
print(f'reverse of your name is: {reverse}')

word=input('Enter a word: ')
reverse=''
for i in word:
    reverse=i+reverse
if reverse==word:
    print(f'{word} is Palindrome')
else:
    print(f'{word} is Not Palindrome')

Python programs file is created in which all programs are practiced
'''
