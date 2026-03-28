'''
Dictionaries -> one of the collection in python which stores data as key:value pair
sbi_surya={'name':'surya','role':'student',6:8}
print(sbi_surya)
keys -> keys are unique and we can only give immutable data types in the keys
values -> we can give all data types (mutable and immutable) which includes duplicates
{}

methods in dictionary
---------------------
keys() -> this method is used to get all keys from the dictionary
values() -> this method is used to get all the values from the dictionary
clear() -> this method is used to delete the dictionary
sbi_surya={'name':'surya','role':'student',6:8}
synatx -> variable_name.method()
print(sbi_surya.keys())
print(sbi_surya.values())
print(sbi_surya.clear()) #output: None
sbi_surya.clear()
print(sbi_surya) #output: {}


set{} -> set data type is a unordered collection and it never allow duplicates
methods in sets
---------------
union -> this is used to add or get two different sets without duplicates
intersection -> this method is used to find out common items from both the sets
difference -> this method is used to find the different once from the second set
any={1,2,3,4}
so={4,5,6}
print(any.union(so))
print(any.intersection(so))
print(any.diffrence(so))
any.pop()
print(any) #output={2,3,4}
pop() method in sets will remove first element in set and in list will remove last element in list

my_details={"name":"Surya","pin":"011971","ATM":"SBI"}
pin=input("Enter pin number: ")
if pin in my_details["pin"]:
    print(f'{pin} is a valid pin')
else:
    print(f'{pin} is not a valid pin')

sentence='python is a programming language'
count=0
for i in sentence:
    if i=="p":
        count+=1
print(count)

sentence="python is a programming language"
print(sentence.count(" "))
'''
