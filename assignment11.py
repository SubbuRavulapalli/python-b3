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

#4.
# x='1234' # o/p int -> 1234
# x=int(x)
# # x=type(x,)
# print(type(x),x)
#
#
#'Amma', 'is', 'MadaM'
#fetch palindrom string # o/p : 'Amma','MadaM'
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
# s=
#
# print(s)

#find the substr how many times it exits
     #ex : 'AAABBBCAA'  op : A->5
#x='AAABBBCAA'
# y=x.count('A')
# print('A is:',y)

#x='Hello World'  o/p: 'hellO worlD' -> make frst letter caps and last letter small in each word of string
# x='Hello World'
# y=x.swapcase()
