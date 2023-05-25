#!/usr/bin/env python
# coding: utf-8

# In[3]:


list = [1, 2, 3, 4]
a= [(val, pow(val, 3)) for val in list]
print(a)


# In[27]:


from collections import OrderedDict
 
dict = {'ram': '10', 'raj': '9',
        'sanjay': '15', 'jai': '2', 'sita': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)


# In[7]:


import random as rn
dict = {}
x, y, z = 10, 20, 30
dict[x, y, z] = x + y - z;
x, y, z = 5, 2, 4
dict[x, y, z] = x + y - z;
print(dict)


# In[8]:


def returnSum(Dict):
    list = []
    for i in Dict:
        list.append(Dict[i])
    final = sum(list)
    return final
dict = {'a': 10, 'b': 20, 'c': 30}
print("Sum :", returnSum(dict))


# In[9]:


import sys
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Name1": "Raj", "Name2": "John", "Name3": "Ram"}
dic3 = {1: "Horse", 2: "Tiger", 3: "Fox", 4: "Lion"}
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")


# In[10]:


test_set = set("Hello")
for val in test_set:
    print(val)



# In[4]:


s={1,2,3,4,5}
print("Maximum of the set: ",max(s))


# In[3]:


s={1,2,3,4,5}
print("Minimum of the set: ",min(s))



# In[2]:


list=['Hello','Python','World']
list.remove('Python')
print(list)


# In[6]:


set1={1,2,3,4,5}
set2={5,6,7,8,9}
for i in set1:
    for j in set2:
        if i==j:
            print("Element common is:", i)


# In[7]:


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("matrix is:")
for i in range(1, len(matrix)):
    matrix[i] = matrix[0]

print(matrix)


# In[8]:


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()


# In[10]:


elements = [1, 2, 3, 2, 1, 3, 4, 5, 4, 5, 5]
element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
num_rows = max(element_counts.values())
num_cols = len(element_counts)
matrix = [[None] * num_cols for _ in range(num_rows)]
for col, element in enumerate(element_counts):
    count = element_counts[element]
    for row in range(count):
        matrix[row][col] = element
for row in matrix:
    print(row)


# In[11]:


matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))
row_sums = [sum(row) for row in zip(*matrix)]
print("Row-wise sums:")
for sum_value in row_sums:
    print(sum_value)


# In[13]:


def evenmatrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1

    return matrix
n = 4
result = evenmatrix(n)
for row in result:
    print(row)


# In[28]:


def fun(a, b):
    return a**b
   
import inspect 
print(inspect.signature(fun)) 


# In[17]:


name = "Yesh"
age = 18
city = "Pondy"

print(name, age, city)


# In[19]:


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)
base =int(input("Enter the base: "))
exponent =int(input("Enter the power: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")


# In[23]:


class grade:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return str((self.a, self.b))
g= [grade("ram", 'a'),
       grade("ravi", 'b'),
       grade("raj", 'c'),
       grade("mani", 'd'),
       grade("goku", 's')]
print(sorted(g, key=lambda x: x.b))


# In[24]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Yesh", age=18, city="Pondy")


# In[ ]:




