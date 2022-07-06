
import sys
import re


Best_Player= str ("messi")
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

while guess != Best_Player and not(out_of_guesses):
    if guess_count< guess_limit:
        guess=input("Who is the best player?:")
        if not re.match("^[a-z]*$", guess):
         print ("Error! Only letters a-z allowed!") 
        guess_count+=1     
    else:
        out_of_guesses=True

if out_of_guesses:
     print("oops! You loose")       
     
else: 
 print("Well Done")