#import
from random import *
import csv

#signupvariables
signupachieved = "N"
logachieved = "N"
loggedin = "f"
accountexist = "f"
loggeduser = "Error"
#needstohappenfirst
File = open("CSVCHECK.txt","a")
File.close()
with open("CSVCHECK.txt", 'r') as read_obj:
  # read first character
  one_char = read_obj.read(1)
  # if not fetched then file is empty
  if not one_char:
    csvcheck = 0
    with open("Logins.csv","a",newline="") as csvfile:
      fieldnames = ["Username","Encrypted","Key"]
      Loginwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
      Loginwrite.writeheader()
      File = open("CSVCHECK.txt","a")
      File.write("DONT NEED TO WRITE FIELDNAMES AGAIN")
      File.close()
  else:
    csvcheck = 1

  
#login/signup functions
def signup(username,password):
  csv_file = csv.reader(open('Logins.csv', "r"), delimiter=",")
  for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if username == row[0]:
      print("Sorry that username is already taken - please try again")
      return
  
  if username == " ":
    print("Username cannot be blank - please try again")
    return

  extra = len(username)
  key = randint(9,500)
  encrypted = ""
  for letter in password:
    number = ord(letter)
    newNum = number + key + extra

    newLetter = chr(newNum)
    encrypted = encrypted + newLetter
  with open("Logins.csv","a",newline="") as csvfile:
    fieldnames = ["Username", "Encrypted","Key"]
    Loginwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
    Loginwrite.writerow({"Username": username, "Encrypted": encrypted, "Key": key})
  global signupachieved
  signupachieved = "Y"
  

def login(username,password):
  csv_file = csv.reader(open('Logins.csv', "r"), delimiter=",")
  for row in csv_file:
  #if current rows 2nd value is equal to input, print that row
    if username == row[0]:
      decrypt(username,row[1],row[2],password)
      return
  else:
    print("Username not found - please signup")
    global accountexist
    accountexist = "f"


def decrypt(username,encryptedtext,decrkey,passguess):
  message = encryptedtext
  extra = len(username)
  key = int(decrkey)
  decrypted = ""
  for letter in message:
      number = ord(letter)
      newNum = number - key - extra
      newLetter = chr(newNum)
      decrypted = decrypted + newLetter
  if passguess == decrypted:
    print("Welcome",username.capitalize())
    global accountexist
    accountexist = "t"
    global loggedUser
    loggedUser = str(username)
  else:
    print("Password is wrong - please try again")
    
  
  
#signup/Login
signupdone = "f"

while loggedin == "f":

  LogOrSign = input("Login or Signup?: (L/S): ")
  if LogOrSign == "L" or LogOrSign == "login" or LogOrSign == "Login" or LogOrSign == "l":
    Username = input("Enter a username: ")
    Password = input("Enter a password: ")
    login(Username,Password)
    if accountexist == "t":
      loggedin = "t"
      logachieved = "Y"
      break

  elif LogOrSign == "S" or LogOrSign == "signup" or LogOrSign == "Signup" or LogOrSign == "s":
    Username = input("Enter a username: ")
    Password = input("Enter a password: ")
    signup(Username,Password)
    if signupachieved == "Y":
      login(Username,Password)
      loggedin = "t"
      logachieved = "Y"
    else:
      Username = input("Enter a username: ")
      Password = input("Enter a password: ")
      signup(Username,Password)

  else:
    print("\n")
    print("Please signup or login")


  
    


