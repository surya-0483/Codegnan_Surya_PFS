'''
Job selection criteria of a B.Tech student: This is a checker task involving assignment, relational, logical and arthematic operators of python.

question: Initially the student should have attendence and overall btech percentage more than or equal to 80% with each semester grade points more than or
equal to 8, then the student is eligible to write the exam and attend interview for the job. So the students name, students attendence and students all
8 semesters grade points should be taken as user input and should be verified whether the student is eligible for writting exam and attending interview or
not. if the student is eligible, display a message that student [student name] is eligible for exam and interview, if the student is not eligible, display
a message that student [student name] is not eligible for exam and interview. Finally the eligible students should score more than or equal to 80 marks in
the written exam and the interview to get selected for the job. So the students written exam score & interview score should be taken as user input and
should be verified whether the student is selected for the job or not. if the student is selected, display a message that student [student name] is
selected for the job, if the student is not selected display a message that student [student name] is not selected for the job.

notice: cgpa = sum of all 8 semesters grade points / 8
overall btech percentage = cpgpa * 9.5

code:
'''

Name=input("Enter students full name: ")
Attendance=float(input(f'Enter {Name} attendance percentage: '))
sgpas=[]
for i in range(1,9):
    sgpa=float(input(f'Enter semester{i} grade points: '))
    sgpas.append(sgpa)
Attendance_check=0
if Attendance<80: #comparision operator
    Attendance_check=1
sgpas_check=[]
sgpa_total=0
for i in range(8):
    sgpa_total+=sgpas[i] #assignment operator
    if sgpas[i]<8: #relational operator
        sgpas_check.append(i)
cgpa=sgpa_total/8 #arthematic operator
btech_percentage=cgpa*9.5 #arthematic operator
print("")
print("Overall Cgpa:",cgpa)
print(f'Overall  B.Tech percentage: {btech_percentage}%')
print("")
print("------------------------------------------------------------")
print("")
eligibility_check=0
if Attendance_check==1 or len(sgpas_check)>0 or btech_percentage<80: #logical operator
    eligibility_check=1
    print(f'{Name} is not eligible for exam and interview because :')
if Attendance_check==1:
    print("the attendance is less than 80%")
if len(sgpas_check)>0: #comparision operator
    string=""
    for i in sgpas_check:
        string=string+str(i)+" " #assignment operator
    print(f'semester {string}grade points are less than 8')
if btech_percentage<80: #relational operator
    print("Overall btech percentage is less than 80%")
if eligibility_check==0:
    print(f'{Name} is eligible for exam and interview')
if eligibility_check==1:
    exit(0)
print("")
print("------------------------------------------------------------")
print("")
Exam_score=float(input("Enter exam score: "))
Interview_score=float(input("Enter interview score: "))
print("")
print("------------------------------------------------------------")
print("")
if Exam_score>=80 and Interview_score>=80: #logical operator
    print(f'{Name} is selected for the job')
else:
    print(f'{Name} is not selected for the job beacuse:')
    if Exam_score<80: #relational operator
        print("Exam score is less than 80")
    if Interview_score<80: #relational operator
        print("Interveiw score is less than 80")

'''
output1:

Enter students full name: surya jaggumantri
Enter surya jaggumantri attendance percentage: 86
Enter semester1 grade points: 8.56
Enter semester2 grade points: 8.71
Enter semester3 grade points: 8.23
Enter semester4 grade points: 8.83
Enter semester5 grade points: 9.12
Enter semester6 grade points: 9.53
Enter semester7 grade points: 9.76
Enter semester8 grade points: 10

Overall Cgpa: 9.092500000000001
Overall  B.Tech percentage: 86.37875000000001%

------------------------------------------------------------

surya jaggumantri is eligible for exam and interview

------------------------------------------------------------

Enter exam score: 88.45
Enter interview score: 82

------------------------------------------------------------

surya jaggumantri is selected for the job


output2:

Enter students full name: surya jaggumantri
Enter surya jaggumantri attendance percentage: 75
Enter semester1 grade points: 8.21
Enter semester2 grade points: 8.1
Enter semester3 grade points: 7.5
Enter semester4 grade points: 7.63
Enter semester5 grade points: 8.56
Enter semester6 grade points: 9
Enter semester7 grade points: 7.2
Enter semester8 grade points: 8

Overall Cgpa: 8.025
Overall  B.Tech percentage: 76.2375%

------------------------------------------------------------

surya jaggumantri is not eligible for exam and interview because :
the attendance is less than 80%
semester 2 3 6 grade points are less than 8
Overall btech percentage is less than 80%


output3:

Enter students full name: surya jaggumantri
Enter surya jaggumantri attendance percentage: 84.7
Enter semester1 grade points: 8
Enter semester2 grade points: 9
Enter semester3 grade points: 10
Enter semester4 grade points: 8.1
Enter semester5 grade points: 9.1
Enter semester6 grade points: 8.5
Enter semester7 grade points: 9.75321
Enter semester8 grade points: 9.52

Overall Cgpa: 8.99665125
Overall  B.Tech percentage: 85.46818687499999%

------------------------------------------------------------

surya jaggumantri is eligible for exam and interview

------------------------------------------------------------

Enter exam score: 69
Enter interview score: 99

------------------------------------------------------------

surya jaggumantri is not selected for the job beacuse:
Exam score is less than 80

'''
