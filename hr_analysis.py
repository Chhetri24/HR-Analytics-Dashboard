import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("HR_Employee_Attrition.csv")

# =========================
# BASIC INFORMATION
# =========================
print("=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("ATTRITION COUNTS")
print("=" * 50)
print(df['Attrition'].value_counts())

# =========================
# ATTRITION RATE
# =========================
attrition_rate = (
    df[df['Attrition'] == 'Yes'].shape[0]
    / df.shape[0]
) * 100

print("\nAttrition Rate: {:.2f}%".format(attrition_rate))

# =========================
# ATTRITION CHART
# =========================
plt.figure(figsize=(6,4))
sns.countplot(x='Attrition', data=df)
plt.title('Employee Attrition')
plt.savefig('attrition_count.png')
plt.show()

# =========================
# OVERTIME VS ATTRITION
# =========================
plt.figure(figsize=(7,4))
sns.countplot(x='OverTime', hue='Attrition', data=df)
plt.title('Attrition by Overtime')
plt.savefig('attrition_overtime.png')
plt.show()

# =========================
# DEPARTMENT VS ATTRITION
# =========================
plt.figure(figsize=(8,5))
sns.countplot(y='Department', hue='Attrition', data=df)
plt.title('Attrition by Department')
plt.savefig('attrition_department.png')
plt.show()

# =========================
# JOB ROLE VS ATTRITION
# =========================
plt.figure(figsize=(12,6))
sns.countplot(y='JobRole', hue='Attrition', data=df)
plt.title('Attrition by Job Role')
plt.savefig('attrition_jobrole.png')
plt.show()

# =========================
# MONTHLY INCOME
# =========================
plt.figure(figsize=(8,4))
sns.histplot(df['MonthlyIncome'], bins=30)
plt.title('Monthly Income Distribution')
plt.savefig('monthly_income_distribution.png')
plt.show()

# =========================
# AGE DISTRIBUTION
# =========================
plt.figure(figsize=(8,4))
sns.histplot(df['Age'], bins=20)
plt.title('Employee Age Distribution')
plt.savefig('age_distribution.png')
plt.show()

# =========================
# EXPORT CLEANED DATA
# =========================
df.to_csv("HR_Employee_Attrition_Cleaned.csv", index=False)

print("\nCleaned dataset exported successfully!")
print("Charts saved successfully!")
