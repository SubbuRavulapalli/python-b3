# ass1 remove the duplicate ele in the list without using set and by using set

#x=[1,2,3,4,1,2,5,6]  # output [1,2,3,4,5,6]
# x=[1,2,3,4,1,2,5,6]
# y=set(x)
# print(y)


# ass2 -> count the each ele how many times it is exits ->
# x=[1,1,2,3,4,5,3,2]
# y=x.count(1)
# print(y)
#



#x=[1,2,3,4,1,2,5,6]

# output [1,2,2,2,3,1,4,1,5,1,6,1]

#  Ass 3 : sort the list without sort function  # use any sorting logic

# x=[2,3,4,1,9,6]
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x)
#






#x=[10,2,4,3,5] -> [2,3,4,5,10]
# x=[10,2,4,3,5]
# print(x.sort(x))


# print only even numbers using list comphreension
# x=[1,3,2,4,5,7,6,8] # output -> [2,4,6,8]  ->
# y=[i for i in x if i%2==0]#even
# z=[i for i in x if i%2!=0]#odd
# print(y)
# print(z)

# wap to print even and its position in another list
# x=[1,3,2,4,5,7,6,8]
# z=[2,2,4,3,6,6,8,7]

# x = [1, 3, 2, 4, 5, 7, 6, 8]
# y=[i for i in x if i%2==0]
#
# print(y)