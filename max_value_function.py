# Get the list of values ..here it is student scores
student_scores = input("Enter the list of student scores").split()

# change str to integer so that calculations can be done

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# find max value through iteration instead of function
max_score = 0

for score in student_scores:
    if ( score > max_score):
        max_score = score

print(f" The highest score in the class is : {max_score}")