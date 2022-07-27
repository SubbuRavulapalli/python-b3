# n=int(input("Enter number of rows: "))
# a=[]
# for i in range(n):
#     a.append([])
#     a[i].append(1)
#     for j in range(1,i):
#         a[i].append(a[i-1][j-1]+a[i-1][j])
#     if(n!=0):
#         a[i].append(1)
# for i in range(n):
#     print("   "*(n-i),end=" ",sep=" ")
#     for j in range(0,i+1):
#         print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
#     print()
#
# x=range(1,100)
# for i in x:
#     if i%2==1:
#         print(i,end=' ')
#
# lower=int(input("Enter the lower limit for the range:"))
# upper=int(input("Enter the upper limit for the range:"))
# for i in range(lower,upper+1):
#     if(i%2!=0):
#         print(i)

# x=[10,1,2,3,100]
# # for i in x:
# x[0]=x[4]
# x[4]=10
#
# print(x)

# n=int(input("enter the num:"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print("factorial of %d is %d" %(n,f))
#     x=list(range(1,11))
# for i in x:
#     print(i,end=" ")

# n = 1234
# r= 0
# while n!= 0:
#     temp= n%10
#     r= r*10 + temp
#     n//= 10
# print("Reversed Number: " + str(r,temp))
# n=int(input("enter a val:"))
# s=0
# temp=n
# while(n>0):
#     r=n%10
#     a=r*10+r
#     n=n//10
#     print("reverse num of %d id: %d"  %(temp,s))

# find the sum of (1,10) numbers using range and loops
# x=[1,2,3,4,5,6,7,8,9,10]
# sum=list
# print(sum)
# for i in x:
#     sum=i+1
# Python program to
# compute sum of digits in
# number.

# Function to get sum of digits
# def getSum(n):
#     sum = 0
#     for digit in str(n):
#         sum += int(digit)
#     return sum
#
#
# n = range(1,10)
# print(getSum(n))



# print(x[::-1])
# x=10,20
# x.extend(2,3,4)
# print(x)

# i=1
# while True:
#     if i%3==0:
#         break
#     print(i)
#     i+=1
# x='abcd'
# for i in x:
#     print(i.upper())
# A = [[1, 2, 3],     [4, 5, 6],     [7, 8, 9]]
# x=(A[2][2])
# print(x)
# i=0
# while i<5:
#     print(i)
#     i+=1
#     if i==3:
#         break
# else:
#     print(0)
# def additem(listparam):
#     listparam +=[1]
# mylist=[1,2,3,4]
# additem(mylist)
# print(len(mylist))
# for i in range(10):
#     if i==5:
#         break
#     else:
#         print(i)
# else:
#     print('Here')
# str='subbu is'
# x=str.split()
# print(x)
# print("abcdef".find("cd") == "cd" in "abcdef")
# num={}
# letter={}
# comb={}
# num[1]=3
# letter[3]='f'
# comb['num']=num
# comb['letter']=letter
# print(comb)
# total={}
# def insert(item):
#     if item in total:
#         tota[item]+=1
#     else:
#         total[item]=1
# insert('apple')
# insert('orange')
# print(len(total))
# my_string="hello world"
# k= [(i.upper(),len(i)) for i in my_string]
# print(k)
# def unpack(a,b,c,d):
#
#     print(a+d)
# x=[1,2,3,4]
# unpack(*x)
# x=[1,2,3,4]
# print(x[:-2])
#print('Hello{name1}and{name2}'.format('subbu','ven'))
# x=[1,1,1,2,3,5,5]
# y=set(x)
# def test(lst):
#     if lst in y:
#         return 1
#     else:
#        return 0
# for i in filter(test,y):
#     print(i,end=' ')

# l= [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print('initial list-',str(l))
# r=list()
# for j in range(0,len(l[0])):
#     temp=0
#     for i in range(0,len(l)):
#         temp=temp+l[i][j]
#     r.append(temp)
# print('final list-',str(r))


# n=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# index=0
# max_index=0
# sum_max=0
# for list in n:
#     sum_list=0
#     for x in list:
#         sum_list+=x
#     if sum_list > sum_max:
#         sum_max=sum_list
#         max_index=index
#     index+=1
# print(n[max_index])


# from collections import defaultdict, Counter
# str1 = 'w3resource'
# my_dict = {}
# for letter in str1:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

# s='w3resource'
# d={}
# for i in s:
#     d[i] =d.get(i, 0) + 1
# print(d)

