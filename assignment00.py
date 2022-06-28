#Input : str = “my name is laxmi”
#output : str= laxmi is name my

# x =["my",'name','is','laxmi']
# y=x.reverse()
# print(y)
# for i in range(len(x)):
#     temp=x[i]
#     temp=temp[::-1]
#     temp=list(temp)
#     # print(temp)
#     temp.reverse()
#     temp="".join(temp)
#     x[i]=temp
# print(x)

#2)Find Highest Frequency Character in a String
 #  ex:  x='Helloworld' #o/p l=3
# x='Helloworld'
# # print(x)
# f={}
# for i in x:
#     if i in f:
#         f[i]=f[i]+1
#     else:
#         f[i]=1
# result=max(f,key=f.get)
# print('highest frequency char is:',result)

#3)Print the Words Ending with Letter 'A'
#    ex :x=Hello Rama NagA is Good RA   # o/p : NagA RA
# x='Hello Rama NagA is Good RA'
#x=['Hello', 'Rama','NagA' 'is' 'Good' 'RA']
# y=len(x)
# print(y)
# x='Hello Rama NagA is Good RA'
# y=x.endswith('A')
# print(y)

# x='1234' # o/p int -> 1234
# x=int(x)
# # x=type(x,)
# print(type(x),x)
#
#
# 'Amma', 'is', 'MadaM'
# fetch palindrom string # o/p : 'Amma','MadaM'
# x='amMa'
# x=x.casefold()
# y=reversed(x)
# if list(x)==list(y):
#     print('palindrom')
# else:
#     print('not')


#"Hello Kasi Your SalaRy is $10000" fetch count all small letters and caps and digits,specia chars
# x="Hello Kasi Your SalaRy is $10000"
# lower=upper=num=spl=0
# for i in range(len(x)):
#     if x[i]==x.islower():
#         lower=lower+1
#     elif x[i]==x.isupper():
#         upper=upper+1
#     elif x[i]==x.isdigit():
#         num=num+1
#     elif x[i]==x.isidentifier():
#     else:
#         return o
# print('lower,upper,num,spl:' ,x)

# x="Hello Kasi Your SalaRy is $10000"
# lower=upper=num=spl=0
# for i in range(len(x)):
#     if(x[i].islower()):
#         lower=lower+1
#     elif(x[i].isupper()):
#         upper=upper+1
#     elif(x[i].isnumeric()):
#         num=num+1
#     else:
#         spl=spl+1
# print('no.of lower is:',lower)
# print('no.of upper is:',upper)
# print('no.of num is :',num)
# print('no.of spl is:',spl)



#find the sum of ascii value of given string
      #ex :'AB' 65+66 =131
# x = 'A'
# a='B'
# y = ascii(x), ord(x)
# z=ascii(a),ord(a)
# print(y*z)

#find the substr how many times it exits
     #ex : 'AAABBBCAA'  op : A->5
#x='AAABBBCAA'
# y=x.count('A')
# print('A is:',y)

#x='Hello World'  o/p: 'hellO worlD' -> make frst letter caps and last letter small in each word of string
# x='Hello World'
# y=x.swapcase()

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
