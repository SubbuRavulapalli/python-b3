
#1.
# 2 3
# 4 5 6
# 7 8 9 10
# count=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(count,end=' ')
#         count=count+1
#     print()

#2.
# str="nagaraj"
# for i in range(0,7):
#     for j in range(0,i+1):
#         print(str[j],end=' ')
#     print()
#


# for i in range(65,79):
#     for j in range(65,i+1):
#           print(chr(i),end=' ')
#     print()

#searching char in string
# for i in range(1,4):
#     x=input("enter the string:")
#     y=input('enter the char:')
#     if y in x:
#         print(" is present")
#     else:
#         print(' is not present')


# x='subbu'
# y='venkat'
# # if x==y
# print("%s and%s arw good frnds"  %(x,y))


#palindrom program
# n=[11,43,67,99,22,223]
# y=[]
# for i in n:
#     temp=i
#     s=0
#     while i>0:
#         r=i%10
#         s=s*10+r
#         i=i//10
#         if s==temp:
#             y.append(s)
# print(y)
# print(max(y))

#fibanaccii seriess
# n=int(input('enter a val:'))
# a=0
# b=1
# for i in range(1,n+1):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=' ')


#palimdrom
# for i in range(0,7):
#      n=int(input("enter the val:"))    #[121,77,443,111,223,675]
#      temp=n
#      r=0             #[11,43,67,99,22,223
#     while(n>0):
#
#          d=n%10
#          r=r%10+d
#          n=n//10
#          if (temp==r):
#             print("the %d is palindrom".format(temp))
#          else:
#              print("not a palimdrom")


#comparing two strings
# for i in range(1,3):
#     x=input('enter a string:')
#     y=input('enter a string:')
#     if len(x)==len(y):
#         if x==y:
#             print('both are equl')
#         else:
#             print('not equl')
#     else:
#          print('not equl')
# count=1
# for i in range(1,15):
#     for j in range(1,i+1):
#         print(count,end=" ")
#         count = count +j
#     print()
# x='subbu'
# print(x.upper())
# print(x)
# for i in range(3):
#     n=int(input("enter ele:"))
#     a=0
#     b=1
#     print(a,b, end=' ')
#     for i in range(1,n+1):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=' ')
#     print()

# n = int(input("enter ele:"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c=c+1
#    if c==2:
#       print('%d is prime num:')
#    else:
#       print('%d is not prime')
# for i in range(1,6):
#     n=int(input('enter ele:'))
#     c=0
#     for i in range(1,n+1):
#       if n%i==0:
#          c=c+1
#          print(i,end=' ')
#     print()
# if(c==2):
#      print('%d is prime:')
# else:
#     print('%d is not prime')
# print(x.count(x))
# x='python IS good'
# y=x.split('o')
# print(x.replace('o','ss',5))

# x='subbu'
# a,b,c,d,e=list(x)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# x='$$'.join(a+b+c+d+e)
# print(x)
# y=x.join(a+b+c+d+e)
# print(y)
# x=list(x)
# print(x)


# x=[11,43,67,99,22,223]
#
# y=[]
# for i in x:
#     temp=i
#     s=0
#     while(i>0):
#         r=i%10
#         s=s*10+r
#         i=i//10
#     if s==temp:
#         y.append(s)
# print(y)
# print(max(y))


# x='venkat ravulapalli'
# print('v' in x)

###replace
# x='asdfasdfddddddddddddddd'
# x=x.replace('d','@@##$').replace('a','x').replace('a','subbu')
# print(x)
# x='subbu'
# print(x.center(10,'@'))
# x.

#x=(10,2,3,5)-> each ele multifly by 10   (100,20,30,50)
# x=(10,2,3,5)
# y=list(x)
# for i in y:
#     i*10
# print(x)
#


# ass2 :
# x=[1,2,3,4] -> [3,5,7]
#reverse of a number...
# n = 1234
# r = 0
#
# while n != 0:
#     d = n % 10
#     r= r * 10 + d
#     n //= 10
#
# print("r: " + str(r))

#factors of a number
# n = int(input("Enter a number :"))
# print("The factors of are:")
#
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i,end=" ")

# n=int(input('enter the num to sum:'))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+sum
#     print('sum of num',n,'num is:',sum)
