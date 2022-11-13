#  #1.
# def main():        #create main function
# 	result=[]      #taking empty list
# 	for i in range(321,1065):           #using for loop
# 		if (i%6==0 and i%11==0 ):       #implement if condition
# 			result.append(i)            # using append function to store numbers
# 	print(result)
# 	print("the numbers divisible by both 6 and 11 is :",len(result))   #using lenth function
# 	print(type(result))
# if __name__ == "__main__":
# 	main()

#
# #2.
# class main():              #using main class
# 	def __init__(self,teacher_name,credits,course_name):  #using init method to create attributes
# 		self.teacher_name = teacher_name         #attributess
# 		self.credits = int(credits)
# 		self.course_name = course_name
# 	def teacher(self,name):                               #using def main method to start class
# 		self.name = name
# 		print(name)
# 		def credits(self,credits):                        #using try exception block to verify that credits is an int..
# 			try:
# 				self.credits = int(credits)
# 				print(credits)
# 			except:
# 				print("oops..  Please emter correct input :")
#
# 		def course(self, course_name):
# 			self.course_name = course_name
# 			print(course_name)
# s1 = main("vijaya sri",90,"masters")                  #using instances/objects
# s2 = main("farhana",95,"masters")                     #adding data
# s3 = main("vennela",96,"engineering")
# print("name:",s1.teacher_name,  "course_name:",s1.course_name,  "credits:",s1.credits)    #printing data using methods defined in the class
# print("name:",s2.teacher_name,  "course_name:",s2.course_name,  "credits:",s2.credits)
# print("name:",s3.teacher_name,  "course_name:",s3.course_name,  "credits:",s3.credits)
#






# # 3.
# def main():                     #using main function
# 	digits = []                #taking empty lists
# 	non_digits = []
# 	string =input("please enter a string :")
# 	for i in string:           #using for loop
# 		if i.isdigit():        # # Extract digits from string
# 			digits.append(i)    #storing digits using append function
# 		if i.isalpha():        # # Extract non-digits from string
# 			non_digits.append(i)   #storing non-digits using append function
# 	print(list(digits))            #coverting into list
# 	print(type(digits))
# 	print("total numbers of digits present in string is :", len(digits))    #lenght of list
# 	print(tuple(non_digits))       #converting into tuple
# 	print(type(non_digits))
# 	print("total numbers of non-digits present in string is :", len(non_digits))
# main()


# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('bsc_resume.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()