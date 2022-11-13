# #1.
# while True:          #using while loop
#     try:                       #implementing try and except block
#         person_age = int(input("Please enter persons's age :"))
#         break
#     except ValueError:
#         print("\nThis is not a number. Try again...")
#         print()
#
#
# if person_age < 1 or person_age > 120:            #if condition
#     print("please enter the valid  age  of person ")  #printing the statement
#

#
# # #2.
# while True:                       #using while loop
#     try:
#
#         days = int(input("Enter number of days :"))  #implement Try and except block
#         break
#     except ValueError:
#         print("Please enter valid input ")
#
#
#
# total_salary = 0
# for i in range(days):
#
#     daysalary = 50
#     total_salary +=daysalary
#
#     print("day %d: $%.2f dollar"%(i+1,daysalary))          #printing the total amount of salary
#
# print("\nTotal amount :$%.2f dollor"%(total_salary))
#
#
#
#
#
# #
# #3.
# #Python program for reading
# #from file
#
# f = open('nums.txt', 'r')     #open the txt file
#
# # Reading from the file
# content = f.readlines()        #Read the txt file
#
# # Variable for storing the sum
# total_num = 0                    #taking variables
# low_num = 0
# high_num = 0
# avrg = 0
#
#
# # Iterating through the content
# # Of the file
# for line in content:
#
#     for i in line:
#
#         # Checking for the digit in
#         # the string
#         if i.isnumeric() == True:
#             total_num = total_num.append(i)
#
# total_num = list(total_num)
# print("The list of integers:", total_num)        #print the list if integers
# total_num.sort()                                 #sorting the above list into ascinding order
# print("The lowest number is :" ,total_num[0])    #printing the lowest num
# print("the highest number is :", total_num[-1])  #printing the highest num
#
# average = sum(total_num)/len(total_num)          #printing the avg
# print("the average of numbers is:",average)


