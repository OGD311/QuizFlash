#imports
import os

#welcome message
print("Welcome to Quizflash Revision app")
print("Please login or signup to access our wide range of quizzes")



#variables
#main log in screen
os.system("python3 allquizzeslistupdater.py")

#import login.py + run
import login

if login.logachieved == "Y":
  os.system("python3 quizrecommendation.py")
  import quizquestionsstore



