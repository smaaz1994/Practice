print("=======================================================================")

name = input("Enter Name: ")
class_y = input("Enter Year: ")
class_s = input("Enter Semester: ")


print("===================== Enter Marks Obtained ============================")

subject1 = float(input("Enter English Marks: "))
subject2 = float(input("Enter Islamiat Marks: "))
subject3 = float(input("Enter Computer Marks: "))
subject4 = float(input("Enter Maths Marks: "))
subject5 = float(input("Enter Physics Marks: "))
subject6 = float(input("Enter Chemistry Marks: "))
subject7 = float(input("Enter Urdu Marks: "))

print("========================== Data Acquired =============================")

maxmarks = float(input("Enter Max Marks: "))

print("=======================================================================")

Gradepassed = bool

if subject1 > 50 and subject2 > 50 and subject3 > 50 and subject4 > 50 and subject5 > 50 and subject6 > 50 and subject7 > 50:
    Gradepassed = True

percentage_ = ((subject1 + subject2 + subject3 + subject4 + subject5 + subject6 + subject7)/(maxmarks*7)) * 100
percentage = int(percentage_)

Totalgrade = ""

if percentage > 89:
    Totalgrade = "A+"

elif 90 > percentage > 79:
    Totalgrade = "A" 

elif 80 > percentage > 69:
    Totalgrade = "B" 

elif 70 > percentage > 59:
    Totalgrade = "C" 

elif 60 > percentage > 49:
    Totalgrade = "D" 

else:
    Totalgrade = "F"

print("                                                                       ")
print("                                                                       ")

print("------------------------ Mark Sheet -----------------------------------")
print("=======================================================================")
print("                                                                       ")

print("Name: ", name)

print("                                                                       ")

print("Year: " + class_y + "\nSemester: " + class_s)

print("                                                                       ")

if Gradepassed == True:
    print("Semester Examination Passed with Grade: ", Totalgrade)
else: 
    print("Semester Examination Failed. Overall Grade: ", Totalgrade)
    
print("                                                                       ")

print("Percentage: "+ str(format(percentage_, '.2f')) + "%")

print("                                                                       ")
print("...................................................................... ")
print("                                                                       ")

print("English Marks: ", subject1)

print("                                                                       ")

print("Islamiat Marks: ", subject2)

print("                                                                       ")

print("Computer Marks: ", subject3)

print("                                                                       ")

print("Maths Marks: ", subject4)

print("                                                                       ")

print("Physics Marks: ", subject5)

print("                                                                       ")

print("Chemistry Marks: ", subject6)

print("                                                                       ")

print("Urdu Marks: ", subject7)

print("                                                                       ")
print("========================== The End ====================================")