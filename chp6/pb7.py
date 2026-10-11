student_marks = int(input("Enter marks: "))
if(student_marks>90 and student_marks<=100):
    print("Excellent")
elif( student_marks >80 and student_marks<=90):
    print("A")
elif(student_marks>70 and student_marks<=80):
    print("B")
elif(student_marks>60 and student_marks<=70):
    print("C")
elif(student_marks>50 and student_marks<=60):
    print("D")
else:
    print("F")