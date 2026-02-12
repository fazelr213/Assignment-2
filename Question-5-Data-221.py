# Import pandas library for working with tables
import pandas as pd

# Read the csv file into a dataframe
data_frame_studentcsv = pd.read_csv("student.csv")

# Create a new column called grade_band and set default value to "High"
data_frame_studentcsv["grade_band"] = "High"

# Change grade_band to "Medium" for grades 14 or below
data_frame_studentcsv.loc[data_frame_studentcsv["grade"] <= 14, "grade_band"] = "Medium"

# Change grade_band to "Low" for grades 9 or below
data_frame_studentcsv.loc[data_frame_studentcsv["grade"] <= 9, "grade_band"] = "Low"

# Group data by grade_band and calculate summary statistics
summary_of_data_set = data_frame_studentcsv.groupby("grade_band").agg(
    students=("grade", "count"),  # Count number of students
    avg_absences=("absences", "mean"),  # Calculate average absences
    pct_internet=("internet", "mean")  # Calculate average of internet column (0/1)
).reset_index()

# Convert internet proportion to percentage
summary_of_data_set["pct_internet"] = summary_of_data_set["pct_internet"] * 100

# Save the summary table to a new CSV file
summary_of_data_set.to_csv("student_bands.csv", index=False)

# Print the final summary table
print(summary_of_data_set)
