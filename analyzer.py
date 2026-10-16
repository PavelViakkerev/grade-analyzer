import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')

#average grade
df['average_grade'] = df[['math', 'physics', 'english']].mean(axis=1)

#summary statistics
summary = df.describe()

#Top 3 students
top_students = df.sort_values('average_grade', ascending=False).head(3)

#best student
best_student=df.loc[df['average_grade'].idxmax()]

#worst student
worst_student=df.loc[df['average_grade'].idxmin()]

#most difficult subject
most_difficult_subject = df[['math', 'physics', 'english']].std().idxmax()

#output
print('data set: ', df)
print('summary statistics: ', summary)
print('Top 3 students: ', top_students)
print('Best student: ', best_student)
print('Worst student: ', worst_student)
print('Most difficult subject: ', most_difficult_subject)

#visualization
sns.barplot(data=df, x='name', y='average_grade')
plt.title('Average Grades of Students')
plt.xlabel('Students Name')
plt.ylabel('Average Grade')
plt.show()
