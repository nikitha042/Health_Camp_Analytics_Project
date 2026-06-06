import pandas as pd

# Load datasets
train = pd.read_csv("data/Train.csv.zip")
camp = pd.read_csv("data/Health_Camp_Detail.csv")
attendance = pd.read_csv("data/First_Health_Camp_Attended.csv")

# Display dataset information
print("Train Dataset Shape:", train.shape)
print("Camp Dataset Shape:", camp.shape)
print("Attendance Dataset Shape:", attendance.shape)

print("\nTrain Columns:")
print(train.columns.tolist())

print("\nCamp Columns:")
print(camp.columns.tolist())

print("\nAttendance Columns:")
print(attendance.columns.tolist())

# Merge attendance and train data
merged = pd.merge(
    attendance,
    train,
    on=["Patient_ID", "Health_Camp_ID"],
    how="left"
)

# Merge with camp details
merged = pd.merge(
    merged,
    camp,
    on="Health_Camp_ID",
    how="left"
)

# Display merged dataset information
print("\nMerged Dataset Shape:", merged.shape)

print("\nFirst 5 Rows:")
print(merged.head())

# Check missing values
print("\nMissing Values:")
print(merged.isnull().sum())

# Save merged dataset
merged.to_csv(
    "output/cleaned_data.csv",
    index=False
)

print("\ncleaned_data.csv saved successfully in output folder!")
# Save merged dataset
merged.to_csv(
    "output/cleaned_data.csv",
    index=False
)

print("\ncleaned_data.csv saved successfully in output folder!")

# ----------------- Graphs -----------------

import matplotlib.pyplot as plt

# Camp Category Count
merged["Category1"].value_counts().plot(kind="bar")
plt.title("Health Camp Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/camp_categories.png")
plt.close()

# Donation Distribution
merged["Donation"].hist(bins=10)
plt.title("Donation Distribution")
plt.xlabel("Donation Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/donation_distribution.png")
plt.close()

# Health Score Distribution
merged["Health_Score"].hist(bins=10)
plt.title("Health Score Distribution")
plt.xlabel("Health Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/health_score_distribution.png")
plt.close()

print("Graphs saved successfully!")