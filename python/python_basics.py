rent=1500
gas=400
groceries=600
print(rent)

total=rent+gas+groceries
print(total)

name="anand"
print(name)

##########################################

print(5+4)
print(5-4)
print(5*4)
print(5/4)
print(5**4)

print(round(5/4))
print(round(577/3, 4))

##########################################
#Strings
#Strings are immutable in python
text="Hello Hai"
print(text[0])
print(text[1])
print(text[0:4])
print(text[:4])
print(text[3:])
text1="Hello AP"
text2="Hello 'AP'"
text3='Hello "AP"'
text4="""
Hi 
Hello
APP
"""
print(text1)
print(text2)
print(text3)
print(text4)

print(text1 + text2)

print("hello" + str(2))

##########################################
#Lists
list = ['bread', 'paste', 'fruits', 'icecream']
print(list)
print(list[0])
print(list[0:2])
print(list[:3])
print(list[2:])

list[2]='veggies'
print(list)
print(list[-1])

list.append('butter')
print(list)

list.insert(1,'electronics') #Insert at a specific location
print(list)

bathroom=['soap', 'shampoo']
items = list+bathroom
print(items)

#String + List won't work

print(len(items))

print('soap' in items)
##########################################
#Pycharm
#Create a new .py file and run it
#Debug mode and step over
##########################################
#Input

# i1=input("Enter the number: ")
i1=5
num=int(i1)
if num%2==0:
    print("Number is even")
else:
    print("Number is odd")

print(4==4)
print(4!=4)
print(4>=4)
print(4<=4)
print(4<5)
print(4>5)
print(4>5 and 6<7)
print(4>5 or 6<7)

indian=['puri', 'idly', 'dosa', 'upma']
chinese=['egg role', 'noodles', 'soup', 'fried rice']
italian=['pizza', 'pasta', 'salad', 'bread']

# dish=input("Enter the dish")
dish='idly'

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else: 
    print("No idea about the dish", dish)
##########################################
#For Loop

exp=[1000, 1500, 4500, 5000, 3000]

total=exp[0] + exp[1] + exp[2] + exp[3] + exp[4]

print(total)

total=0

for i in exp:
    total+=i

print(total)

for i in range(1,11):
    print(i)

for i in range(len(exp)):
    print("Month", i+1, "Expense:", exp[i])

locations=['delhi', 'mumbai', 'hyderabad', 'guntur']

for i in range(len(locations)):
    if locations[i] == 'guntur':
        print("Found at", i)
        break
    else:
        print("Not Found at", i)

for i in range(len(locations)):
    if locations[i] == 'guntur':
        print("Found at", i)
        continue
    else:
        print("Not Found at", i)


#While loop
i=0
while i < 6:
    print(i)
    i+=1

#Functions
#Modular, Readable

def sum(a,b):
    total=a+b
    return total

n=sum(5,6)
print("Total We got:", n)

#Named arguments sum(b=6, a=5)
#Default arguments def sum(a,b=0)
#Positional arguments sum(4,5)
#Local Variables vs Global Variables

#Comments """  """

##########################################
# List = All values have similar meaning (Homogeneous) 
# Tuple = all values have different meaning (heterogenous) and immutable
tpl=(4,7)
print(tpl[0])
print(tpl[1])
# tpl[0] = 4
print(tpl[0])
# Dictionary
d = {"anand": 456, "subbu": 567, "pra": 666}

print("anand" in d)
print("anand1" in d)

for i in d:
    print(i)

for i in d:
    print(i, d[i])    

for i, j in d.items():
    print(i, j)

##########################################
# import matplotlib
# pip install matplotlib
# PyPi =Python package Index
# pip unintall matplotlib

##########################################
# Modules
# Reusing something written by someone else
import math
print(math.sqrt(5))
print(math.pi)
print(math.log10(5))
print(math.floor(5.6))
print(math.ceil(5.6))

import calendar
cal=calendar.month(1991, 7)
print(cal)
print(calendar.isleap(1991))

#Python Module Index 

# Write a module
# functions.py
def calc1_func():
    print("Function1")

def calc2_func():
    print("Function2")
    
# Importing modules in 3 ways
# import functions
# functions.calc_func1
# functions.calc_func1

# If we move the functions to a different directory
# import modules.functions as f

# import sys
# sys.path.append("/modules_path")
# import functions as f

##########################################
#JSON
# Light weight when compared to XML

book = {}

book['tom']={
    'name': 'tom',
    'addr': 'california',
    'phone': 408
}
book['yom']={
    'name': 'yom',
    'addr': 'texas',
    'phone': 469
}

# print(book)

import json
s=json.dumps(book) # String
print(s) 

with open('book.txt', 'w') as f:
    f.write(s)

f=open('book.txt', 'r')
s=f.read()
print(type(s))
print(s)
book=json.loads(s)
print(type(book))
print(book)
##########################################
# __main__, predefined variables, Entry Point for Python

print(__name__)

if __name__ == '__main__':
    a=sum(5,7)
    print(a)

# If we call the main module from some other module then it prints something else
# Area to main method then __name__ would be __area__
##########################################
# Exception Hanlding
try:
    x=4/0
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

##########################################
#Class
    # properties, methods

    #name, age, occupation
    #speaks, do work

class Human:
    def __init__(self, name, occupation, age):
        self.name=name
        self.age=age
        self.occupation=occupation

    def do_work(self):
        if self.occupation == 'tennis':
            print("Plays Tennis", self.name)
        elif self.occupation == 'cricket':
            print("Plays Cricket", self.name)

    def speaks(self):
        print("How are you", self.name)

h1=Human('anand', 'tennis', 30)
h2=Human('chandu', 'cricket', 25)
print(h1.name)
h1.do_work()
h2.do_work()
h1.speaks()

################################################


