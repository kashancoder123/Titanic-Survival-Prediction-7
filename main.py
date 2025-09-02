import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset
data = pd.read_csv("Titanic Dataset.csv")

# =========================
# 1. Basic Survival Bar Chart
# =========================
survival_counts = data["Survived"].value_counts().sort_index()
plt.bar(["Died", "Survived"], survival_counts, color=["red", "green"])
plt.title("Survival Counts")
plt.xlabel("Passenger Status")
plt.ylabel("Number of Passengers")
plt.show()

# =========================
# 2. Pie Chart for Survival
# =========================
plt.pie(survival_counts,
        labels=["Died", "Survived"],
        autopct="%1.1f%%",
        colors=["red", "green"],
        startangle=90,
        shadow=True)
plt.title("Survival Distribution")
plt.show()

# =========================
# 3. Survival by Gender
# =========================
plt.figure(figsize=(6,4))
sns.countplot(data=data, x="Survived", hue="Sex", palette={"male":"blue", "female":"pink"})
plt.title("Survival by Gender")
plt.xlabel("Passenger Status (0 = Died, 1 = Survived)")
plt.ylabel("Count")
plt.show()

# =========================
# 4. Survival by Passenger Class
# =========================
plt.figure(figsize=(6,4))
sns.countplot(data=data, x="Pclass", hue="Survived", palette=["red", "green"])
plt.title("Survival by Passenger Class")
plt.xlabel("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)")
plt.ylabel("Count")
plt.show()
