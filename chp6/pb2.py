subject1 = int(input("Enter marks of student: "))
subject2 = int(input("Enter marks of student: "))
subject3 = int(input("Enter marks of student: "))

total_percentage = ((subject1+subject2+subject3)/300)*100
if(total_percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33):
    print(f"You are pass congratulation: {total_percentage}")
else:
    print(f"you  are faill: {total_percentage}")