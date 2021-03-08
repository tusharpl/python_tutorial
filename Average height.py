# Get the input of student height a string separated with spaces
student_heights = input("Enter a list of student heights ").split()
# make the string integer
for n in range(0, len(student_heights)):
    student_heights[n]= int(student_heights[n])
print(student_heights)

total_height = 0
# without using len() count the students
number_of_students = 0
for student in student_heights:
    number_of_students += 1
# without using sum() find the sum of heights
for height in student_heights:
    total_height = total_height + height
# round the value after finding the average
Average_height = round(total_height/number_of_students)
print(Average_height)