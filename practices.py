'''doc_strings_functions-inside the function if we keep 3 times single code pr double code is called doc strings'''
# def niha():
#     '''hii
# hello
# good morning'''
# print(niha.__doc__)

'''Default argument-the function having default values,if we want to change we can change the values'''
# def a(hello='python',date=5):
#     print('hello:',hello)
#     print('date:',date)
# a()
# a('advance python')
# a(date=6)

'''addition of two numbers using function'''
# def n(a,b):
#     c=a+b
#     d=a+b
#     print('sum is',c)  
#     print('sum is',d)
# n(6,6)  # first it will be added to both variables
# n(2.5,4.6)  #  later it will be added to both variables

'''add return'''
# def sum(a,b):
#     c=a+b
#     return c
# x=sum(10,20)
# print('sum is',x)  # sum is 30
# y=sum(10.5,2.3)
# print('sum is :',y)  #  sum is : 12.8

'''even odd using function'''
# def a(num):
#     if num%2==0:
#         print(num,'is even')
#     else:
#         print(num,'is odd')
# x=int(input())
# a(x)  # 5 is odd
# a(6)  # 6 is even
# a(8)  # 8 is even
# a(9)  # 9 is odd
# a(7)  # 7 is odd
    
'''filter()-function that returns even numbers from a list'''
# def a(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# b=[int(x) for x in input().split()]
# c=list(filter(a,b))
# print('from the b the a values are:',c)

'''filter()-function that returns odd numbers from a list'''
# def a(n):
#      if n%2!=0:
#         return True
#      else:
#         return False
# b=[int(x) for x in input().split()]
# c=list(filter(a,b))
# print('from the b the a values are:',c)

'''lambda-function to calculate sum of two numbers'''
# a=lambda x,y,z: x+y+z
# b=lambda x,y,z: x*y*z
# c=a(1,2,3)
# d=b(4,5,6)
# print(c)  #  6
# print(d)  #  120

'''lambda function that returns bigger number'''
# x=lambda a,b: a if a>b else b
# a,b=[int(z) for z in input().split()]
# print(x(a,b))

# y=[int(z) for z in input().split()]
# print('bigger number is:',max(y))
# print('smaller number is:',min(y))

'''lambda filter-lambda function that returns even numbers from a list'''
# a=[int(x) for x in input().split()]
# b=list(filter(lambda x:(x%2==0),a))
# c=list(filter(lambda x:(x%2!=0),a))
# print(b)
# print(c)

'''lambda map-lambda that returns squares'''
# a=[1,2,3,4,5,6]
# b=list(map(lambda x:x**2,a))
# c=list(map(lambda x:x+2,a))
# d=list(map(lambda x:x-2,a))
# print(b)  # [1, 4, 9, 16, 25, 36]
# print(c)  # [3, 4, 5, 6, 7, 8]
# print(d)  # [-1, 0, 1, 2, 3, 4]

'''lambda reduce'''
# from functools import*
# x=[2,4,6,8]
# y=reduce(lambda a,b:a ,x)
# z=reduce(lambda a,b:b ,x)
# m=reduce(lambda a,b:a+b ,x)
# n=reduce(lambda a,b:a-b ,x)
# print(y)  # 2
# print(z)  # 8
# print(m)  # 20
# print(n)  # -16


# a='babu '
# b=len(a)
# while (b>0):
#     print(a[b-1],end='')
#     b-=1

# a='babu'
# print(a[::-1])

# import math as m
# print(m.factorial(5))

# a=5
# b=1
# for i in range(1,a+1): 
    # b=b*i 
# print(b)

# from functools import*

# a=[]
# for i in range(1,6):
    # a.append(i)
    # print(a)
# a=[2,3,4,5]
    # f=reduce(lambda x,y:x*y,a)
# print(f)

