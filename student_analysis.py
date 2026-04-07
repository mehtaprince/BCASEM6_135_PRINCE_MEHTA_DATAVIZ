import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Karan"],
    "Graduation_Percentage": [75, 82, 68, 90, 77],
    "Age": [21, 22, 20, 23, 21]
}
df = pd.DataFrame(data)

# Display DataFrame
print("Student Data:\n")
print(df)

# Calculate average age
avg_age = df["Age"].mean()
print("\nAverage Age of Students:", avg_age)

avg_percentage = df["Graduation_Percentage"].mean()
print("Average Graduation Percentage:", avg_percentage)

print("\nBasic Statistics using describe():\n")
print(df.describe())