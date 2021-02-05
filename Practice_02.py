#!/usr/bin/env python
# coding: utf-8

# # Factorial!
# ### You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.
# ### Input Format: The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.
# ### Output Format: Output a single line denoting the factorial of the number N.

# In[10]:


n =int(input())
def factorial(n):
    return 1 if n == 0 else n*factorial(n-1)
print(factorial(n))


# # Marksheet :

# In[16]:


marks = float(input("Enter your marks:"))
print('A' if marks>=80 else 'B' if marks>=60 and marks <=80 else 'C'if marks>=40 and marks <=60 else 'D' )


# In[17]:


marks = float(input("Enter your marks:"))
if marks >=80 and marks <=100:
    grade ='A'
else:
    if marks >=60 and marks <=79:
         grade ='B'
    else:
        if marks >=40 and marks <=59:
            grade ='C'
        else:
            grade = 'D'
print(f'Grade = {grade}')


# In[25]:


marks = float(input("Enter your marks:"))
if marks >=80 and marks <=100:
    grade ='A'
elif marks >=60 and marks <=79:
    grade ='B'
elif marks >=40 and marks <=59:
    grade ='C'
else:
    grade = 'D'
print(f'Grade = {grade}')


# In[59]:


marks = float(input("Enter your marks:"))
if marks in range(80, 100):
     grade ='A'
elif marks in range(60, 79):
    grade ='B'
elif marks in range(40, 59):
    grade = 'c'
else:
    grade = 'D'    
print(f'Grade = {grade}')


# # SET :
# ### A set is an unordered collection data type with no duplicate elements. Sets are iterable and mutable. The elements appear in an arbitrary order when sets are iterated.
# ### Sets are commonly used for membership testing, removing duplicates entries, and also for operations such as intersection, union, and set difference.

# In[27]:


setA = set([9,8,7,6,5,4,3,2,1])
print(setA)


# In[37]:


setB = set([5,7,9,1,6,2,8,7,3,5,4,5,2])
print(setB)


# In[52]:


setN = set ([3,1,5,9])
print(setN)


# In[53]:


setN.add(8) # Python set add(element)


# In[54]:


print(setN)


# In[55]:


setN.remove(5) # Using remove(element) Used to remove element from the set
print(setN)


# In[56]:


setN = set ([3,1,5,9])
print(setN)
setN.add(8) # Python set add(element)
print(setN)
setN.remove(5) # Using remove(element) Used to remove element from the set
print(setN)


# #  Python: Division
# 
# 

# In[61]:


from __future__ import division
a = int(input())
b = int(input())

intdiv = a//b
floatdiv = a/b

print("{0}\n{1}".format(intdiv,floatdiv))


# # Python Recursion:
# ### Recursion is a method of breaking a problem into subproblems which are essentially of the same type as the original problem. You solve the base problems and then combine the results. Usually this involves the function calling itself.

# # Fibbonacci Series
# ### fibo(n) = 0 if n == 1
# ### fibo(n) = 1 if n== 2
# ### fibo(n-2) + fibo(n-1) Otherwise

# In[62]:


n =int(input("Enter Value:"))
def fibo(n):
    return 0 if n ==1 else 1 if n == 2 else fibo(n-2) + fibo(n-1) 
print(fibo(n))


# # LOOPS
# ### For and While
# ### Counter Control Loop and sentinel Control Loop
# ### CCL - Iterative and SCL - Number does not define here
# # Factorial! 

# In[65]:


n = int(input("Enter Value:"))
f = 1
i = 2
while i <= n : # Using 'While' in here
    f *= i
    i += 1
print(f'Factorial:{f}')


# In[75]:


c=0
while True:
    print(c)
    c += 1
    if c >= 10:
        break


# In[80]:


count = 0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))


# In[73]:


for i in range(10):
    print(i)


# In[68]:


for i in range(1,10):
    print(i)


# In[69]:


for i in range(3,8,2):
    print(i)


# In[76]:


for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


# In[79]:


for x in range(10):
    # Check if x is odd
    if x % 2 == 1:
        continue
    print(x)


# In[ ]:




