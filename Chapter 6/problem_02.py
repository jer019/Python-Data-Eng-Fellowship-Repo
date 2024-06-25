# create a program which tells if the student is pass or fail based on the percentage in 3 subjects
# student is considered pass in the exa if he have atleast total 40% and 33% in each subject

# marks input
marks1=int(input("Enter marks of subject1: "))
marks2=int(input("Enter marks of subject2: "))
marks3=int(input("Enter marks of subject3: "))

# calculate percentage
total_percentage=(100*(marks1+marks2+marks3))/300

if(total_percentage >= 40 and marks1 >=33 and marks2>=33 and marks3>=33):
    print("You passed the exam with total percentage= ",total_percentage)

else:
    print("You failed! try your best next time!",total_percentage)

