marks_list = []
for m in range(5):
    marks = int(input("Enter marks in a subject: "))
    marks_list.append(marks)

average = sum(marks_list)/5
percentage = sum(marks_list)/50*100 #assuming each subject is for 10 marks

print("Average marks: "+str(average))
print("Percentage marks: "+str(percentage))