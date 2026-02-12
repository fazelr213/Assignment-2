# Import pandas to work with csv file
import pandas as pd

# Load the dataset
data_frame_crime_csv = pd.read_csv("crime.csv")

# Create risk column
data_frame_crime_csv["risk"] = "LowCrime"
data_frame_crime_csv.loc[data_frame_crime_csv["ViolentCrimesPerPop"] >= 0.50, "risk"] = "HighCrime"

# Group by risk and calculate average unemployment
result = data_frame_crime_csv.groupby("risk")["PctUnemployed"].mean() * 100

# Print results clearly
print("Average Unemployment Rate:")
print(f"HighCrime:, {result["HighCrime"]}%")
print(f"LowCrime:, {result["LowCrime"]}%")
