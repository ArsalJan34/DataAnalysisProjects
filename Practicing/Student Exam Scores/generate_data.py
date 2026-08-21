import numpy as np
import pandas as pd

np.random.seed(42)
n = 100
data = {
  "Student_ID": [f"STU_{i:03d}" for i in range(1,n+1)],
  "Gender": np.random.choice(["Male", "Female"], size=n),
  "Grade_Level":np.random.choice(["Grade 10", "Grade 11", "Grade 12" ],size=n),
  "Math_Score": np.random.randint(40,100, size=n),
  "English_Score": np.random.randint(50,100, size=n),
  "Passed": np.random.choice(["Yes","No"], size=n, p=[0.85,0.15])

}
df_students = pd.DataFrame(data)
df_students.to_csv("students_score.csv",index=False)
print("students_scores.csv created!")
