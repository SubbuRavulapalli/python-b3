# 1) find the given num is even or odd
#
# n=int(input("given number is:"))
# if n%2==0:
#     print("the num is even")
# else:
#     print("the num is odd")
# output:given number is:333
#        the num is odd
#
#
# 2) print the numbers in reverse order
#
# n = 1234
# r = 0
#
# while n != 0:
#     d = n % 10
#     r= r * 10 + d
#     n //= 10
#
# print("r: " + str(r))
#
#
#
#
# 3) #find the sum of (1,10) numbers using range and loops
# 4) find the factorial of given number
#
# n=int(input("enter the num:"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print("factorial of %d is %d" %(n,f))
#
#
#
#
# 5) find the factors of given number
#
# n = int(input("Enter a number :"))
# print("The factors of are:")
#
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
# output:
# Enter a number :239
# The factors of are:
# 1
# 239
#
#
#
#
# 6) x=[10,1,2,3,100]-> swap the frst and last ele in x o/p :[100,1,2,3,10](loops not required)
#
# x=[10,1,2,3,100]
# # for i in x:
# x[0]=x[4]
# x[4]=10
#
# print(x)
#
#
#
# 7) x=[1,2,10,3,20,4] -> find the sum of even numbers and odd numbers
#
# x=[1,2,3,4,5,6,7,8,9]
# y=(x[1::2])
# print(y)#even
# print(sum(y))
# z=(x[0::2])
# print(z)
# print(sum(z))
# output:
# [2, 4, 6, 8]
# 20
# [1, 3, 5, 7, 9]
# 25
#
#


# assignment8
#
#
# 1.
# pattern
# program
# x = int(input("enter a val:"))
# for i in range(1, x + 1):
#     print("*" * (x + 1))
# output:
# ** ** *
# ** ** *
# ** ** *
# ** ** *
#
# 2.
# pattern
# program
# n = int(input("enter the val:"))
# for i in range(1, n + 1):
#     print('*' * i)
# output:
# *
# **
# ** *
# ** **
#
# 3.
# Print
# 1
# to
# 10
# multiplication
# tables
# n = int(input("enter a val:"))
# for i in range(1, 11):
#     print(n, "x", i, '=', n * i)
# output:
# 5
# x
# 1 = 5
# 5
# x
# 2 = 10
# 5
# x
# 3 = 15
# 5
# x
# 4 = 20
# 5
# x
# 5 = 25
# 5
# x
# 6 = 30
# 5
# x
# 7 = 35
# 5
# x
# 8 = 40
# 5
# x
# 9 = 45
# 5
# x
# 10 = 50
#
# 4.
# Wap
# to
# get
# unique
# numbers
# from list without
#
# using
# set
# X = [1, 2, 3, 2, 3, 4, 5]
#
# n = [1, 2, 3, 2, 3, 4, 5]
# print("the list is :" + str(n))
# result = []
# for i in n:
#     if i not in result:
#         result.append(i)
#         print("the list after remove duplicates:" + str(result))
# output: the
# list is: [1, 2, 3, 2, 3, 4, 5]
# the
# list
# after
# remove
# duplicates: [1]
# the
# list
# after
# remove
# duplicates: [1, 2]
# the
# list
# after
# remove
# duplicates: [1, 2, 3]
# the
# list
# after
# remove
# duplicates: [1, 2, 3, 4]
# the
# list
# after
# remove
# duplicates: [1, 2, 3, 4, 5]
#
# 5.
# X = ['helo', 'world', 'good']
#
# x = "hello world good"
# print(x.capitalize())
# x1 = 'helo'
# x2 = 'world'
# x3 = 'good'
# print(x1.capitalize() + x2.capitalize() + x3.capitalize())
# output:
# Hello
# world
# good
# HeloWorldGood
#
# 6.
# Wap
# to
# get
# all
# palindrom
# numbers
# from list
#
# Ex:
# n = int(input("enter the val:"))  # [121,77,443,111,223,675]
# temp = n
# r = 0
# while (n > 0):
#     d = n % 10
#     r = r % 10 + d
#     n = n // 10
#     if (temp == r):
#         print("the %d is palindrom".format(temp))
#     else:
#         print("not a palimdrom")
#
# break


