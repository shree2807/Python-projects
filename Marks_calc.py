import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean, median, mode, stdev, variance

# Step 1: Load Dataset
df = pd.read_csv('marks.csv')

# Step 2: Extract Marks
marks = df['Marks'].tolist()

# Step 3: Perform Statistical Analysis
mean_val = mean(marks)
median_val = median(marks)
mode_val = mode(marks)
std_dev = stdev(marks)
var_val = variance(marks)

# Step 4: Print Statistics
print("📊 Statistical Analysis of Student Marks:")
print(f"Mean               : {mean_val}")
print(f"Median             : {median_val}")
print(f"Mode               : {mode_val}")
print(f"Standard Deviation : {std_dev:.2f}")
print(f"Variance           : {var_val:.2f}")

# Step 5: Visualizations
# Histogram
plt.figure(figsize=(10, 5))
sns.histplot(marks, bins=5, kde=True, color='pink')
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(y=marks, color='lightgreen')
plt.title("Marks Boxplot")
plt.ylabel("Marks")
plt.grid(True)
plt.show()