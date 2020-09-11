# Author: John Shields jts5975@psu.edu
def getGradePoint(lg):
  if (lg == "A"):
    gp = 4.0
  elif (lg == "A-"):
    gp = 3.67
  elif (lg == "B+"):
   gp = 3.33
  elif (lg == "B"):
   gp = 3.0
  elif (lg == "B-"):
   gp = 2.67
  elif (lg == "C+"):
   gp = 2.33
  elif (lg == "C"):
   gp = 2.0
  elif (lg == "D"):
   gp = 1.0
  else:
   gp = 0.0
  return (gp)


def run():
 lg1 = input("Enter your course 1 letter grade: ")
 lg = lg1
 c1 = float(input("Enter your course 1 credit: "))
 print(f"Grade point for course 1 is: {getGradePoint(lg)}")
 gp1 = getGradePoint(lg)
 lg2 = input("Enter your course 2 letter grade: ")
 lg = lg2
 c2 = float(input("Enter your course 2 credit: "))
 print(f"Grade point for course 2 is: {getGradePoint(lg)}")
 gp2 = getGradePoint(lg)
 lg3 = input("Enter your course 3 letter grade: ")
 lg = lg3
 c3 = float(input("Enter your course 3 credit: "))
 print(f"Grade point for course 3 is: {getGradePoint(lg)}")
 gp3 = getGradePoint(lg)
 lg1, lg2, lg3
 GPA = (gp1 * c1 + gp2 * c2 + gp3 * c3) / (c1 + c2 + c3) 
 GPA = print(f"Your GPA is: {GPA}")

if __name__ == "__main__":
 run()