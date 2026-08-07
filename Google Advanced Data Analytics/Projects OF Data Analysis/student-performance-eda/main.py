import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load CSV
df = pd.read_csv("student_performance.csv")

# 1. Convert Exam_Date to datetime
df["Exam_Date"] = pd.to_datetime(df["Exam_Date"])
df["Month_Name"] = df["Exam_Date"].dt.month_name()

# 2. Use numpy to create a result status column (Marks>= 60 passes)
df["Status"] = np.where(df["Marks"] >= 60, "Pass", "Fail")
#3 . Calculate average marks per subject
subject_avg = (
  df.groupby("Subject")["Marks"]
  .mean()
  .reset_index()
  .sort_values(by="Marks", ascending=False)
)
print("--- Subject Average Marks ---")
print(subject_avg)

# 4. Data visualization (Matplotlib)
plt.figure(figsize=(8,5))

plt.bar(
  subject_avg["Subject"],
  subject_avg['Marks'],
  color = ["Red", "Blue", "Orange", "Yellow"]
)
plt.title("Average Student Marks by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")

plt.grid(axis="y", linestyle="--" , alpha=0.7)

plt.tight_layout()
plt.savefig("subject_avg_marks.png")
plt.show()
