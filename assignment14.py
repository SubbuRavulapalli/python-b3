#1.wa function to check wheather num is prime or not
# def prime():
#    x=int(input('enter a val:'))
#    for i in range(1,x+1):
#        while x%i==0:
#            if i==2:
#                print('val is prime')
#            else:
#                print('val is not prime')
#            return()
# prime()
#
#

#2) types of all functions with example
##functions:it is a group of statements in a single unit.
#1.without args without return values
# def list():
#     print('list is mutable')
#     print('it allow duplicates also..')
# list()
#2.without args with return values
# def tuple():
#      print('tuple is immutable')
#      print('it allow duplicates')
# tuple()
#3.with args with return values
# def mul(a,b):
#     return a*b
# c=mul(20,25)
# print(c)
#4.with args without return values
# def sub(a,b):
#     print(a-b)
# sub(225,25)

#5.variable len args
#it will accept n no. of elements
#it will return tuple
# def mul(*a):
#     a=pow(2,5)
#     print(a)
#     return
# mul()

#6.keyword variable len:
# def python(**a):
#     return a
# x=python(a=2,b=23,c=6,d=5)
# print(x)

#lambda: it is anonymous fun
#stntax:var_name=lambda var__:business logic

# z=lambda a:a if a%2==0 else 0
# print(z(20),'is even')



#3) x={'A:100,'B':200}    # op {100:'A',200:'B'}
# def python():
#     x = {'A': 100, 'B': 200}
#     keys = list(x.keys())
#     # print(keys)
#     values = list(x.values())
#     # print(values)
#     print(x)
#     z = dict(zip(values, keys))
#     print(z)
# python()


# 4) x=[121,24,55,7,9] -> [121,55] (write function to fetch only palindrom nubers)
# def palindrom():
#     x = [121, 24, 55, 7, 9]
#     for i in range(0, len(x)):
#         temp = x[i]
#         r = 0
#         while (x[i] > 0):
#             d = x[i] % 10
#             r = r * 10 + d
#             x[i] = x[i] // 10
#             if temp == r:
#                 print(' is palindrom', temp)
# palindrom()
#


# 5) x=[1,2,3,5] -> add 10 to each element in list use lambda fun
# def add():
#     x=[1,2,3,5]
#     for i in x:
#        y=x[i]+10
#        break
#     print(y)
#
#
#
# add()



# 6) what is filter ,reduce map with syntax aand example
#filter: * filter will take 2 args ,one is function,and list
#        * it will filter the particular elements
#syntax: var_name=list(filter(fun ,iterable obj))

# x=[1,2,3,4,5,6,7]
# a=list(filter(lambda i:i%2==0 ,x) )
# print(a)
#
#map: * map will apply on each nd every element on the list
#     * it will midify all the element nd generate new element

x=list(range(1,5))
# def square(x):
#     return x*10
z=list(map(lambda i:i%2==0,x))
print(z)

#reduce: reduce fun. reduce the sequence of ele into a single ele by applingnspecified fun.


# from functools import reduce
# x=list(range(1,11))
# print(x)

# 7) wa function x=[[1,2,3],[4,5,6],[1,2,3]] remove duplicate list from list
# def duplicate():
#     x = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
#     y=set(x)
#     print(y)
#
#
# def duplicate(**x):
#     return x
# n=duplicate( [[1, 2, 3], [4, 5, 6], [1, 2, 3]])
# print(x)



