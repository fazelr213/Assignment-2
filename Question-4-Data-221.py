# Import pandas to work with csv data
import pandas as pd

# Load the student dataset into a dataframe
data_frame_student_csv = pd.read_csv("student.csv")

# Filter students who:
# - study time is 3 or more
# - have internet access (1)
# - have 5 or fewer absences
filtered_students = data_frame_student_csv[
    (data_frame_student_csv["studytime"] >= 3) &
    (data_frame_student_csv["internet"] == 1) &
    (data_frame_student_csv["absences"] <= 5)
]

# Save the filtered students to a new CSV file
filtered_students.to_csv("high_engagement.csv", index=False)

# Print the number of students that were saved
print("Students saved:", len(filtered_students))

# Print the average grade of the filtered students
print("Average Grade:", filtered_students["grade"].mean())

