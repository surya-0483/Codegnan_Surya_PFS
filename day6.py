'''
time=input("Enter 24hours time: ").split(":")
if int(time[0])>=13:
    print(f'{time[0]}:{time[1]} converted into 12hours time is {int(time[0])-12}:{time[1]}pm')
else:
    print(f'{time[0]}:{time[1]} converted into 12hours time is {time[0]}:{time[1]}am')

list -> collection of diffrent items or diffrent data types in side the [], which are seperated by,
eg -> [1,'name',[1,2,'teja']]

list_1=[1,2,3,"python",[1,2,["python","java"],"language"]]
print(list_1[4][2][0][3]) #output: h
print(list_1[3][1]) #output: y
print(list_1[4][2][1][0]) #output: j

Methods of List
---------------
append() -> this method is used to add new items at the last index of the list
syntax -> variable_name.append(item)
list_2=[1,2,3,4,5]
list_2.append(69)
print(list_2) #[1,2,3,4,5,69]
list_2.append([96,21])
print(list_2) #[1,2,3,4,5,69,[96,21]]

extend() -> this method is used to add items to list in the last index, where each item is each index in the list
syntax -> variable_name.extend(items)
list_3=[1,2,3,4,5]
list_3.extend(69)
print(list_3) #[1,2,3,4,5,69]
list_3.extend([96,21])
print(list_3) #[1,2,3,4,5,69,96,21]
list_3.extend("surya")
print(list_3) #[1,2,3,4,5,69,96,21,'s','u','r','y','a']

remove() -> this method will directly delete the item or value from the list which is in the list
synatx -> variable_name.remove(item in the list)
list_4=[1,2,3,4,5]
list_4.remove(3)
print(list_4) #[1,2,4,5]

pop() -> this method will delete the item or value based on index position
syntax -> variable_name.pop(index value)
list_5=[23,"python",56,89,6]
list_5.pop(1)
print(list_5) #[23,56,89,6]

notice: list is mutable and string is immutable
mutable -> i can directly modify on that purticular variable
immutable -> i cannot modify directly on the variable, i should assign to another variable to modify
'''
