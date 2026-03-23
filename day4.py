'''
if statement -> this (if statement) is used to check any condition, if the condition becomes true then it will enter inside the (if statement)

age=int(input("Enter your age: "))
if age>=18:
    print("your age is 18 or above")

student_attendance=int(input("please enter your sem attendance: "))
if student_attendance>=75:
    print("you can directly sit in the sem exam")
    
#my own example-1:
exam_score=float(input("please enter your exam score: "))
if exam_score>=80:
    print("you are selected for the interview")
    
#my own example-2:
interview_marks=float(input("please enter your interview marks: "))
if interview_marks>=90:
    print("you are selected for the job")

#if-else statement-> this also caled as fall back statement which only execute when the(if statement) becomes false

age=int(input("Enter your age: "))
if age>=18:
    print("you can vote")
else:
    print(f'you cannot vote and have to wait {18-age} years to vote')

total_am=int(input("Enter the total shopping money: "))
if total_am>=149:
    print("No deliver cost")
else:
    print(f'Add {149-total_am} to your cart')

#my own example-3:
bill=float(input("Enter your bill amount: "))
if bill>=1500:
    bill*=0.9
    print(f'Your bill is greater than or equal to 1500, so 10% discount is applied on your bill which makes up your bill amount to {bill}')
else:
    print(f'your bill is less than 1500, so 10% discount is not applied on your bill hence your bill amount is {bill}')

#if-elif-else statement (if+else)--- in the elif part, I can one more condition and by using multiple elif's we can add multiple conditions

student_marks=int(input("Enter your marks: "))
if student_marks>=90:
    print("You got A+ grade")
elif student_marks>=80:
    print("You got A grade")
elif student_marks>=70:
    print("you got B+ grade")
elif student_marks>=60:
    print("you got B grade")
elif student_marks>=50:
    print("you got C grade")
elif student_marks>=40:
    print("you got D grade")
else:
    print("your Fail")

#my own example-4:
num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
operator=input("Enter the symbol of operator (+,-,*,/): ")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
else:
    print(num1/num2)

num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))
operator=int(input("Enter your choice\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
if operator==1:
    print(num1+num2)
elif operator==2:
    print(num1-num2)
elif operator==3:
    print(num1*num2)
else:
    print(num1/num2)

user_choice=int(input("please enter any number: "))
if user_choice%2==0:
    print(f'{user_choice} is a even number')
else:
    print(f'{user_choice} is a odd number')

#my own example-5:
num=float(input("Enter a number: "))
if num<0:
    print(f'{num} is a negative number')
elif num>0:
    print(f'{num} is a positive number')
else:
    print("The number you entered is Zero")
'''
