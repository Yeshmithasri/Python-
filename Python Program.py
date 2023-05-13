#!/usr/bin/env python
# coding: utf-8

# In[33]:


print("Hello World")


# In[2]:


a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=a+b
print("the sum is",c)


# In[3]:


a=int(input("Enter first number"))
b=int(input("Enter second number"))
print(a,b)
a=a+b
b=a-b
a=a-b
print("After swapping")
print(a,b)


# In[1]:


n=float(input("Enter the values in kilometers"))
m=n*0.621371
print("In miles=",m)


# In[4]:


n=int(input("Enter a number"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")


# In[6]:


n=int(input("Enter year"))
if((n%4==0)and(n%100!=0)or(n%400==0)):
    print("Leap Year")
else:
    print("not a Leap year")


# In[2]:


for n in range(0,50):
    for i in range(2,n):
        if(n%i==0):
            print(i)
    else:
        break
        
            
        
        


# In[4]:


n=int(input("Enter range"))
n1=0
n2=1
print(n1)
print(n2)
for i in range(0,n):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3


# In[7]:


n=int(input("Enter a number"))
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if sum==temp:
    print("Armstrong")
else:
    print("Not armstrong")
        


# In[10]:


n=int(input("Enter range"))
sum=0
for i in range(0,n):
    sum=sum+i
print("Sum is",sum)


# In[15]:


for i in range(1,6):
    print("*"*i)
    i+=1


# In[2]:


s=input("Enter a string")
n=int(input("Enter index"))
s1=s[:n]
print(s1)


# In[7]:


l=[10,14,15,23,75,60]
for i in l:
    if i%5==0:
        pass
    else:
        l.remove(i)
print(l)


# In[10]:


str='hiallhiwelcomehi'
str.count('hi')


# In[20]:


for i in range(1,6):
    for j in range(i):
        print(i,end='')
    print('')


# In[5]:


n=int(input("Enter a number"))
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==temp:
    print("Palindrome")
else:
    print("Not a Palindrome")


# In[4]:


list=[1,2,3,4,5]
print(list)
list[0],list[-1]=list[-1],list[0]
print("After interchanging first and last element")
print(list)


# In[5]:


list=[1,2,3,4,5]
print(list)
list[1],list[-2]=list[-2],list[1]
print("After interchanging first and last element")
print(list)


# In[6]:


list=[1,2,3,4,5]
l=len(list)
print(l)


# In[10]:


list=[1,2,3,4,5]
print("Maximum element",max(list))


# In[9]:


list=[1,2,3,4,5]
print("Minimum element=",min(list))


# In[6]:


str=input("Enter a string")
rev=str[::-1]
if rev==str:
    print("Palindrome string")
else:
    print("Not Palindrome string")


# In[27]:


str="Hello"
print(str)
s=str[::-1]
print("Reverse of string-",s)


# In[32]:


str="Welcome"
str1=str.replace('l','')
print(str1)


# In[26]:


str="Hello"
l=len(str)
print("Length of string",l)


# In[3]:


n="This is a python language"
s=n.split(" ")
for i in s:
    if len(i)%2==0:
        print(i)
        


# In[2]:


tup=(2,3,6,'hi')
print(len(tup))


# In[8]:


tup=(2,4,1,6,3)
print("Maximum element",max(tup))
print("Minimum element",min(tup))


# In[4]:


tup=(2,4,1,6,3)
print(sum(tup))


# In[1]:


list = [[('This', 4), ('is', 3)], [('Python', 2)], [('Language', 6), ('popular', 1)]]
print("The original list is : " + str(list))
l1= [2,3,4]
l2= [[(idx, val) for idx in key] for key,  val in zip(list,l1)]
print("The matrix after row elements addition : " + str(l2)) 

