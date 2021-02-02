#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1 
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

filtered_List = filter(lambda x: x != '' and x != ' ' and x != '  ' and x != '   ', places)

new_places = list(filtered_List)

print(new_places)


# In[ ]:


#2

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

#what I tried first thinking I could later turn the lists into a dictionary ↓
#split_List = {}
#for i in authors:
    #split_List = i.split(" ")
    #print(split_List)

authors.sort(key=lambda author_name: author_name.split(" ")[-1].lower())
print(authors)


# In[ ]:


#3

places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

celsius_value = [32, 12, 44, 29]
farhrenheit_conversion = list(map(lambda x: (float(9)/5)*x + 32, celsius_value))
print(farhrenheit_conversion)


# In[ ]:


#4

def fibonacciNums(num):
    if num <= 0:
        print("fibonacciNums(0) = 0")
        return num
    else:
        print(f"fibonacciNums{num}) = {num} - fibonacciNums({num + 0})")
        return num - fibonacciNums(num - 1)  
fibonacciNums(10)

