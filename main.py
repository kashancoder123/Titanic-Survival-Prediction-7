import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic data
df = pd.read_csv('Titanic Dataset.csv')

# Survival pie chart
df["Survived"].value_counts().plot.pie(kind='pie', autopct='%1.1f%%', colors=['red', 'green']) 
labels=['Did Not Survive', 'Survived'],
figsize=(4, 4)
plt.title('Survival Distribution')
plt.ylabel('')
plt.show()



# Survival by Gender (bar chart)
df.groupby("Gender")["Survived"].mean().plot(kind="bar", color=['blue', 'pink'])
plt.title("Survival Rate")
plt.ylabel("Survival Rate")
plt.show()


df.groupby("Pclass")["Survived"].mean().plot(kind="bar")