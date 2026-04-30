'''
#DATA ANALYSIS

#Why this is needed ---this is critical because it converts raw data into actionable insights , enabling information to make decisions easy and improve operational efficiency


1.Decision making
2.improved operational efficiencey
3.customer understandability
4.market insights
5.risk management
6.data driven strategies


#LINECHART

import matplotlib.pyplot as plt
x=[200,40,60,80]
y=[1,2,3,4]
plt.plot(y,x)
plt.show()

#BAR GRAPH

import matplotlib.pyplot as plt
plt.bar(["POGO","CN","KUSHI"] , [4,9,5])
plt.show()

#PIE CHART

import matplotlib.pyplot as plt
plt.pie([35,15,50] , labels =["surya","kartheek","varshini"])
plt.show()

#HISTOGRAM

import matplotlib.pyplot as plt
plt.hist([23,15,78,12])
plt.show()

#NUMPY

Numpy which is numerical python is the fundamental open source library for scientific computing in python , providing high performance , N-dimensional arrays
objects(ndarray) ,
---- this enables efficient numerical computation with linear algebra and data manipulation , also serving as the basis for tools like tensorflow and scipy

import numpy as np
arr= np.array([1,2,3])
print(arr - 1)

#PANDAS

this pandas is used for handling structured data in table format

import pandas as pd
data = {"Name": ["harshith","mohan"] ,"Marks":[89,75]}
any=pd.DataFrame(data)
print(any)


import matplotlib.pyplot as plt
plt.bar([2024,2025,2026] , [67,89,50], color="yellow")
plt.title("car sales")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()

import matplotlib.pyplot as plt
plt.pie([40,15,35],labels=['backend(python)','frontend(HTML,CSS)','framework(flask)','library(Numpy,Pandas,Matplotlib)'])
plt.tittle('ATM Application(Project)')
plt.legend(['sai','akash','abdul'])
plt.show()

import matplotlib.pyplot as plt
plt.scatter([1,2,3,4] ,[200,400,100,800],color="yellow",s=300)
plt.title("Swift car sales")
plt.xlabel("years")
plt.ylabel("Number of sales")
plt.show()
'''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()

except requests.exceptions.RequestsException as e:
    print("Error Fetching data:",e)
    exit()
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]

    #Get raw price text
    price_text = book.find("p",class_="price_color").text
    price = float(re.findall(r'\d+\.\d+',price_text)[0])

    names.append(name)
    prices.append(price)

df = pd.DataFrame({
    "Book Name": names,
    "Price": prices
    })

print("\n Table Data:\n")
print(df.head())

#save to csv
df.to_csv("books_data.csv", index=False)
print("\n CSV file 'books_data.csv' created successfully!")

#Data Visualization
plt.figure()
plt.bar(names[:10], prices[:10]) # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()
