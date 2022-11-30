#imports
import csv
import login
from csv import writer
import numpy as np
import random

#variables
UserScore = 0
SelectedQ = ""
done = "f"
passvariable = ""
TotalQs = 0
QuizChosen = "f"
QuestionCompletedCount = 0
QuestionNum = 1
NoOfQs = 0
RandomQNum = 0
StorTotalQ = 0

#function - maybe unnecessary
def passvar(variable):
  global passvariable
  passvariable = variable

def TotalQR(TotalQ):
  global TotalQs
  TotalQs = int(TotalQ)
  QuizQsConv = int(TotalQ/10)
  global NoOfQs
  NoOfQs = int(random.randint(10,QuizQsConv))


  
#main
with open("CSVCHECK.txt", 'r') as read_obj:
  # read first character
  one_char = read_obj.read(1)
  # if not fetched then file is empty
  if not one_char:
    with open("quizquestions.csv","w",newline="") as csvfile:
      fieldnames = ["QuestionNum","Question","Answer1","Answer2","Answer3","Answer4","Correctanswer","QuizID","FinalQ"]
      Loginwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
      Loginwrite.writeheader()
    with open("playerscores.csv","w",newline="") as csvfile:
      fieldnames = ["Username","TotalCorrect","TotalQ","Percentage","QuizID"]
      Loginwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
      Loginwrite.writeheader()



while QuizChosen == "f":
  QuizSelection = input("Choose a quiz or enter LIST to view a full list of available quizzes: ")
  if QuizSelection == "LIST" or QuizSelection == "List" or QuizSelection == "list":
    csv_file = csv.reader(open('allquizzes.csv', "r"), delimiter=",")
    print("\n")
    for row in csv_file:
        if row[0] != "Title":
          print(row[0],"","Q"+row[1],"",row[2])
  else:
    csv_file = csv.reader(open('allquizzes.csv', "r"), delimiter=",")
    print("\n")
    for row in csv_file:
      if row[0] == QuizSelection.capitalize() or row[3] == QuizSelection.upper():
        SelectedQ = row[3]
        passvar(SelectedQ)
        TotalQR(int(row[1]))

        csv_file = csv.reader(open("playerscoressorted.csv","r"),delimiter=",")
        QuizChosen = "t"
        for row in csv_file:
          if row[4] == passvariable and row[0] == login.loggedUser:
            percent = (int(row[1])/int(row[2])*100)
            percentround = str(np.round(percent,1))
            print("Your highest score is",str(row[1]),"out of",str(row[2]),"which is",str(percentround)+"%")
            print("\n")
            QuizChosen = "t"  
            break 
        else:
          break
  

for i in range(NoOfQs):
  quiz = csv.reader(open("quizquestions.csv","r"),delimiter=",")
  next(quiz)
  chosenrow = random.choice(list(quiz))
  print("Q"+str(QuestionNum)+":",chosenrow[1].capitalize())
  print("A."+chosenrow[2].capitalize())
  print("B."+chosenrow[3].capitalize())
  print("C."+chosenrow[4].capitalize())
  print("D."+chosenrow[5].capitalize())

  UserAnswer = input("Enter the letter of the correct answer: ")


  if QuestionCompletedCount == NoOfQs-1:
    print("Your total score is",str(UserScore)+"/"+str(NoOfQs))
    TotalCorrect = str(UserScore)
    TotalQs = str(NoOfQs)
    QuizID = chosenrow[7]
    Username = login.loggedUser
    percent = (int(UserScore)/int(NoOfQs)*100)
    Percentroundstore = str(np.round(percent,1))
    row_contents = [Username,TotalCorrect,TotalQs,Percentroundstore,QuizID]
    with open("playerscores.csv", 'a', newline='') as write_obj:
      csv_writer = writer(write_obj)
      csv_writer.writerow(row_contents)
            
  elif chosenrow[6] == UserAnswer.lower():
    print("Correct")
    print("\n")
    UserScore = UserScore + 1 
    QuestionCompletedCount = QuestionCompletedCount + 1
    QuestionNum = QuestionNum + 1


  elif chosenrow[6] != UserAnswer.lower():
    print("Incorrect")
    print("The correct answer was",chosenrow[6].upper())
    print("\n")
    QuestionCompletedCount = QuestionCompletedCount + 1
    QuestionNum = QuestionNum + 1

      

      
        


with open('playerscores.csv', newline='') as csvfile:
    rdr = csv.reader(csvfile)
    l = sorted(rdr, key=lambda x: x[3], reverse=True)


with open('playerscoressorted.csv', 'w') as csvout:
    wrtr = csv.writer(csvout)
    wrtr.writerows(l)