#1) wa function to check wheather num is prime or not
def prime():
    x=int(input('enter a element:'))
    fact=0
    for i in range(2,x//2+1):
        if(x%i==0):
            fact =fact+ 1
    if(fact<=2):

        print('element is prime')
    else:
        print('element is not prime')


prime()





# 2) x={'A:100,'B':200}    # op {100:'A',200:'B'}
# x={'A':100,'B':200}
# y={}
# for i in x:
#     y.setdefault(x[i],i)
# print(y)
#
# print(x.keys(),x.values())

# 4) Write a function that two strings are anagram or nor
#    # Ex : string1 :"Naga"   string 2:"aNga"    both are anagrams
str1=input('enter string 1')
str2=input('enter string 2')
sum=0
sum1=0
if len(str1 )==len( str2):

    for i in str1:
        sum=sum+ord(i)
    for i in str2:
        sum1=sum1+ord(i)
    if sum==sum1:
        print('srings are anagram')
    else:
        print('strings not anagram')
else:
    print('srings not anagram')



