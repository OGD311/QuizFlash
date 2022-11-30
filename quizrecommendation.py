#imports
import csv
from random import *

#lists
TitleL = ["Driving Theory","French Language Food","Latin Language"]
QcL = [30,25,450]
DescL = ["Questions for the theory section of your driving exam","French language revision -> Topic: Food","Contains all words needed for GCSE Latin"]
QuizIDL = ["DT","FLF","LLC"]
listlength = len(QuizIDL) - 1
#main code
#erases csv file -> updates if any changes
with open("quizrecommendations.csv","w",newline="") as csvfile:
      fieldnames = ["Title","Qc","Desc","QuizID"]
      Loginwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
      Loginwrite.writeheader()

#adds current quizdata
for i in range(0,3):
  P = randint(0,listlength)
  Title = TitleL[P].capitalize()
  Qc = QcL[P]
  Desc = DescL[P].capitalize()
  QuizID = QuizIDL[P]
  del TitleL[P]
  del QcL[P]
  del DescL[P]
  del QuizIDL[P]
  with open("quizrecommendations.csv","a",newline="") as csvfile:
    fieldnames = ["Title", "Qc","Desc","QuizID"]
    currentquizwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
    currentquizwrite.writerow({"Title":Title, "Qc":Qc, "Desc":Desc, "QuizID":QuizID})
  listlength = listlength - 1

#prints current quiz data
csv_file = csv.reader(open('quizrecommendations.csv', "r"), delimiter=",")
print("\n")
print("Recommended quizzes: ")
for row in csv_file:
  if row[0] != "Title":
    print(row[0],"","Q"+row[1],"",row[2])
print("\n")
