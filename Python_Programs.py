'''
word=input('Enter a word: ')
reverse=''
for i in word:
    reverse=i+reverse
if reverse==word:
    print(f'{word} is Palindrome')
else:
    print(f'{word} is Not Palindrome')

limit=int(input('Enter range of numbers: '))
for i in range(limit+1):
    if i%2==0:
        print(f'{i} is a even number')
    else:
        print(f'{i} is a odd number')

num=int(input("Enter a number: "))
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
if count==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

limit=int(input("Enter the range: "))
print("1 is not a prime number")
primes=[]
for i in range(2,limit+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        primes.append(i)
        print(f'{i} is a prime number')
    else:
        print(f'{i} is not a prime number')
print(f'The number of prime numbers upto {limit} are {len(primes)} which are {primes}')

table_number = int(input("enter the number : "))
for i in range (1,21):
    print(f"{table_number}x{i} = {table_number * i}")

methods
-----------------
count(),capitalize(),join(),
strip(),replace(),split(),
casefold(),isalnum(),isalpha()
,isdigit(),isdecimal(),islower(),
isupper()
------------------
there are more methods , but this methods are used most in the programming  


al = input("enter the string :")
count_u = 0
count_l = 0
for j in al :
    if j.isupper():
        count_u += 1
    elif j.islower():
        count_l += 1
print(f"there are total {count_u} cap L")
print(f"there are total {count_l} small l")
#------------------------------------------------------------------------------

ak = input("enter the string :")
Cap_L = []
small_L = []
for ch in ak :
    if ch.isupper():
        Cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{Cap_L} contains all the caps ")
print(f"{small_L} contains all the smalls")
#--------------------------------------------------------------------------------       
icici_ramayya_ac_details = {"Name":"Neduri jaichandra dasaradha ramayya",
                            "date-of-brith" : "15-06-2004",
                            "ATM PIN" : "113374"}
print("welcome to the icici bank")
print("please insert the ATM card")
icici_user_pin = input("please enter your 6 digits ATM pin : ")
if len(icici_user_pin) == 6:
    if icici_user_pin in icici_ramayya_ac_details['ATM PIN']:
        print("the pin number is correct")
    else:
        print("the pin number is incorrect")
else:
    print("please enter the 6 digits numbers")

#---------------------------------------------------------------------------------
# perfect number
per_num = int(input("enter the number : "))
fact_all = 0

for j in range(1, per_num):
    if per_num % j == 0:
        fact_all += j

if fact_all == per_num:
    print(f"{per_num} is a perfect number")
else:
    print(f"{per_num} is not a perfect number")

break --->this is used to get out of the purticular loop

for i in range (1,10):
    print(i)
    if i == 5 :
        break

list = [1,2,3,4,5]
for n in list :
    print(n)
    if n == 1:
        break

continue ---> this is used to skip that particular loop and this methods is not used for multiple values

for j in range(1,20):
    if j == 5:
        continue
    print(j)
    
list = [1,3,4,5,"neduri","jaichandra"]
for j in list:
    if j == "neduri":
        continue
    print(j)

ad = "neduri jaichandra dasaradha ramayya"
for j in ad:
    if j == "n":
        continue
    print(j)

pass ---> this is called as space holder
incase any statement like (if, for, else, elif...) this should complete, if not we will get syntax error to avoid this we are using pass

for i in range (1,100):
    pass

else -- for
--------------
it will fall back to else block, when all loops are completed

for m in range(1,10):
    print(m)
else :
    print("else block")

#while ---> this a combination for and if statements, if we did not end the loop in proper way it will run upto the memory space in the becomes empty
user_in = int(input("enter the limit : "))
num_1 = 0
num_2 = 1
print(num_1,num_2,end="")
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")

pattern programs

num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range(j):
        print("*",end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (2,num+2):
    for i in range(1,j):
        print(i,end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range (num):
        print("*",end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (num):
    for i in range(num-j):
        print("*",end = "")
    print()

num = int(input("enter the limit of the pattern : "))
for j in range (num):
        print(" "*(num - j), end = "")
        for i in range(j+1,j-1) :
            print("*", end= " ")
        print()

icici_ramayya_ac_details = {"Name":"Neduri jaichandra dasaradha ramayya",
                            "date-of-brith" : "15-06-2004",
                            "ATM PIN" : "113374",
                            "Balance" : 200000}
print("welcome to the icici bank")
print("please insert the ATM card")
icici_user_pin = input("please enter your 6 digits ATM pin : ")
if len(icici_user_pin) == 6:
    if icici_user_pin in icici_ramayya_ac_details['ATM PIN']:
        icici_user_choice = int(input("enter \n1.withdraw: ")) 
        if icici_user_choice == 1:
            money_w = int(input("enter the money to withdraw : "))
            if money_w <= icici_ramayya_ac_details['Balance']:
                icici_ramayya_ac_details['Balance'] -= money_w
                print(icici_ramayya_ac_details['Balance'])
            else:
                print("insuff")
            
    else:
        print("the pin number is incorrect")
else:
    print("please enter the 6 digits numbers")

functions() -> this is a block of code which is reusable.
functions are of 2 types:
1. built-in or in-built -> they comes with the program itself those are aldready defined. example: append(),max(),min(),print(),sort(),sum(),map()
2. user defined -> this is created person who is developing or using for development
note: it starts with a def keyword followed by function name and it has calling function
syntax: def function_name(parameters) ------code------- function_name(arguments)

def even_number_check(num):
    if num%2==0:
        return(f'{num} is a even number')
    else:
        return(f'{num} is not a even number')
num=int(input())
print(even_number_check(num))

def even_number_check(num):
    if num%2==0:
        print(f'{num} is a even number')
    else:
        print(f'{num} is not a even number')
num=int(input())
even_number_check(num)

def even_number_check(num):
    if num%2==0:
        print(f'{num} is a even number')
    else:
        print(f'{num} is not a even number')
even_number_check(num=int(input()))

num=int(input("enter a number: "))
count=0
def prime_check(prime_num,count):
    for i in range(1,prime_num+1):
        if prime_num%i==0:
            count+=1
    if count==2:
        print(f'{prime_num} is a prime number')
    else:
        print(f'{prime_num} is not a prime number')
prime_check(num,count)

def prime_check(prime_num,count):
    for i in range(1,prime_num+1):
        if prime_num%i==0:
            count+=1
    if count==2:
        print(f'{prime_num} is a prime number')
    else:
        print(f'{prime_num} is not a prime number')
prime_check(prime_num=int(input("Enter a number: ")),count=0)

def palindrome(word,empty):
    for i in word:
        empty=i+empty
    if word==empty:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')
palindrome(word=input("Enter a word: "),empty="")

def fibo(limit,n1,n2):
    print(n1,n2,end=" ")
    for i in range(limit-2):
        add=n1+n2
        print(add,end=" ")
        n1=n2
        n2=add
fibo(limit=int(input("Enter the range: ")),n1=0,n2=1)

print(f'no of words in the given sentence: {len(input("enter a sentence: ").split())}') #no of words in a sentence

#compound intrest
principal=float(input("Enter Principle: "))
rate_of_intrest=float(input("Enter Rate of Intrest: "))
time_period=float(input("Enter Time Period: "))
n=int(input("Compounded Anually = 1\nCompounded Half yearly = 2\nCompounded Quaterly = 4\nEnter respective number: "))
amount=principal*((1+(rate_of_intrest/100*n))**(n*time_period))
print(f'Compound Intrest = {amount-principal}')

ways to pass the arguments in the calling function ->

required arguments: it should match same number of variables in the calling with def or same number of variables in the arguments with the parameters
num=9
mum_2=10
def add(num,num_2):
    print(num+num_2)
add(num,num_2)

default arguments: it will take the default values from the arguments
my_name="Surya"
def add(my_name):
    print(my_name)
add(my_name="patnaik")
add(my_name="jaggumantri")

def prime(num,count):
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
prime(num=int(input("Enter a number: ")),count=0)

#user-friendly prime check code
def prime(num,count):
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
while(1):
    num=input("Enter a number to check whether it is prime or not else enter 'stop' to stop the process: ")
    if num=='stop':
        exit()
    elif num.isdigit()==True:
        prime(int(num),count=0)
    else:
        print("Enter valid input")

keyword arguments: in the calling function or in the arguments, we will directly pass it as key=value form
def any(num,num_2):
    print(num,num_2)
any(num=7,num_2=int(input('enter a number: ')))

def any(num,num_3,num_2):
    print(f'num={num},num_2={num_2},num_3={num_3}')
any(num_2=7,num=0,num_3=90)

variable length arguments: adding a star (*) before the parameter name in the function, receive a tuple of arguments and can access items with indexes
def name(*candidate):
    print(candidate)
    print(candidate[1])
    for i in candidate:
        print(i,end=" ")
name('surya','sowmi','anu')

#Amstrong number
num=int(input("Enter a number: "))
length=len(str(num))
total=0
for i in str(num):
    total+=int(i)**length
if total==num:
    print(f'{num} is a Amstrong number')
else:
    print(f'{num} is not a Amstrong number')

#Perfect number
num=int(input("Enter a number: "))
total=0
for i in range(1,num):
    if num%i==0:
        total+=i
if total==num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')

#compound intrest
p=float(input('enter pricipal: '))
ri=float(input('enter intrest: '))
t=float(input('enter time: '))
n=int(input('enter 1,2or4: '))
a=p*(1+(ri/(100*n))**(t*n))
print(f'compund intrest is: {a-p}')

recursive functions
-------------------
recursion is a programming technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller,simpler sub
problems. recursion is especially useful for problems that can divided into identical smaller tasks, such as mathematical calculations, tree traversals or
divide-and-conqure algorithms.

def fibonaci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return(fibonaci(num-1)+fibonaci(num-2))
print(fibonaci(int(input())))

def validate_pin(self):
    while self.remaining_attempts>0:
        user_pin=input('Enter 4 digit PIN: ')
        if len(user_pin)==4 and user_pin == self.user_info['ATM PIN']:
            print('Welcome to the ATM')
            return True
        else:
            self.remaining_attempts-=1
            if self.remaining_attempts>0:
                print(f'Invalid PIN. Attempts left: {self.remaining_attempts}')
            else:
                print('Card blocked. Please contact customer care')
                return false

def vowel_consonents(sentence,vowels,consonents):
    for i in sentence:
        if i in 'AEIOUaeiou':
            vowels.append(i)
        elif i.isalpha()==True:
            consonents.append(i)
    print(f'{vowels} these are the vowels in the sentence')
    print(f'{consonents} these are the consonents in the sentence')
vowel_consonents(sentence=input('enter a sentence: '),vowels=[],consonents=[])

sbi_surya={'Name':'Surya Jaggumantri','ATM pin':'2004','Balance':'5000','Transaction history':[]}
while(1):
    count=0
    check=0
    while(count<3 and check==0):
        pin=input('Enter ATM pin: ')
        if pin!=sbi_surya['ATM pin']:
            count+=1
            print(f'incorrect pin, you have {3-count} attempts more')
        else:
            print('welcome to home page')
            check=1
    if count==3:
        print('your attempts are over contact customer care')
        exit(0)
    num=int(input(f'1.deposite\n2.withdraw\n3.change pin\n4.transaction history : '))
    if num==3:
        count=0
        check=0
        while(count<3 and check==0):
            old_pin=input('enter old pin: ')
            if old_pin!=sbi_surya['ATM pin']:
                count+=1
                print(f'incorrect old pin, you have {3-count} attempts more')
            else:
                new_pin=input('enter new pin: ')
                if len(new_pin)==4 and new_pin.isdigit()==True:
                    sbi_surya['ATM pin']=new_pin
                    print('pin updated sucessfully!')
                    check=1
                else:
                    print('enter valid pin')
        if count==3:
            print('your attempts are over contact customer care')
            exit(0)

output:
Enter ATM pin: 1997
incorrect pin, you have 2 attempts more
Enter ATM pin: 23
incorrect pin, you have 1 attempts more
Enter ATM pin: 2004
welcome to home page
1.deposite
2.withdraw
3.change pin
4.transaction history : 3
enter old pin: 2345
incorrect old pin, you have 2 attempts more
enter old pin: 3456
incorrect old pin, you have 1 attempts more
enter old pin: 2004
enter new pin: 1997
pin updated sucessfully!
Enter ATM pin: 2004
incorrect pin, you have 2 attempts more
Enter ATM pin: 3456
incorrect pin, you have 1 attempts more
Enter ATM pin: 1997
welcome to home page
1.deposite
2.withdraw
3.change pin
4.transaction history : 3
enter old pin: 1997
enter new pin: 2004
pin updated sucessfully!
Enter ATM pin: 45
incorrect pin, you have 2 attempts more
Enter ATM pin: 34
incorrect pin, you have 1 attempts more
Enter ATM pin: 46
incorrect pin, you have 0 attempts more
your attempts are over contact customer care

lambda function()
-> this is also called anonymous function
-> A lambda function can take n number of arguments but have only one expression
syntax -> lambda(keyword) arguments : expression

any=lambda so : so+10
print(any(6))

add=lambda num1,num2 : num1+num2
print(f'sum of given numbers: {add(int(input('enter 1st number: ')),int(input('enter 2nd number: ')))}')

square=lambda x:x**2
print(square(int(input())))

some=lambda an,how,do:(how-an)*do
print(some(4,9,2))

result=lambda a,b,c,d,e,f,g:a//b/c%d*e+f-g
print(f'result= {result(int(input('enter num1: ')),int(input('enter num2: ')),int(input('enter num3: ')),int(input('enter num4: ')),int(input('enter num5: ')),int(input('enter num6: ')),int(input('enter num7: ')))}')

list comperhension -> this is offers the shorter synatx when you want to create a new list from the existing list
syntax -> variable_name=[expression loop and condition]

old_list=[1,2,3,4,5]
new_list=[j for j in old_list]
print(new_list)

old_list=[1,2,3,4,5]
new_list=[j for j in old_list if j%2==0]
print(new_list)

-------------------------------------------------------------BANK APPLICATION-----------------------------------------------------------------------------
check=0
while check==0:
    bank_num=input('1.SBI\n2.ICICI\n3.HDFC\n4.Axis\n5.Indian Bank\n6.BOI\nEnter the respective number of the bank you want to choose: ')
    if bank_num in '123456':
        bank_dict={'1':'SBI','2':'ICICI','3':'HDFC','4':'Axis','5':'Indian Bank','6':'BOI'}
        bank_name=bank_dict[bank_num]
        check=1
    else:
        print('Enter Valid Input')
        print('')
print('')
print(f'Create your {bank_name} Bank Account \n---------------------------------------------------------------')
your_name=input('Enter your name: ')
check=0
while check==0:
    your_pin=input('Enter your pin: ')
    if your_pin.isdigit()==True and len(your_pin)==4:
        check=1
    else:
        if your_pin.isdigit()==False:
            print('enter pin involving only numbers')
        else:
            print('enter 4-digit pin')
check=0
while check==0:
    your_balance=input('Enter your bank balance: ')
    if your_balance.isdigit()==True and len(your_balance)<6:
        your_balance=int(your_balance)
        check=1
    else:
        if your_balance.isdigit()==False:
            print('enter valid input')
        else:
            print('maximum balance can be 1 lakh exclusive')
bank_account={'name':your_name,'pin':your_pin,'balance':your_balance,'transaction_history': []}
print('')
print(f'Your Name: {your_name}\nYour Pin: {your_pin}\nYour Balance: {your_balance}')
print(f'Your {bank_name} Bank Account is Sucessfully Created \n---------------------------------------------------------------')
print('')
while(1):
    check=0
    while check<3:
        pin_entered=input('Enter your pin: ')
        if pin_entered==bank_account['pin']:
            check=4
        else:
            check+=1
            print(f'The pin you entered is incorrect, you have {3-check} attempts left')
    if check==3:
        print('Please contact customer care')
        exit()
    print('')
    check=0
    while check<3:
        functionality_num=input('HOME PAGE\n-------------------\n1.WithDraw\n2.Deposite\n3.Change Pin\n4.Transaction History\n5.Balance\nEnter the respective number of operation you want to perform: ')
        if functionality_num in '12345':
            check=4
        else:
            check+=1
            print(f'Enter valid input as mentioned you have {3-check} attempts left')
            print('')
    if check==3:
        print('Please contact customer care')
        exit()
    print('')
    if functionality_num=='1':
        check=0
        while check<3:
            withdraw_amount=input('Enter the Amount you want to WithDraw: ')
            if withdraw_amount.isdigit()==True:
                withdraw=int(withdraw_amount)
                if withdraw%100!=0:
                    print('You can WithDraw only in 100s')
                elif withdraw<=bank_account['balance']:
                    bank_account['balance']-=withdraw
                    print(f'{withdraw} Amount is WithDrawn Sucessfully')
                    balance=bank_account['balance']
                    bank_account['transaction_history'].append(f'{withdraw} Amount is WithDrawn Sucessfully and your bank balance is {balance}')
                    check=4
                else:
                    print('Insufficient Funds in your Bank Balance')
            else:
                check+=1
                print(f'Enter valid input as  mentioned you have {3-check} attempts left')
        if check==3:
            print('Please contact customer care')
            exit()
        print('')
    elif functionality_num=='2':
        check=0
        while check<3:
            deposite_amount=input('Enter the Amount you want to Deposite: ')
            if deposite_amount.isdigit()==True:
                deposite=int(deposite_amount)
                if deposite%100!=0:
                    print('You can Deposite only in 100s')
                elif deposite>99999:
                    print('The maximum amount you can Deposite is 1 lakh exclusive')
                else:
                    bank_account['balance']+=deposite
                    print(f'{deposite} Amount is Deposited Sucessfully')
                    balance=bank_account['balance']
                    bank_account['transaction_history'].append(f'{deposite} Amount is Deposited Sucessfully and your bank balance is {balance}')
                    check=4
            else:
                check+=1
                print(f'Enter valid input as  mentioned you have {3-check} attempts left')
        if check==3:
            print('Please contact customer care')
            exit()
        print('')
    elif functionality_num=='3':
        check=0
        while check<3:
            old_pin=input('Enter your old pin: ')
            if old_pin==bank_account['pin']:
                check=0
                new_pin=input('Enter your new pin: ')
                if new_pin.isdigit()==True and len(new_pin)==4:
                    check=0
                    re_enter_new_pin=input('Re enter your new pin: ')
                    if re_enter_new_pin==new_pin:
                        bank_account['pin']=new_pin
                        bank_account['transaction_history'].append(f'You have changed your old pin {old_pin} to new pin {new_pin}')
                        print(f'Your pin has changed to {new_pin} Successfully')
                        check=4
                    else:
                        check+=1
                        print(f'The pin you re entered is wrong, you have {3-check} attempts left')
                else:
                    check+=1
                    if new_pin.isdigit()==False:
                        print(f'Enter pin involving numbers, you have {3-check} attempts left')
                    else:
                        print(f'Pin should be of 4 digits, you have {3-check} attempts left')
            else:
                check+=1
                print(f'The pin you entered is incorrect, you have {3-check} attempts left')
        if check==3:
            print('Please contact customer care')
            exit()
        print('')
    elif functionality_num=='4':
        print('Transaction History: ')
        if len(bank_account['transaction_history'])!=0:
            for i in bank_account['transaction_history']:
                print(i)
        else:
            print('you didnt perform any action')
        print('')
    else:
        balance=bank_account['balance']
        bank_account['transaction_history'].append(f'You checked your balance which is {balance}')
        print(f'Your Bank Balance: {balance}')
        print('')
    check=0
    while check<3:
        repeat=input('1.Home Page\n2.Exit\nEnter the respective number of operation you want to perform: ')
        if repeat=='1':
            print('---------------------------------------------------------------')
            print('')
            check=4
        elif repeat=='2':
            print(f'Thank you {your_name}')
            exit()
        else:
            check+=1
            print(f'Enter valid input as mentioned you have {3-check} attempts left')
            print('')
    if check==3:
        print('Please contact customer care')
        exit()
----------------------------------------------------------------------------------------------------------------------------------------------------------
Generators -> This is a special type of function that generates or return an ITERATOR which one at a time

yield -> it will take a pause and again resume, this is not a normal keyword cannoy be used in normal fuctions
         This is used to produce a value and pause execution
         
next -> this is used to get next value from a generator
        when the value is finished, it will stop the iterator
        
def my_generator():
    yield 1
    yield 2
    yield 3
an=my_generator()
print(next(an))
print(next(an))
print(next(an))

def square_gen(n):
    for i in range(n):
        yield i**2
for val in square_gen(5):
    print(val)

def prime_nums_gen(n):
    for i in range(2,n):
        factors=0
        for j in range(1,i+1):
            if i%j==0:
                factors+=1
        if factors==2:
            yield i
for val in prime_nums_gen(int(input())):
    print(val)

n=int(input('Enter the range: '))
def prime_nums_gen(n):
    for i in range(2,n):
        factors=0
        for j in range(1,i+1):
            if i%j==0:
                factors+=1
        if factors==2:
            yield i
print(f'prime numbers below {n} using generator:',end=' ')
for val in prime_nums_gen(n):
    print(val,end=' ')
print('')
def prime(n):
    for i in range(2,n):
        factors=0
        for j in range(1,i+1):
            if i%j==0:
                factors+=1
        if factors==2:
            print(i,end=' ')
print(f'prime numbers below {n} using functions:',end=' ')
prime(n)

import time
def countdown(n):
    while n>0:
        yield n
        n-=1
for num in countdown(10):
    print(num)
    time.sleep(1) #delay of 1 second of output

Modules
--------
---> A module in apython is simply file that contain python code (Functions, Variables, classes)
---> To use modules, we have to use a keyword called import before the module
---> syntax: import Module_name, to use this: file_name.functionality(arguments)
Types of Modules
-----------------
1. Built-in or Inbuilt
2. User-define modules

User-define modules: this is developed by the user or programmer inside a file of python code and used by called import with filename...
syntax: import(keyword) file_name
        file_name.functionality(arguments)

import surya_module as sm #there is a file in my system named surya_module which contain all these user defined functions of mathematical operations
num1=int(input('Enter num1: '))
num2=int(input('Enter num2: '))
print(f'{num1}+{num2}={sm.add(num1,num2)}')
print(f'{num1}-{num2}={sm.sub(num1,num2)}')
print(f'{num1}*{num2}={sm.mul(num1,num2)}')
print(f'{num1}/{num2}={sm.div(num1,num2)}')
print(f'{num1}//{num2}={sm.int_div(num1,num2)}')
print(f'{num1}%{num2}={sm.mod(num1,num2)}')
print(f'{num1}^{num2}={sm.pow(num1,num2)}')
print(f'{num2}th root of {num1} = {sm.root(num1,num2)}')

Built-in or Inbuilt: Aldready these are comes with installation and they are ready to use in the program. This is developed by the developer
syntax---> import(keyword) module_name
           module_name.functionality

import math
print(math.sqrt(16))

import random
key=random.randint(1,100)
attempts=0
while attempts<5:
    value=int(input('Try to guess the number what computer generated which is between 1 to 100: '))
    if value==key:
        attempts=6
        print('Correct, You Won Hurreh!!!')
    else:
        attempts+=1
        if value>key:
            print(f'The number you entered is greater than the number you should guess, you have {5-attempts} left')
        else:
            print(f'The number you entered is less than the number you should guess, you have {5-attempts} left')
if attempts==5:
    print(f'Better Luck Next Time, the number generated by computer is {key}')

output1:
Try to guess the number what computer generated which is between 1 to 100: 23
The number you entered is less than the number you should guess, you have 4 left
Try to guess the number what computer generated which is between 1 to 100: 50
The number you entered is greater than the number you should guess, you have 3 left
Try to guess the number what computer generated which is between 1 to 100: 30
The number you entered is less than the number you should guess, you have 2 left
Try to guess the number what computer generated which is between 1 to 100: 40
The number you entered is less than the number you should guess, you have 1 left
Try to guess the number what computer generated which is between 1 to 100: 44
Correct, You Won Hurreh!!!

output2:
Try to guess the number what computer generated which is between 1 to 100: 50
The number you entered is less than the number you should guess, you have 4 left
Try to guess the number what computer generated which is between 1 to 100: 70
The number you entered is greater than the number you should guess, you have 3 left
Try to guess the number what computer generated which is between 1 to 100: 60
The number you entered is greater than the number you should guess, you have 2 left
Try to guess the number what computer generated which is between 1 to 100: 65
The number you entered is greater than the number you should guess, you have 1 left
Try to guess the number what computer generated which is between 1 to 100: 62
The number you entered is greater than the number you should guess, you have 0 left
Better Luck Next Time, the number generated by computer is 53

import pyttsx3
engine=pyttsx3.init()
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()
text_to_speech(text=input('Enter Text: '))

import pyttsx3
engine = pyttsx3.init()
def speak_text(text):
    engine.say(text)
user_text = input("enter your message : ").lower( )
name = "user"
if "my name is " in user_text:
    name = user_text.split("my name is ")[-1].strip( )
elif "name is " in user_text:
    name = user_text.split("name is ")[-1].strip( )

if user_text in["hi","hello","hey"]:
    response = "Hello ! How can i help u?"
elif "name" in user_text:
    response = f" Hello (name),how can i help u?"
else :
    response = "sorry ,i didnt understand that"
print(response)
speak_text(response)
engine.runAndWait()

#Greetings_chat_bot:
import pyttsx3
def greetings_chat_bot(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
name=input('Enter your name: ')
greetings_chat_bot(f'Hi {name}')
print(f'hi {name}')
while(1):
    message=input('Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): ').lower()
    if message in ['hi','hello','hey','good morning']:
        response=f'{message} {name}'
    elif message=='how are you ?':
        response='Iam fine, how are you ?'
    elif message=='iam fine':
        response='Good to hear that'
    elif message=='who are you ?':
        response='Iam a Greetings Chat Bot'
    elif message=='exit':
        response=f'Nice talking to you {name}, Bye'
    else:
        response='Sorry I didnt understand that'
    greetings_chat_bot(response)
    print(response)
    if message=='exit':
        break

output: (computer will speak these outputs)
Enter your name: Surya
hi Surya
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): hi
hi Surya
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): hello
hello Surya
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): hey
hey Surya
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): good morning
good morning Surya
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): who are you ?
Iam a Greetings Chat Bot
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): how are you ?
Iam fine, how are you ?
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): iam fine
Good to hear that
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): thanks bot
Sorry I didnt understand that
Enter a message (hi, hello, hey, good morning, who are you ?, how are you ?, Iam fine, exit): exit
Nice talking to you Surya, Bye

Introduction to OOP's
Classes
Objects
Attributes
Methods

OOP's
------
---> object oriented language (OOP) is a style of programming where we model real-world things as objects that contain both data and functions(behaviour)
---> reusablility and scalability 
Class
------
---> class is a blue print or template that defines what kind of data and behaviour a certain type of object will have
---> syntax :
class Class_Name:
    Pass
Object
------
---> This is Instance of class or an object is a real instance created from a class. it is the actual thing that exists in the memory while the program runs
---> syntax:
class class_name:
    Pass
object_name=class_name()
Attributes
-----------
---> these are variables that store data realeted to a class or object
---> syntax:
class class_name:
    def __init__(self,arguments):
        self.argument=value
object_name=class_name()
here each argument is a attribute
self is the keyword of the constructor init

class dog:
    def __init__(self,bread,gender):
        self.bread=bread
        self.gender=gender
dog_1=dog(input('Enter bread name: '),input('Enter gender name: '))
print(f'dogs bread: {dog_1.bread}')
print(f'dogs gender: {dog_1.gender}')

constructor(__init__)
---------------------
---> A constructor is a special method used to initialize the object data
__init__()
self: it is an instance variable

class student:
    def __init__(self, name, ID):
        self.name=name
        self.ID=ID
    def display(self):
        print(self.name,self.ID)
student_1=student('Teja',123)
student_1.display()

Access Specifiers
-----------------
1.Public: we can use it anywhere in the program 
syntax---> name
2.Protected: this is only for internal use
syntax---> _name
3.Private: this one is restricted
syntax---> __name

class some:
    def __init__(self):
        self.public='public'
        self.protected='protected'
        self.private='private'
any=some()
print(any.public)
print(any.protected)
print(any.private)

Encapsulation:
the priciple of binding data such as attributes, methods and variables into a single unit which is a class is called encapsulation, it provides data security
by giving abstraction

class BankAc:
    def __init__(self,balance):
        self.__balance=balance
    def deposite(self,amount):
        self.__balance+=amount
    def get_balance(self):
        return self.__balance
Acc=BankAc(15000)
Acc.deposite(7000)
print(Acc.get_balance())

Inheritance:
This allows child class(subclass) to acquire the attributes and methods of a parent class (base class) this is called inheritence
1. Single Inheritance : using single method of the child class from parent class

super():
this is used to call methods of the parent class from the child class

class parent:
    def display(self):
        print('This is parent method')
class child(parent):
    def display(self):
        super().display()
        print('This is child method')
any = child()
any.display()

2. Multiple Inheritance: A child class inherits from more than one parent class

class Father:
    def skill_1(self):
        print('Father: hard working')
class Mother:
    def skill_2(self):
        print('Mother: Cooking')
class child(Father, Mother):
    def All_skills(self):
        print('Child: Coding')
any=child()
any.skill_1()
any.skill_2()
any.All_skills()

Multi-level: This occurs when a class inherits from a child class, creating a grandparents-->parent-->child in this structure

class Grandparent:
    def Show_Grandparent(self):
        print('Iam Grandparent')
class Parent(Grandparent):
    def Show_Parent(self):
        print('Iam Parent')
class Child(Parent):
    def Show_Child(self):
        print('Iam Child')
any=Child()
any.Show_Grandparent()
any.Show_Parent()
any.Show_Child()

Hierarchial
-----------
-->this occcurs when multiple child classes inherit from a single parent class, this process is called hierarchial

class parent:
    def _parent(self):
        print("I'm Grand parent")

class child_1(parent):
    def _child(self):
        print("I'm a child 1")

class child_2(parent):
    def child_(self):
        print("I'm a child 2")

class child_3(child_1,child_2):
    def child(self):
        print("I'm child")

obj=child_3()
obj._parent()
obj._child()
obj.child_()
obj.child()

hybrid inheritance
------------------
-->This is a combination of two or more types of inheritance,such as single,multiple,
multi-level ,or hirerarchiel all this in a single class...

class parent:
    def _parent(self):
        print("I'm Grand parent")

class child_1(parent):
    def _child(self):
        print("I'm a child 1")

class child_2(parent):
    def child_(self):
        print("I'm a child 2")

class child_3(child_1,child_2,application):
    def child(self):
        print("I'm child")

obj=child_3()
obj._parent()
obj._child()
obj.child_()
obj.child()
obj.app_upgrade()
obj.system_upgrade()
obj.mobile_upgrade()

Polymorphism: this allows a object of diffrent classes to be treated as instance of the same base class, with methods behaving diffrently based on the
actual object type
example:
print(len('python'))
print(len([1,2,3]))

method overloading: this defines multiple methods with the same name but different parameters (numbers, type or order) in the same class

class calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c
cal=calculator()
print(cal.add())
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))

Method overriding: this occurs in the child class, redefining a parent class method with the same signature for runtime.

class animal:
    def speak(self):
        return 'Sound'
class dog(animal):
    def speak(self):
        return 'Woof'
DOG=dog()
print(DOG.speak())

class parents:
    def thitlu(self):
        return 'poramboku'
class mother:
    def thitlu(self):
        return 'vedhavannari'
class father(parents,mother):
    def thitlu(self):
        return 'chethanakodaka'
fahhh=father()
print(fahhh.thitlu())

operator overloading: this is customizes operator like +,- for user-defined classes by implementing special methods...
example: __add__,__sub__

class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,st):
        return someone(self.a+st.a,self.b+st.b)
    def __str__(self):
        return f'({self.a},{self.b})'
any=someone(2,3)
so=someone(5,9)
print(any+so)

Data Abstraction: this hides complex implementation details, exposing only essential features via abstract class or interface.

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
Circle=circle(5)
print(Circle.area())

class Student:
    def __init__(self,name,id_,courses,details={}):
        self.name=name
        self.id_=id_
        self.courses=courses
        self.details={}
    def student_details(self):
        self.details['name']=self.name
        self.details['id']=self.id_
        self.details['courses']=self.courses
        return self.details
    def display(self,add):
        print('Student Details in Codegnan\n----------------------------------\n')
        for i in add:
            print(f'Name: {i["name"]}\nID: {i["id"]}\nCourses: {i["courses"]}\n')
print('Codegnan Institute\n---------------------')
num_students=int(input('Enter the no of students in the institute: '))
add=[]
for i in range(num_students):
    name=input('Enter student name: ')
    id_=input('Enter student id: ')
    courses=[]
    num_courses=int(input('Enter the no of courses student want to opt: '))
    for j in range(num_courses):
        courses.append(input('Enter course name: '))
    obj_student=Student(name,id_,courses)
    add.append(obj_student.student_details())
print('')
obj_student.display(add)

#output:
Codegnan Institute
---------------------
Enter the no of students in the institute: 3
Enter student name: surya
Enter student id: cgvi0009
Enter the no of courses student want to opt: 3
Enter course name: python programming
Enter course name: data structures and algorithm
Enter course name: quantitative aptitude
Enter student name: sowmika
Enter student id: cgvi0010
Enter the no of courses student want to opt: 2
Enter course name: java programming
Enter course name: python programming
Enter student name: anupama
Enter student id: cgvi0011
Enter the no of courses student want to opt: 1
Enter course name: python prgramming

Student Details in Codegnan
----------------------------------

Name: surya
ID: cgvi0009
Courses: ['python programming', 'data structures and algorithm', 'quantitative aptitude']

Name: sowmika
ID: cgvi0010
Courses: ['java programming', 'python programming']

Name: anupama
ID: cgvi0011
Courses: ['python prgramming']

Handling Errors
----------------
try block
---------
---> the try block will test a block of code for errors
try:
    print(b)

except block
------------
---> except block will take care of any errors that occurs in try block
try:
    print(b)
except:
    print('b is not defined')

else block
----------
---> else keyword to define a block of code to be excuted if no error were raised

try:
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
except:
    print('Enter an Integer')
else:
    print(f'sum of the numbers: {a+b}')

finally block
-------------
---> This block will execute either try block have any error or no error

try:
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
except:
    print('Error, enter an Integer')
else:
    print('No Error')
finally:
    print(f'sum of the numbers: {a+b}')

try:
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
    result=a/b
except ValueError:
    print('Error, enter an Integer')
except ZeroDivisionError:
    print('Error, cannot divide by zero')
else:
    print(f'quotient: {result}')
finally:
    print('The program is completed')

File handling
-------------
---> File handler is an object of file to maintain several functions of file such as creating, reading, writing and update also deleting the file

how to open a file
------------------
open(): this helps to open file, it takes 2 parameters and in this we have to close the file by calling close() function after program...
1.file name
2.mode

Modes ('r','w','a','x','t')
---------------------------
1. 'r'-- read
-------------
--> to read the file we will this mode and if the file doesnt exist. it will throw the error

any=open('codegnan.txt','r')
print(any.read())
any.close()

2. 'w'-- write
--------------
--> to write the text into the file we will use this mode and it will create a file if it doesnt exist
--> it will over write new text with old text in the file

any=open('codegnan.txt','w')
any.write('\nThis is write mode')
any.close()

any=open('writemode.txt','w')
any.write('I opened this file using write mode')
any.close()

3.'a'-- append
--------------
--> to add the text into the file this is used and it will create the file if it doesn't exist
--> it will write text at end

4. 'x'-- create
---------------
--> this is used to create the file, but if the file is aldready in the system it raise error

To read a file
--------------
1. read()
---------
--> this method can read the entire file chunk by chunk we can also specify the size
2. readline()
-------------
--> this method can only read one line at a time in a file
3. readlines()
--------------
--> this method can read the entire file and return into list with each line is one index in the list

with open('codegnan.txt','r') as any:
    print(any.read())

Regular Expression (RegEx)
--------------------------
--> This regular expression or RegEx is a sequence of characters that forms a searching pattern.
--> To use this we have to import re, which will unlock the package

Functions
---------
1.findall --> by using this function, it will find all sequence in the string
syntax--> re.findall('metachar',variable_name)
2.search --> by using this function, it will only find first sequence in the string
syntax--> re.search('metachar',variable_name)

import re
any='python is a language'
so=re.findall('a',any)
se=re.search('a',any)
print(so)
print(se)

Metacharacters
--------------
metacharacters are used to form searching pattern

1.[]--> In this meta character we can search for [a-z],[A-Z],[0-9]

import re
any='this regular expression or RegEx is a sequence of characters that forms a searching pattern'
so=re.findall('[a-z]',any)
print(so)

import re
any='this regular expression or RegEx is a sequence of characters that forms a searching pattern'
so=re.findall('[aeh]',any)
print(so)

import re
any='#this regular expression 7or RegEx is a sequence of characters 2that forms a searching pattern'
so=re.findall('[a-z0-9]',any)
so1=re.search('[a-z0-9]',any)
so2=re.search('[0-9]',any)
print(so)
print(so1)
print(so2)
print(so1)

2.dot(.)--> this meta character wil form a searching pattern as it will take any single character for (.)

import re
we='hello everyone'
the=re.findall('h...o',we)
thing=re.search('he..o',we)
print(the)
print(thing)

3.^ --> this is used to find the is string is starting with the sequence or not

import re
how='this regular expression or RegEx is a sequence of characters that forms a searching pattern'
who=re.findall('^this reg',how)
then=re.search('^this reg',how)
print(who)
print(then)

4.$ --> this is used to the string is ending with the sequence or not

import re
out='This is used to find the string is ending with the sequence'
one=re.findall('sequence$',out)
two=re.search('sequence$',out)
print(one)
print(two)

5.* --> this meta character will form a searching pattern as it will take any zero or more character for (*)

import re
teja='this meta character will form a searching pattern as it will take any zero or more character for (*)'
surya=re.findall('c.*i',teja)
raju=re.findall('t.*',teja)
shyam=re.search('t.*',teja)
mohan=re.findall('.*er,teja)
harshit=re.search('.*or,teja)
print(surya)
print(raju)
print(shyam)
print(mohan)
print(harshit)

6.+ --> this meta character will form a seaching pattern as it will take any one or more character for (+)

import re
teja='this meta character will form a seaching pattern as it will take any one or more character for (+)'
gk=re.findall('an.+y',teja)
mk=re.findall('t.+',teja)
koll=re.search('t.+',teja)
print(gk)
print(mk)
print(koll)

7. ? --> this meta character will form a seaching pattern as it will take any zero or one character for (?)

import re
any='this meta character will form a seaching pattern as it will take any one or more character for (+)'
an=re.findall('th.?s',any)
print(an)

import re
any='this is meta character'
an=re.search('Th.?',any)
print(an)

8.{} --> this meta character will form a seaching pattern as it will take any zero or one character

import re
any='this meta character will form a seaching pattern as it will take any zero or one character'
an=re.findall('.{25}ro',any)
an_=re.findall('me.{25}',any)
an__=re.findall('.{25}',any)
print(an)
print(an_)
print(an__)

9. | --> this meta character will form a searching pattern as it consider right or left any string is present or not for (|)

import re
any='This meta character will form'
an=re.findall('that|will',any)
print(an)

Special sequence
----------------
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning

1. \A --> Returns a match if the specified characters are at the beginning of the string

import re
txt='the rain in spain'
x=re.findall('\Athe',txt)
print(x)

2. \b --> Returns a match where the specified characters are at the beginning or at the end of a word

import re
txt='The rain in Spain'
x=re.findall(r'\bSpain',txt)
print(x)

3. \d --> Returns a match where the string contains digits(numbers from 0-9)

import re
txt='the rain in 56 spain'
x=re.findall('\d',txt)
print(x)

4. \D --> Returns a match where the string DOES NOT contain digits

import re
txt='the rain in 67 spain'
x=re.findall('\D',txt)
print(x)

5. \s --> Returns a match where the string contains a white space character

import re
txt='The rain in Spain'
x=re.findall('\s',txt)
print(x)

6. \S --> Return a match where the string DOES NOT contain a white space character

import re
txt='The rain in spain'
x=re.findall('\S',txt)
print(x)

Time and Date
-------------
%d---> Day
%m---> Month
%Y---> Year
%H---> Hour
%M---> Minutes
%S---> seconds
%p---> AM/PM
%A---> Day name
%B---> Month name

import datetime
now=datetime.datetime.now()
print(now)

import datetime
today=datetime.date.today()
print(today.strftime('%d-%m-%Y'))
print(today.strftime('%A'))
print(today.strftime('%B'))
now=datetime.datetime.now()
print(now.strftime('%H:%M:%S %p'))
print(datetime.datetime.now())

import re

def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'   
    return re.fullmatch(pattern, name)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.[a-z])(?=.[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)


def main():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    if not validate_name(name):
        print("Invalid Name")

    if not validate_email(email):
        print("Invalid Email")

    if not validate_phone(phone):
        print("Invalid Phone Number")

    if not validate_password(password):
        print("Invalid Password")


if __name__== "__main__":
    main()
'''
