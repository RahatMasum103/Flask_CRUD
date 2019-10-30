# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 02:09:46 2019

@author: APU
"""

def binary_search(arr, low, high, element):
    while (low < high ):
        mid = int(low + (high-1)/2)
        print (mid)
        if (element == arr[mid]):
            return element
        elif (element < arr[mid]):
            high = mid - 1
        else:
            low = mid +1
    return -1

input_array = [2, 5, 15, 20, 25]
size_array = len(input_array)
print ("Array Length",size_array)

print (input_array[0])

x = 5
result = binary_search(input_array, 0, size_array-1, x)

if (result !=-1):
    print ("Element %d found" % result)
else:
    print ("Element not found")
    
for i in range(2,size_array):
    print (input_array[i])
    
b = lambda a : a + 10
print(b(5))

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print (thisdict['model'])

b = "Hello, World!"
print(b[2:5])

s = b.replace(' ','')
print (s.split('e'))

class myClass:
    def __init__(self,x):
        self.x = x   
        
    def show(self):
        print (self.x)
    
p = myClass(5)
p.show()
print (p.x)

str = "hello"

it_ele = iter(str)
print (next(it_ele))

import re

txt = "The rain in Spain"
x = re.search("^T.*n$", txt)

print(x)

class Person:
    def __init__(self,name):
        self.name=name
    
    def isPerson(self):
        return False

class Employee(Person):
    def __init__(self,name):
        self.name = name
        
    def isPerson(self):
        return True
    
p1 = Person('Apu')
print (p1.isPerson())

p2 = Employee("X")
print (p2.isPerson())

dict = {1:'a', 2:'b', 3:{30:'c',40:'d'},4:[1,2,3,4]}

print(dict[3][40])

print (dict[4][0])
del dict[2]
print (dict)