import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ai_job_dataset.csv")
print(df)  # View first 5 rows

df.shape              # Rows, columns
df.info()             # Data types and null values
df.describe()         # Summary of numerical columns
df.columns.tolist()   # Column names

df.isnull().sum().sort_values(ascending=False)

df.duplicated().sum()   # Number of duplicate rows
df.drop_duplicates(inplace=True)

#salary distribution
sns.histplot(df['salary_usd'], kde=True)
plt.title('Salary Distribution (USD)')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

#univariate analysis
top_jobs = df['job_title'].value_counts().head(10)
sns.barplot(y=top_jobs.index, x=top_jobs.values)
plt.title('Top 10 Job Titles')
plt.xlabel('Count')
plt.ylabel('Job Title')
plt.show()

df['employment_type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Employment Type Distribution')
plt.ylabel('')
plt.show()

#bivariate analysis
sns.boxplot(x='experience_level', y='salary_usd', data=df)
plt.title('Salary by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Salary (USD)')
plt.show()

#bivariate analysis
sns.countplot(x='remote_ratio', hue='company_size', data=df)
plt.title('Remote Ratio by Company Size')
plt.xlabel('Remote Work %')
plt.ylabel('Number of Jobs')
plt.show()

#multivariate analysis
plt.figure(figsize=(12, 6))
sns.boxplot(x='industry', y='salary_usd', hue='experience_level', data=df)
plt.xticks(rotation=45)
plt.title('Salary Distribution by Industry and Experience Level')
plt.show()

df.to_csv("cleaned_jobs_data.csv", index=False)
