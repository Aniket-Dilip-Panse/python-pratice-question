# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# '''
# Can be solved in 2 parts:
# 1st part:
# 1.Take name and score as input
# 2.Store name and score in nested list `students_grade`
# 3.Make a Unique_sorted_score_list that is unique(using set()) and sorted(using sorted()) scores
# 4.Fetch second_lowest_score from Unique_sorted_score_list
# 2nd part:
# 1.create an empty list => low_student_list
# 2.for every student in `students_grade`
# 3.check if second_lowest_score match any student[score]
# 4.if Yes: append in student_list
# 5.iterate through `low_student_list` to print result
# '''

students_grade = []
for _ in range(int(input("enter the size of list "))):
    name = input("enter student name ")
    score = int(input(f"enter {name} score "))
    students_grade.append([name,score])
stored_scores = sorted(list(set([x[1] for x in students_grade])))
second_lowest = stored_scores[1]

low_final_list = []
for student in students_grade:
    # checking 2nd largest_score to each student[score]
    if second_lowest == student[1]:
        low_final_list.append(student[0])
for student in sorted(low_final_list):
    print(student)