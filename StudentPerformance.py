import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_excel("studentMarkSheet.xlsx")

# Show first few rows
print("Dataset Preview:")
print(df.head())

# Calculate average score for each student
df["Average"] = df[['Maths', 'Science', 'English', 'Telugu']].mean(axis=1)

# Find top performer
top_student = df[df["Average"] == df["Average"].max()]
print("\nTop Performer:")
print(top_student[["Name", "Average"]])

# Plot subject-wise average marks
subject_avg = df[['Maths', 'Science', 'English', 'Telugu']].mean()
subject_avg.plot(kind='bar', title="Subject-wise Average Marks", color='skyblue')
plt.ylabel("Average Marks")
plt.show()

# Grade distribution (simple logic)
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(get_grade)
print("\nGrade Distribution:")
print(df["Grade"].value_counts())

# Plot grade distribution
sns.countplot(x="Grade", data=df, palette="pastel")
plt.title("Grade Distribution")
plt.show()
