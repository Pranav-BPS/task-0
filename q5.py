#q5.py
import pandas as pd
import numpy as np
df=pd.read_csv("student_performance.csv")
print(df.head())
print(df.shape)
for col in df.columns:
    print(col)
if df.isnull().sum().values.any() == 0:
    print("There are missing values in the dataset.")
else:
    print("There are no missing values in the dataset.")
print("mean of Final_score:",df['Final_Score'].mean())
print(df.loc[df["Final_Score"].idxmax(), "Student"])
df['Improvement'] = df['Final_Score'] - df['Previous_Score']
print(df.loc[df['Attendance'] > 80, 'Student'])
df=df.sort_values('Final_Score', ascending=False)
df.to_csv("processed_student_performance.csv", index=False)