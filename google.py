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
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = range(1,10)
print(getSum(n))

