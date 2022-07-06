import re
import sys
num1= input("enter first number:")
if not re.match("^[0-9]*$", num1):
         print ("INVALID CHARACTERS!") 
         sys.exit()

num2= input("Enter second Num: ")
if not re.match("^[0-9]*$", num2):
         print ("INVALID CHARACTERS!") 
         sys.exit()
Result = float(num1) + float(num2)
print(Result)


