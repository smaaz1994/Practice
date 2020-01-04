#Assignment: superstore management

students=[]

def addstudent():   #Add
    student = {}
    student['Name'] = input('Enter Name: ')
    student['Age'] = input('Enter Age: ')
    student['Father Name'] = input("Enter Father's Name: ")
    student['Address'] = input('Enter Address: ')
    students.append(student)
    print("Request Processed Succesfully!")

def delstudent():   #Delete Record
    delentry = input("Enter Student's Name: ")
    ind = 0
    for student in students:
        if student['Name']==delentry:
            del students[ind]
            break
        else:
            print("No such Entry Exists!")
        ind += 1

def editstudent(x):
    for i in range(len(students)):
        if x == i:
            print(students[x])
            students[i]['Name'] =  input("Name: ")
            students[i]['Father Name'] = input("Father Name: ")
            students[i]['Age'] = input("Age: ")
            students[i]['Address'] = input("Address: ")
            students[i]['Contact'] = input("Contact: ")
            print("\nRecord edited!")
            break

def displaystudent():
    for i in range(len(students)):
        print('ID:\t',i,'\n===========')
        print(students[i])

def searchrecord(xp):
    for i in range(len(students)):
        if xp == i:
            print(students[xp])
            break
        else:
            print("Record not found!")

while True:
    print("Press 1 to Add Student")
    print("Press 2 to Edit Student")
    print("Press 3 to Search Student")
    print("Press 4 to Delete Student")
    print("Press 5 to Display All Records")
    print("Press 6 to Exit")
    
    option = int(input("Enter 1 - 6: "))

    if option == 1:
        addstudent()
    elif option == 2:
        x = int(input("Enter Name: "))
        editstudent(x)
    elif option == 6:
        print("Closing Program....")
        break
    else:
        print("Invalid Option! Exit Program....")
        break
    
