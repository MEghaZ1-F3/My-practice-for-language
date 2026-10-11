student_marks = int(input("Enter marks: "))
if(student_marks>90 and student_marks<=100):
   grade="Ex"
elif( student_marks >80 and student_marks<=90):
   grade="A"
elif(student_marks>70 and student_marks<=80):
   grade="B"
elif(student_marks>60 and student_marks<=70):
   grade="C"
elif(student_marks>50 and student_marks<=60):
   grade="D"
else:
   grade="F"

print(f"Your grad is: {grade}")