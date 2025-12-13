print(f"-----------------------------------------")
print(f"STUDENT PROGRESS TRACKER SYSTEM ")
print("-----------------------------------------")
#
name=input("Enter the name of the student: ")
class_room=input("Enter the student's class room number: ")
roll_no=input("Enter the student pin number: ")
subject=int(input("Enter the number of subjects: "))
total_marks=int(input("Enter the total marks of all subjects: "))
def enter_marks():
    failed_subject=0
    passed_subject=0
    all_subject_marks=[]
    awarded_marks=0
    for i in range(1,subject+1):
        while True:
          
          marks=int(input(f"The subject-{i} marks: "))
          all_subject_marks.append(marks)
          awarded_marks+=marks  
          print(total_marks)  
          if marks<35:
               failed_subject=True
          else:
               passed_subject=True 
          break
    average_marks=awarded_marks/subject
    marks_percentage=(awarded_marks/total_marks)*100
    if average_marks>90:
         print("GRADE A")
    elif average_marks>75 and average_marks<89:
         print("GRADE B")
    elif average_marks>50 and average_marks<74:
         print("GRADE C")
    elif average_marks>35 and average_marks<49:
         print("GRADE D")
    else:
         print("FAIL")

    #PASS/FAIL LOGIC
    if failed_subject==True:
          result="FAIL"
    else:
          result="PASS"


    return marks,all_subject_marks,average_marks,awarded_marks,result,passed_subject,failed_subject,marks_percentage
marks,all_subject_marks,average_marks,awarded_marks,result,passed_subject,failed_subject,marks_percetage=enter_marks()
def report():
    print("\n\n-----------------------------------------")
    print("\n\n-----------------------------------------")
    print("STUDENT PROGRESS REPORT ")
    print("----------------------------------------- ")
    print(f"Name: {name}")
    print(f"Class: {class_room}")
    print(f"Roll No: {roll_no}")
    print(f"Total Marks: {awarded_marks}")
    print(f"Average: {average_marks}")
    print(f"Marks Percentage: {marks_percetage}")
    print(f"Result: {result}")
    print(f"----------------------------------------- ")  
    return name,class_room,roll_no,awarded_marks,average_marks,marks_percentage,result
name,class_room,roll_no,awarded_marks,average_marks,marks_percentage,result=report()
while True:
     print("MENU:")
     print(f"What do you want to do next? ")
     print(f"1.Enter marks again?")
     print(f"2. View report again?")
     print(f"3. Exit! ")
     choice=int(input("Enter a choice from 1 to 3 "))
     if choice==1:
          marks,all_subject_marks,average_marks,awarded_marks,result,passed_subject,failed_subject,marks_percentage=enter_marks()
     elif choice==2:
          name,class_room,roll_no,awarded_marks,marks_percetage,average_marks,result = report()
     elif choice==3:
          print("Exiting!")
          break
     else:
          print("Enter a valid choice :")