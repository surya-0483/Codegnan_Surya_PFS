'''
#Type conversions:

#int conversions:
a=int(input("Enter a Number: ")) #input=5
print(type(a)) #output=<class 'int'>
print(a) #output=5
#int to float:
b=float(a)
print(type(b)) #output=<class 'float'>
print(b) #output=5.0
#int to complex:
c=complex(a)
print(type(c)) #output=<class 'complex'>
print(c) #output=(5+0j)

#float conversions:
d=float(input("Enter a Number: ")) #input=5.0
print(type(d)) #output=<class 'float'>
print(d) #output=5.0
#float to int:
e=int(d)
print(type(e)) #output=5
print(e) #output=<class 'int'>
#float to complex:
f=complex(d)
print(type(f)) #output=<class 'complex'>
print(f) #output=(5+0j)

#complex inputs cannot be converted into int and float
'''

#Ration bill fee calculator case study on numeric data types:
print("Rashion Bill :")
print("------------------------------------------------------")
dal_price=int(input("Enter the amount of dal per kg: "))
dal_quantity=float(input("Enter quantity of dal you want to purchase in kg: "))
sugar_price=int(input("Enter the amount of sugar per kg: "))
sugar_quantity=float(input("Enter quantity of sugar you want to purchase in kg: "))
oil_price=int(input("Enter the amount of oil per liter: "))
oil_quantity=float(input("Enter quantity of oil you want to purchase in liters: "))
soap_price=int(input("Enter the amount of one soap: "))
soap_quantity=float(input("Enter no of soaps you want to purchase: "))
wheat_floor_price=int(input("Enter the amount of wheat floor per kg: "))
wheat_floor_quantity=float(input("Enter quantity of wheat floor you want to purchase in kg: "))
print("------------------------------------------------------")
print("amount of dal per kg: ",dal_price)
print("quantity of dal you purchased in kg: ",dal_quantity)
print("amount of sugar per kg: ",sugar_price)
print("quantity of sugar you purchased in kg: ",sugar_quantity)
print("amount of oil per liter: ",oil_price)
print("quantity of oil you purchased in liters: ",oil_quantity)
print("amount of one soap: ",soap_price)
print("no of soaps purchased: ",soap_quantity)
print("amount of wheat floor per kg: ",wheat_floor_price)
print("quantity of wheat floor you purchased in kg: ",wheat_floor_quantity)
print("------------------------------------------------------")
print("Total Bill: ",(dal_price*dal_quantity)+(sugar_price*sugar_quantity)+(oil_price*oil_quantity)+(soap_price*soap_quantity)+(wheat_floor_price*wheat_floor_quantity))

'''

output:

Rashion Bill :
------------------------------------------------------
Enter the amount of dal per kg: 150
Enter quantity of dal you want to purchase in kg: 2
Enter the amount of sugar per kg: 60
Enter quantity of sugar you want to purchase in kg: 1
Enter the amount of oil per liter: 120
Enter quantity of oil you want to purchase in liters: 3
Enter the amount of one soap: 50
Enter no of soaps you want to purchase: 5
Enter the amount of wheat floor per kg: 50
Enter quantity of wheat floor you want to purchase in kg: 2
------------------------------------------------------
amount of dal per kg:  150
quantity of dal you purchased in kg:  2.0
amount of sugar per kg:  60
quantity of sugar you purchased in kg:  1.0
amount of oil per liter:  120
quantity of oil you purchased in liters:  3.0
amount of one soap:  50
no of soaps purchased:  5.0
amount of wheat floor per kg:  50
quantity of wheat floor you purchased in kg:  2.0
------------------------------------------------------
Total Bill:  1070.0

'''
