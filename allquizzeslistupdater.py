#imports
import csv

#variables
TitleL = ["Driving Theory","French Language Food","Latin Language"]
QcL = [30,25,450]
DescL = ["Questions for the theory section of your driving exam","French language revision -> Topic: Food","Contains all words needed for GCSE Latin"]
QuizIDL = ["DT","FLF","LLC"]
listlength = len(QuizIDL)
#main
with open("allquizzes.csv","w",newline="") as csvfile:
      fieldnames = ["Title","Qc","Desc","QuizID"]
      Loginwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
      Loginwrite.writeheader()

for P in range(0,listlength):
  Title = TitleL[P].capitalize()
  Qc = QcL[P]
  Desc = DescL[P].capitalize()
  QuizID = QuizIDL[P]
  with open("allquizzes.csv","a",newline="") as csvfile:
    fieldnames = ["Title", "Qc","Desc","QuizID"]
    currentquizwrite = csv.DictWriter(csvfile, fieldnames=fieldnames)
    currentquizwrite.writerow({"Title":Title, "Qc":Qc, "Desc":Desc, "QuizID":QuizID})
    listlength = listlength - 1

