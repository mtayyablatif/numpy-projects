import numpy as np


total_subjects = int(input("How many subjects in total?: "))
marks_list = []
subjects_list = []

for i in range(total_subjects):
    subject = input(f"Enter the name of {i+1} subject: ")
    mark = int(input(f"Enter the marks of that subject: "))
    subjects_list.append(subject)
    marks_list.append(mark)

subjects = np.array(subjects_list)
marks = np.array(marks_list)

# marks = np.array([91, 89, 85, 78, 64, 66])
# subjects = np.array(['Anthropology', 'IT', 'Financial Accounting', 'Management Accounting', 'Economics', 'Statistics-II'])

mean = np.mean(marks)
max_marks = np.max(marks)
min_marks = np.min(marks)

position_max_marks = np.argmax(marks)
position_min_marks = np.argmin(marks)

best_subject = subjects[position_max_marks]
worst_subject = subjects[position_min_marks]

pass_fail = marks >= 50

print("=" * 45)
print(f"{'STUDENT REPORT CARD':^45}")
print("=" * 45)
print(f"{'Subject':<25}{'Marks':<10}{'Status':<10}")
print("-" * 45)

for subject, mark, passed in zip(subjects, marks, pass_fail):
    status = "PASS" if passed else "FAIL"
    print(f"{subject:<25}{mark:<10}{status:<10}")

print("-" * 45)
print(f"Average Marks   : {mean:.2f}")
print(f"Best Subject    : {best_subject} ({max_marks})")
print(f"Weakest Subject : {worst_subject} ({min_marks})")
print("=" * 45)

